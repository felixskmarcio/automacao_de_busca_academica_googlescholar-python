# 📚 Automação de Busca Acadêmica Google Scholar - Python

Este projeto contém um script Python que automatiza buscas acadêmicas no Google Scholar usando Playwright para scraping web inteligente.

## 📑 Índice

- [🤖 O que faz o Script](#-o-que-faz-o-script)
- [🚀 Como Executar](#-como-executar)
- [⚙️ Configuração](#️-configuração)
- [🎯 Personalizações Avançadas](#-personalizações-avançadas)
- [⚡ Guia Rápido de Uso](#-guia-rápido-de-uso)
- [📊 Estrutura dos Dados de Saída](#-estrutura-dos-dados-de-saída)
- [🛡️ Recursos de Proteção](#️-recursos-de-proteção)
- [🚨 Observações Importantes](#-observações-importantes)
- [🔧 Solução de Problemas](#-solução-de-problemas)
- [📁 Estrutura do Projeto](#-estrutura-do-projeto)
- [❓ Perguntas Frequentes (FAQ)](#-perguntas-frequentes-faq)
- [🎯 Próximos Passos](#-próximos-passos)

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

Abra o arquivo `busca_scholar.py` e encontre estas configurações no início do código:

#### 📍 Localização no código:
```python
# Linhas 3-6: Configurações principais
SEARCH_URL = "https://scholar.google.com.br/scholar?hl=pt-BR&as_sdt=0%2C5&q=prompt+engineering&lr=lang_pt&oq="
OUTPUT_FILE = "Automação/Busca_Acad_mica.json"
MAX_PAGES = 50

# Linha 94: Termo de busca (dentro da função main)
search_term = "prompt engineering"
```

#### 🎯 Como Configurar:

| Parâmetro | Localização | Descrição | Exemplo |
|-----------|-------------|-----------|---------|
| **`SEARCH_URL`** | Linha 3 | URL completa do Google Scholar | Ver geradores abaixo ⬇️ |
| **`search_term`** | Linha 94 | Termo de busca (precisa coincidir com URL) | `"inteligência artificial"` |
| **`OUTPUT_FILE`** | Linha 4 | Caminho do arquivo de saída | `"resultados/ia_2024.json"` |
| **`MAX_PAGES`** | Linha 5 | Limite máximo de páginas | `25` (recomendado 10-50) |

#### 🛠️ Geradores de URL Prontos:

**Para Português Brasileiro:**
```python
# Template base
base_url = "https://scholar.google.com.br/scholar?hl=pt-BR&as_sdt=0%2C5&q={TERMO}&lr=lang_pt&oq="

# Exemplos prontos para copiar:
SEARCH_URL = "https://scholar.google.com.br/scholar?hl=pt-BR&as_sdt=0%2C5&q=inteligencia+artificial&lr=lang_pt&oq="
SEARCH_URL = "https://scholar.google.com.br/scholar?hl=pt-BR&as_sdt=0%2C5&q=machine+learning&lr=lang_pt&oq="
SEARCH_URL = "https://scholar.google.com.br/scholar?hl=pt-BR&as_sdt=0%2C5&q=deep+learning&lr=lang_pt&oq="
SEARCH_URL = "https://scholar.google.com.br/scholar?hl=pt-BR&as_sdt=0%2C5&q=blockchain&lr=lang_pt&oq="
```

**Para Inglês:**
```python
# Template base
base_url = "https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q={TERMO}&lr=lang_en&oq="

# Exemplos prontos:
SEARCH_URL = "https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=artificial+intelligence&lr=lang_en&oq="
SEARCH_URL = "https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=natural+language+processing&lr=lang_en&oq="
```

#### 💡 Dicas para Criar URLs:

1. **Substitua espaços por `+`**: "prompt engineering" → "prompt+engineering"
2. **Remova acentos**: "inteligência" → "inteligencia"
3. **Use aspas para termos exatos**: "machine learning" → `%22machine+learning%22`
4. **Combine termos**: "AI AND healthcare" → "AI+AND+healthcare"

### 🎯 Personalizações Avançadas

#### 🔄 1. Alterar Termo de Busca (Completo):

```python
# PASSO 1: Linha 94 - Defina o termo
search_term = "blockchain technology"

# PASSO 2: Linha 3 - Atualize a URL correspondente
SEARCH_URL = "https://scholar.google.com.br/scholar?hl=pt-BR&as_sdt=0%2C5&q=blockchain+technology&lr=lang_pt&oq="

# ✅ IMPORTANTE: O termo na URL deve coincidir com search_term (substituindo espaços por +)
```

#### 🌍 2. Configurações de Idioma:

```python
# 🇧🇷 Português Brasileiro (padrão)
SEARCH_URL = "https://scholar.google.com.br/scholar?hl=pt-BR&as_sdt=0%2C5&q=inteligencia+artificial&lr=lang_pt&oq="

# 🇺🇸 Inglês
SEARCH_URL = "https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=artificial+intelligence&lr=lang_en&oq="

# 🇪🇸 Espanhol
SEARCH_URL = "https://scholar.google.es/scholar?hl=es&as_sdt=0%2C5&q=inteligencia+artificial&lr=lang_es&oq="

# 🇫🇷 Francês
SEARCH_URL = "https://scholar.google.fr/scholar?hl=fr&as_sdt=0%2C5&q=intelligence+artificielle&lr=lang_fr&oq="
```

#### 🚀 3. Configurações de Performance:

```python
# Linha ~98: Configurações do navegador
browser = await p.chromium.launch(
    headless=False,        # True = sem interface | False = com interface
    slow_mo=1000,         # Velocidade (ms): 0=rápido, 2000=devagar
    args=[
        '--disable-blink-features=AutomationControlled',  # Anti-detecção
        '--disable-web-security',                          # Para alguns sites
        '--no-sandbox'                                     # Para Linux/Docker
    ]
)
```

#### 📂 4. Configurações de Arquivos:

```python
# Diferentes formatos de saída
OUTPUT_FILE = "dados/scholar_resultados.json"           # JSON (padrão)
OUTPUT_FILE = "resultados/busca_2024.json"             # Com data
OUTPUT_FILE = f"dados/scholar_{search_term}.json"      # Com termo de busca

# Organizando por data
from datetime import datetime
data_hoje = datetime.now().strftime("%Y%m%d_%H%M")
OUTPUT_FILE = f"resultados/scholar_{data_hoje}.json"
```

#### ⚙️ 5. Configurações de Coleta:

```python
# Linha 5: Limite de páginas
MAX_PAGES = 10    # Para testes rápidos
MAX_PAGES = 25    # Para buscas médias
MAX_PAGES = 50    # Para buscas completas (padrão)
MAX_PAGES = 100   # Para pesquisas extensas (cuidado com bloqueios!)

# Linha ~133: Timeout entre páginas (mais devagar = mais seguro)
await page.wait_for_timeout(3000)   # 3 segundos (padrão)
await page.wait_for_timeout(5000)   # 5 segundos (mais seguro)
await page.wait_for_timeout(1000)   # 1 segundo (mais rápido)
```

#### 🎯 6. Filtros Avançados na URL:

```python
# Filtro por período de tempo
SEARCH_URL = "https://scholar.google.com.br/scholar?hl=pt-BR&as_sdt=0%2C5&q=machine+learning&as_ylo=2020&as_yhi=2024&lr=lang_pt&oq="

# Filtro por autor específico
SEARCH_URL = "https://scholar.google.com.br/scholar?hl=pt-BR&as_sdt=0%2C5&q=machine+learning&as_sauthors=Silva&lr=lang_pt&oq="

# Busca apenas em títulos
SEARCH_URL = "https://scholar.google.com.br/scholar?hl=pt-BR&as_sdt=1%2C5&q=allintitle%3A+machine+learning&lr=lang_pt&oq="

# Excluir citações (apenas artigos originais)
SEARCH_URL = "https://scholar.google.com.br/scholar?hl=pt-BR&as_sdt=0%2C5&q=machine+learning&as_vis=1&lr=lang_pt&oq="
```

#### 🔧 7. Exemplo de Configuração Completa:

```python
# Configuração otimizada para pesquisa em IA
SEARCH_URL = "https://scholar.google.com.br/scholar?hl=pt-BR&as_sdt=0%2C5&q=inteligencia+artificial&as_ylo=2020&lr=lang_pt&oq="
OUTPUT_FILE = f"resultados/ia_brasil_{datetime.now().strftime('%Y%m%d')}.json"
MAX_PAGES = 30
search_term = "inteligência artificial"

# No navegador (linha ~98):
browser = await p.chromium.launch(
    headless=True,     # Executar em background
    slow_mo=2000       # Mais devagar para evitar bloqueios
)
```

## ⚡ Guia Rápido de Uso

### 🏃‍♂️ Para Iniciantes (5 minutos):

1. **Instale as dependências:**
   ```bash
   pip install playwright
   playwright install chromium
   ```

2. **Execute com configuração padrão:**
   ```bash
   python busca_scholar.py
   ```
   - Busca: "prompt engineering"
   - Páginas: até 50
   - Idioma: Português
   - Arquivo: `Automação/Busca_Acad_mica.json`

### 🎯 Para Usuários Intermediários:

1. **Abra `busca_scholar.py`**
2. **Altere apenas estas 2 linhas:**
   ```python
   # Linha 94: Seu termo de busca
   search_term = "inteligência artificial"
   
   # Linha 3: URL correspondente (substitua espaços por +, remova acentos)
   SEARCH_URL = "https://scholar.google.com.br/scholar?hl=pt-BR&as_sdt=0%2C5&q=inteligencia+artificial&lr=lang_pt&oq="
   ```
3. **Execute:** `python busca_scholar.py`

### 🚀 Para Usuários Avançados:

```python
# Configuração personalizada completa
from datetime import datetime

# Parâmetros principais
search_term = "blockchain healthcare"
SEARCH_URL = "https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=blockchain+healthcare&as_ylo=2020&lr=lang_en&oq="
OUTPUT_FILE = f"dados/blockchain_health_{datetime.now().strftime('%Y%m%d')}.json"
MAX_PAGES = 20

# Performance otimizada
browser = await p.chromium.launch(headless=True, slow_mo=1500)
await page.wait_for_timeout(4000)  # 4 segundos entre páginas
```

### 📋 Checklist Antes de Executar:

- [ ] ✅ Python 3.7+ instalado
- [ ] ✅ Playwright instalado (`pip install playwright`)
- [ ] ✅ Chromium instalado (`playwright install chromium`)
- [ ] ✅ Termo de busca definido na linha 94
- [ ] ✅ URL atualizada na linha 3 (sem acentos, espaços = +)
- [ ] ✅ Pasta de saída criada (se necessário)
- [ ] ✅ Internet funcionando

### ⏱️ Tempos Estimados:

| Páginas | Tempo Aproximado | Artigos (estimativa) |
|---------|------------------|---------------------|
| 5 páginas | 2-3 minutos | ~50 artigos |
| 10 páginas | 5-8 minutos | ~100 artigos |
| 25 páginas | 15-20 minutos | ~250 artigos |
| 50 páginas | 30-40 minutos | ~500 artigos |

> ⚠️ **Cuidado**: Mais de 25 páginas pode ativar CAPTCHA

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

## ❓ Perguntas Frequentes (FAQ)

### 🔧 Instalação e Configuração:

**Q: Erro "playwright not found"**
```bash
# Solução:
pip install playwright
playwright install chromium
```

**Q: Como mudar o termo de busca?**
```python
# 1. Linha 94: Defina o termo
search_term = "seu termo aqui"

# 2. Linha 3: Atualize a URL (substitua espaços por +)
SEARCH_URL = "https://scholar.google.com.br/scholar?hl=pt-BR&as_sdt=0%2C5&q=seu+termo+aqui&lr=lang_pt&oq="
```

**Q: Onde ficam os resultados salvos?**
- Padrão: `Automação/Busca_Acad_mica.json`
- Personalizável na linha 4: `OUTPUT_FILE = "seu_caminho.json"`

### 🚨 Problemas Comuns:

**Q: Apareceu CAPTCHA, e agora?**
- ✅ **Normal**: Aguarde 1-2 horas
- ✅ **Prevenir**: Use menos páginas (MAX_PAGES = 10-25)
- ✅ **Alternativa**: Use VPN ou mude IP

**Q: Script não encontra artigos**
- ✅ Verifique se o termo existe no Scholar
- ✅ Teste URLs diferentes (português/inglês)
- ✅ Remova filtros muito específicos

**Q: Muito lento ou travando**
- ✅ Diminua `slow_mo` (linha ~98): `slow_mo=500`
- ✅ Reduza `MAX_PAGES` (linha 5): `MAX_PAGES = 15`
- ✅ Use `headless=True` (sem interface visual)

### 🎯 Uso e Personalização:

**Q: Como buscar em inglês?**
```python
SEARCH_URL = "https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=artificial+intelligence&lr=lang_en&oq="
search_term = "artificial intelligence"
```

**Q: Como filtrar por ano?**
```python
# Apenas artigos de 2020-2024
SEARCH_URL = "https://scholar.google.com.br/scholar?hl=pt-BR&as_sdt=0%2C5&q=machine+learning&as_ylo=2020&as_yhi=2024&lr=lang_pt&oq="
```

**Q: Posso buscar múltiplos termos?**
- 📝 **Atualmente**: Um termo por execução
- 🔮 **Futuro**: Recurso planejado para próximas versões

**Q: Como exportar para Excel?**
```python
# Adicione depois de salvar o JSON:
import pandas as pd
import json

with open('Automação/Busca_Acad_mica.json', 'r') as f:
    data = json.load(f)
    
df = pd.DataFrame(data)
df.to_excel('resultados.xlsx', index=False)
```

### 🔍 Interpretação dos Dados:

**Q: O que significa cada campo?**
- `title`: Título do artigo
- `authors`: Autores (separados por vírgula)
- `year`: Ano de publicação 
- `journal`: Revista/conferência
- `citations`: Número de citações
- `url`: Link direto para o artigo
- `abstract`: Resumo/snippet

**Q: Por que alguns campos estão vazios (null)?**
- ✅ **Normal**: Nem todos os artigos têm todas as informações
- ✅ **Scholar limita**: Alguns dados não são sempre disponíveis
- ✅ **Estrutura muda**: HTML do Scholar pode variar

### ⚡ Performance e Otimização:

**Q: Como acelerar a coleta?**
```python
# Configuração mais rápida (CUIDADO: maior risco de bloqueio)
browser = await p.chromium.launch(headless=True, slow_mo=500)
await page.wait_for_timeout(1000)  # 1 segundo entre páginas
MAX_PAGES = 15  # Limite menor
```

**Q: Como ser mais "stealth" (passar despercebido)?**
```python
# Configuração mais segura
browser = await p.chromium.launch(headless=True, slow_mo=2500)
await page.wait_for_timeout(5000)  # 5 segundos entre páginas
MAX_PAGES = 10  # Limite bem baixo
```

## 🎯 Próximos Passos

### 🔄 Melhorias Possíveis:

1. **Interface gráfica** com tkinter
2. **Múltiplos termos** de busca simultâneos
3. **Filtros avançados** (ano, autor, revista)
4. **Export para CSV/Excel**
5. **Integração com APIs** de periódicos
6. **Análise bibliométrica** automática
7. **Sistema de agendamento** automático
8. **Dashboard** para visualização de dados

### 🤝 Contribuições:

- 🐛 **Reporte bugs** abrindo issues
- 💡 **Sugira melhorias** via pull requests
- 🔧 **Contribua com código** seguindo boas práticas
- 📚 **Melhore a documentação**

## 🎉 Pronto para Usar!

### 🚀 Comando para Executar:
```bash
python busca_scholar.py
```

### ✨ Em poucos minutos você terá:
- 📊 **Dados estruturados** em formato JSON
- 🔍 **Artigos acadêmicos** com metadados completos  
- 📈 **Informações de citações** para análise bibliométrica
- 🔗 **Links diretos** para cada artigo
- 📝 **Abstracts** para revisão rápida

### 🌟 Aproveite sua pesquisa acadêmica automatizada!

---

### 📜 Licença e Disclaimer

**📚 Uso Educacional**: Este script é destinado para fins educacionais e de pesquisa acadêmica.

**⚖️ Responsabilidade**: Respeite os termos de uso do Google Scholar e use com moderação.

**🤝 Contribuições**: Melhorias e sugestões são sempre bem-vindas!

---

<div align="center">

**📧 Dúvidas?** Consulte o [FAQ](#-perguntas-frequentes-faq) ou abra uma issue!

**⭐ Gostou?** Dê uma estrela no projeto!

**🔧 Quer contribuir?** Pull requests são bem-vindos!

</div>

