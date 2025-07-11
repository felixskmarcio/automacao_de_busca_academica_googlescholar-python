import asyncio
import json
from playwright.async_api import async_playwright

SEARCH_URL = "https://scholar.google.com.br/scholar?hl=pt-BR&as_sdt=0%2C5&q=prompt+engineering&lr=lang_pt&oq="
OUTPUT_FILE = "Automação/Busca_Acad_mica.json"
MAX_PAGES = 50  # Limite máximo de páginas para evitar loops infinitos

class ArticleInfo:
    def __init__(self, title, authors, year, journal, abstract, url, doi, citations, source, search_term):
        self.title = title
        self.authors = authors
        self.year = year
        self.journal = journal
        self.abstract = abstract
        self.url = url
        self.doi = doi
        self.citations = citations
        self.source = source
        self.search_term = search_term

    def to_dict(self):
        return self.__dict__

async def extract_article_info(page, article_element, search_term):
    try:
        title_el = await article_element.query_selector('h3')
        title = await title_el.inner_text() if title_el else None
        
        url_el = await article_element.query_selector('h3 a')
        url = await url_el.get_attribute('href') if url_el else None
        
        meta_el = await article_element.query_selector('.gs_a')
        meta = await meta_el.inner_text() if meta_el else ""
        
        authors, year, journal = None, None, None
        if meta:
            parts = meta.split(" - ")
            authors = parts[0]
            if len(parts) > 1:
                journal_year = parts[1]
                import re
                year_match = re.search(r'(\d{4})', journal_year)
                year = year_match.group(1) if year_match else None
                journal = journal_year.replace(year, "").strip() if year else journal_year
        
        abstract_el = await article_element.query_selector('.gs_rs')
        abstract = await abstract_el.inner_text() if abstract_el else None
        
        doi = None
        if url and "doi.org" in url:
            doi = url.split("doi.org/")[-1]
        
        citations = None
        cite_link = await article_element.query_selector('a:has-text("Citado por")')
        if cite_link:
            cite_text = await cite_link.inner_text()
            import re
            match = re.search(r'Citado por (\d+)', cite_text)
            if match:
                citations = int(match.group(1))
        
        return ArticleInfo(
            title=title,
            authors=authors,
            year=year,
            journal=journal,
            abstract=abstract,
            url=url,
            doi=doi,
            citations=citations,
            source="Google Scholar",
            search_term=search_term
        )
    except Exception as e:
        print(f"Erro ao extrair informações do artigo: {e}")
        return None

async def find_next_button(page):
    """Tenta encontrar o botão 'Próxima' usando diferentes seletores"""
    selectors = [
        'button[aria-label="Próxima"]',
        'a[aria-label="Próxima"]',
        'td[align=right] a.gs_nma',
        'span.gs_ico_nav_next',
        'a:has-text("Próxima")',
        'a:has-text("Next")',
        '.gs_ico_nav_next',
        '#gs_n td:last-child a'
    ]
    
    for selector in selectors:
        button = await page.query_selector(selector)
        if button:
            return button
    return None

async def main():
    search_term = "prompt engineering"
    print(f"Iniciando busca por: {search_term}")
    print(f"URL: {SEARCH_URL}")
    
    async with async_playwright() as p:
        # Mudança para headless=False para debug (você pode mudar para True depois)
        browser = await p.chromium.launch(headless=False, slow_mo=1000)
        page = await browser.new_page()
        
        # Configurações para evitar detecção de bot
        await page.set_extra_http_headers({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
        await page.goto(SEARCH_URL)
        results = []
        page_num = 1
        
        while page_num <= MAX_PAGES:
            print(f"\n--- Página {page_num} ---")
            
            # Verifica se há CAPTCHA
            captcha = await page.query_selector('form#captcha-form')
            if captcha:
                print("❌ CAPTCHA detectado! Parando a automação.")
                break
            
            # Aguarda carregar os resultados
            try:
                await page.wait_for_selector('.gs_r', timeout=10000)
            except:
                print("❌ Timeout ao carregar resultados. Parando.")
                break
            
            articles = await page.query_selector_all('.gs_r')
            print(f"📄 {len(articles)} artigos encontrados nesta página")
            
            if len(articles) == 0:
                print("❌ Nenhum artigo encontrado. Parando.")
                break
            
            # Extrai informações dos artigos
            for i, article in enumerate(articles):
                info = await extract_article_info(page, article, search_term)
                if info:
                    results.append(info.to_dict())
                    title_preview = info.title[:50] if info.title else "Sem título"
                    print(f"  ✅ Artigo {i+1}: {title_preview}...")
                else:
                    print(f"  ❌ Erro ao extrair artigo {i+1}")
            
            # Procura o botão "Próxima"
            next_button = await find_next_button(page)
            
            if next_button:
                print("🔄 Indo para a próxima página...")
                await next_button.click()
                await page.wait_for_timeout(3000)  # Espera 3 segundos
                page_num += 1
            else:
                print("✅ Não há mais páginas. Busca finalizada!")
                break
        
        print(f"\n📊 Total de artigos coletados: {len(results)}")
        
        # Salva no arquivo JSON
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        
        print(f"💾 Resultados salvos em: {OUTPUT_FILE}")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main()) 