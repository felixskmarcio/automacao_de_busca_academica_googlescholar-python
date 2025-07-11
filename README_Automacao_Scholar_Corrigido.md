# 📚 Automação de Busca Acadêmica Google Scholar - Python

Este projeto contém um script Python que automatiza buscas acadêmicas no Google Scholar usando Playwright para scraping web inteligente.

## 🤖 O que faz o Script

O `busca_scholar.py` é uma automação que:

- 🔍 **Busca automaticamente** no Google Scholar
- 📄 **Extrai informações** de artigos acadêmicos
- 🔄 **Navega por múltiplas páginas** automaticamente
- 💾 **Salva resultados** em arquivo JSON estruturado
- 🛡️ **Evita detecção** de bot com headers customizados
- ⚠️ **Detecta CAPTCHA** e para quando necessário

## 🚀 Como Executar

### 📋 Pré-requisitos

1. **Python 3.7+** instalado
2. **Instalar dependências:**

```bash
pip install playwright asyncio
```

3. **Instalar browsers do Playwright:**

```bash
playwright install chromium
```

### ▶️ Executando o Script

1. **Execute o comando:**

```bash
python busca_scholar.py
```

2. **O script irá:**
   - Abrir o navegador automaticamente
   - Buscar por "prompt engineering" (configurável)
   - Extrair dados de até 50 páginas
   - Salvar em `Automação/Busca_Acad_mica.json`

## ⚙️ Configuração

### 🔧 Parâmetros Principais

No arquivo `busca_scholar.py`, você pode alterar:

```python
# Termo de busca e URL
SEARCH_URL = "https://scholar.google.com.br/scholar?hl=pt-BR&as_sdt=0%2C5&q=prompt+engineering&lr=lang_pt&oq="
search_term = "prompt engineering"  # Linha 94

# Arquivo de saída
OUTPUT_FILE = "Automação/Busca_Acad_mica.json"

# Limite de páginas
MAX_PAGES = 50
```

### 🎯 Personalizações

1. **Alterar termo de busca:**
   ```python
   # Linha 94 - modifique o termo
   search_term = "machine learning"
   
   # Linha 4 - atualize a URL com o novo termo codificado
   SEARCH_URL = "https://scholar.google.com.br/scholar?hl=pt-BR&as_sdt=0%2C5&q=machine+learning&lr=lang_pt&oq="
   ```

2. **Mudar idioma da busca:**
   ```python
   # Para inglês:
   SEARCH_URL = "https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=prompt+engineering&lr=lang_en&oq="
   ```

3. **Executar sem interface (headless):**
   ```python
   # Linha 98 - mudar para True
   browser = await p.chromium.launch(headless=True, slow_mo=1000)
   ```

4. **Ajustar velocidade:**
   ```python
   # Linha 98 - aumentar slow_mo para ir mais devagar
   browser = await p.chromium.launch(headless=False, slow_mo=2000)
   ```

## 📊 Estrutura dos Dados de Saída

### 📋 Arquivo JSON Gerado:

```json
[
  {
    "title": "Título do Artigo Acadêmico",
    "authors": "Autor A, Autor B, Autor C",
    "year": "2023",
    "journal": "Nome da Revista ou Conferência",
    "abstract": "Resumo ou snippet do artigo extraído do Scholar",
    "url": "https://link-direto-para-o-artigo.com",
    "doi": "10.1000/exemplo.doi",
    "citations": 25,
    "source": "Google Scholar",
    "search_term": "prompt engineering"
  }
]
```

### 🔍 Campos Extraídos

| Campo | Descrição | Exemplo |
|-------|-----------|---------|
| **title** | Título completo do artigo | "Deep Learning for NLP" |
| **authors** | Lista de autores separados por vírgula | "Smith, J., Doe, A." |
| **year** | Ano de publicação | "2023" |
| **journal** | Nome do periódico/conferência | "Nature Machine Intelligence" |
| **abstract** | Resumo ou snippet do artigo | "Este trabalho apresenta..." |
| **url** | Link direto para o artigo | "https://nature.com/articles/..." |
| **doi** | DOI quando disponível | "10.1038/s42256-023-..." |
| **citations** | Número de citações | 15 |
| **source** | Fonte dos dados | "Google Scholar" |
| **search_term** | Termo usado na busca | "prompt engineering" |

## 🛡️ Recursos de Proteção

### 🔒 Anti-Detecção:

- **User-Agent personalizado** para simular navegador real
- **Velocidade controlada** com `slow_mo`
- **Timeouts inteligentes** entre páginas
- **Detecção de CAPTCHA** automática

### ⚠️ Limitações Respeitadas:

- **Máximo de 50 páginas** por execução
- **Pausa de 3 segundos** entre páginas
- **Parada automática** em caso de CAPTCHA
- **Timeout de 10 segundos** para carregamento

## 🚨 Observações Importantes

### ⚠️ Limitações do Google Scholar:

1. **Rate Limiting**: Google pode bloquear IPs com muitas requisições
2. **CAPTCHA**: Aparece automaticamente após muitas buscas
3. **Estrutura HTML**: Pode mudar e quebrar o script
4. **Resultados limitados**: Scholar não mostra todos os artigos

### 💡 Boas Práticas:

1. **Execute com moderação**: Não mais que 2-3 buscas por hora
2. **Use VPN se necessário**: Para evitar bloqueios de IP
3. **Monitore os logs**: Observe mensagens de erro no console
4. **Backup dos dados**: Salve resultados importantes

## 🔧 Solução de Problemas

### 🐛 Problemas Comuns:

| Problema | Causa | Solução |
|----------|-------|---------|
| **Erro de importação** | Playwright não instalado | `pip install playwright` |
| **Browser não encontrado** | Chromium não instalado | `playwright install chromium` |
| **CAPTCHA aparece** | Muitas requisições | Aguarde 1-2 horas e tente novamente |
| **Sem resultados** | Termo muito específico | Tente termos mais amplos |
| **Script trava** | Timeout de rede | Verifique conexão com internet |

### 🔍 Debug e Logs:

1. **Executar com interface visual:**
   ```python
   browser = await p.chromium.launch(headless=False)
   ```

2. **Verificar logs no console:**
   - Mensagens de "✅ Artigo extraído"
   - Avisos de "❌ Erro ao extrair"
   - Status de navegação entre páginas

3. **Testar seletores:**
   - O script usa múltiplos seletores para encontrar elementos
   - Se falhar, pode ser mudança na estrutura do Scholar

## 📁 Estrutura do Projeto

```
n8n/
├── busca_scholar.py                     # Script principal
├── README_Automacao_Scholar_Corrigido.md  # Este arquivo
├── SOLUÇÃO_ERRO_IMPORTACAO.md          # Guia de troubleshooting
└── Automação/
    └── Busca_Acad_mica.json            # Arquivo de saída (gerado)
```

## 🎯 Próximos Passos

### 🔄 Melhorias Possíveis:

1. **Interface gráfica** com tkinter
2. **Múltiplos termos** de busca simultâneos
3. **Filtros avançados** (ano, autor, revista)
4. **Export para CSV/Excel**
5. **Integração com APIs** de periódicos
6. **Análise bibliométrica** automática

### 🤝 Contribuições:

- Reporte bugs abrindo issues
- Sugira melhorias
- Contribua com código

## 🎉 Pronto para Usar!

Execute `python busca_scholar.py` e comece a coletar dados acadêmicos automaticamente! 🚀

---

**⚠️ Disclaimer**: Este script é para fins educacionais e de pesquisa. Respeite os termos de uso do Google Scholar e use com responsabilidade.

