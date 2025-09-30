# Banco de Exercícios – Treinamento Python com IA

Organização por bloco e nível (Básico / Intermediário / Sênior). Cada exercício possui Objetivo, Critérios de Aceite e Dicas.

---
## Bloco 1 – Fundamentos & Organização

### 1.1 Básico – Parametrizar caminho de arquivo
- Objetivo: Adaptar função de carregamento para receber `--input <arquivo.csv>`.
- Aceite: Script falha com mensagem clara se arquivo não existe.
- Dica: `Path.exists()`.

### 1.2 Intermediário – Validação de tipos
- Objetivo: Validar que colunas numéricas não possuem strings.
- Aceite: Lança `ValueError` com lista de colunas inválidas.
- Dica: `pandas.to_numeric(..., errors='coerce')` + check nulos.

### 1.3 Sênior – Fallback de encoding
- Objetivo: Tentar UTF-8, fallback para ISO-8859-1 com log de aviso.
- Aceite: Log em nível WARNING quando fallback.
- Dica: Loop sobre lista de encodings.

### 1.4 Sênior Extra – Micro profiling
- Objetivo: Medir tempo de parse e imprimir no log.
- Aceite: Log contém duração em ms.
- Dica: `time.perf_counter()`.

---
## Bloco 2 – Manipulação de Dados

### 2.1 Básico – Receita total e top 3 categorias
- Objetivo: Calcular soma de `preco * quantidade` e top 3 categorias por receita.
- Aceite: Retorna dict com chaves `total_receita` e `top_categorias` (lista).
- Dica: `groupby('categoria')['receita'].sum().nlargest(3)`.

### 2.2 Intermediário – Detecção de outliers (z-score)
- Objetivo: Marcar linhas com z-score de preço > 3.
- Aceite: Nova coluna boolean `is_outlier`.
- Dica: `(serie - media) / std`.

### 2.3 Intermediário – Downcasting numérico
- Objetivo: Reduzir memória de colunas inteiras/float.
- Aceite: Redução >= 20% no uso de memória (exibir antes/depois).
- Dica: `pd.to_numeric(..., downcast='integer')`.

### 2.4 Sênior – Dataclass de métricas
- Objetivo: Função que recebe DataFrame e retorna `StatsResult` com validação.
- Aceite: Tipos corretos + teste unitário.
- Dica: `@dataclass` + asserts.

### 2.5 Sênior – Benchmark apply vs vetorização
- Objetivo: Comparar tempo de loop/apply vs operação vetorizada.
- Aceite: Tabela simples com tempos e fator de melhoria.
- Dica: Use 100k linhas sintéticas.

---
## Bloco 3 – Automação & CLI

### 3.1 Básico – Flag --limit
- Objetivo: Processar apenas N linhas iniciais.
- Aceite: Quando `--limit 10`, DataFrame final tem 10 linhas.
- Dica: `df.head(limit)`.

### 3.2 Intermediário – Logging em arquivo com rotação
- Objetivo: Adicionar handler de rotação 1MB / 3 backups.
- Aceite: Arquivo `logs/app.log` criado e rotaciona.
- Dica: `RotatingFileHandler`.

### 3.3 Intermediário – Código de saída
- Objetivo: CLI retorna código 2 quando falha ingestão.
- Aceite: `sys.exit(2)` em erro específico.
- Dica: Capturar exceção dedicada.

### 3.4 Sênior – Métricas de duração por etapa
- Objetivo: Medir tempo (ms) de ingestão, transform, modelo.
- Aceite: JSON final inclui `timings`.
- Dica: Decorator simples de timing.

### 3.5 Sênior – Cache simples de resultado
- Objetivo: Pular recomputação se hash do dataset igual.
- Aceite: Arquivo cache `cache/<hash>.json` reutilizado.
- Dica: `hashlib.sha256`.

---
## Bloco 4 – Modelos Pré-Treinados

### 4.1 Básico – Trocar task do pipeline
- Objetivo: Usar `pipeline('sentiment-analysis')`.
- Aceite: JSON contém campo `sentiment`.
- Dica: Ajustar prompt/entrada.

### 4.2 Intermediário – Checagem de repetição
- Objetivo: Bloquear insight com repetição n-gram > limite.
- Aceite: Se score > 0.3, gera nova tentativa (máx 2).
- Dica: Função `repetition_score` existente.

### 4.3 Intermediário – Parametrização de sampling
- Objetivo: Adicionar flags `--temperature` e `--top-p`.
- Aceite: Valores refletem no pipeline (logados).
- Dica: Passar kwargs ao `pipeline`.

### 4.4 Sênior – Scoring de insight
- Objetivo: Função que avalia: contém KPI (% ou R$), contém recomendação (palavras chave) e comprimento.
- Aceite: Retorna dict com pontuação composta.
- Dica: Regex + contagem condicional.

### 4.5 Sênior – Execução batch
- Objetivo: Gerar 5 variações em paralelo e escolher melhor score.
- Aceite: Escolha registrada no JSON final com lista de candidatos.
- Dica: ThreadPool + limitar workers.

---
## Exercício Integrador Final

Construir script `run_insight.py` (ou estender) para:
1. Carregar/Gerar dados.
2. Calcular métricas (função pura testada).
3. Gerar insight textual (modelo configurável via CLI).
4. Validar heurísticas (repetição, KPIs).
5. Salvar JSON com métricas, parâmetros, insight, timestamp, hash dataset, timings.

Critérios: Corretude, Clareza, Eficiência, Segurança, Reprodutibilidade, Observabilidade.

---
## Rubrica Resumida
| Dimensão | Indicador | Excelente |
|----------|-----------|-----------|
| Corretude | Execução sem falhas | 0 erros, testes verdes |
| Clareza | Nomeação & modularização | Funções < 30 linhas |
| Eficiência | Uso de vetorização | Zero loops desnecessários |
| Segurança | Sem segredos & validação | Erros tratados com códigos claros |
| Reprodutibilidade | Hash + versões | JSON registra libs + modelo |
| Observabilidade | Logs & timings | Todas etapas com ms registrados |

---
## Dicas Gerais
- Implemente primeiro o caminho feliz simples; depois incremente.
- Salve exemplos de saída para comparação.
- Anote parâmetros de geração para reproduzir insights.
- Revise dependências antes de adicionar novas.

Boa prática: Commits pequenos e descritivos (ex: `feat(cli): adicionar flag --limit`).
