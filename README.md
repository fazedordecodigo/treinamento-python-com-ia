# Treinamento: Python com IA (4h)

Pipeline completo: Dados -> Transformação -> Automação -> Inferência com modelo pré-treinado.

## Conteúdo dos Blocos

| Bloco | Tema | Foco Principal | Entregável |
|-------|------|----------------|------------|
| 1 | Introdução Python IA | Fundamentos produtivos (tipagem, estrutura, logging) | Função de resumo validada |
| 2 | Manipulação de Dados | SQL + pandas + NumPy (limpeza, métricas) | DataFrame normalizado + métricas |
| 3 | Automação | CLI, logging estruturado, testes | Comando `run_insight` funcional |
| 4 | Modelos Pré-Treinados | Uso de `transformers`, insight textual | Insight salvo em JSON |

## Requisitos

- Python >= 3.11 (ideal 3.13 se disponível)
- CPU suficiente; GPU opcional para modelos maiores
- Acesso à internet (baixar modelo Hugging Face)

## Instalação

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Execução Rápida

```bash
python scripts/run_insight.py --limit 50 --model distilgpt2
cat outputs/insight.json
```

## Estrutura

```
src/
  config.py                # Configurações centralizadas
  data_pipeline/
    ingest.py              # Criação e seed do banco
    transform.py           # Carregamento em pandas
    stats.py               # Cálculo de métricas (NumPy)
  automation/
    cli.py                 # CLI principal
    logging_config.py      # Config de logging
  models_inference/
    inference.py           # Geração de insight via transformers
    evaluation.py          # Heurísticas de avaliação simples
scripts/
  run_insight.py           # Entry point
tests/
  test_stats.py            # Teste unitário exemplo
outputs/                   # Gerado em runtime
```

## Fluxo do Pipeline
1. Inicializa banco + seed (SQLite)
2. Extrai dados para DataFrame
3. Calcula métricas agregadas vetoricamente
4. Gera insight textual usando modelo pré-treinado
5. Salva JSON com metadados + insight

## Ajustando Modelo
Alterar via argumento CLI:
```bash
python scripts/run_insight.py --model distilbert-base-multilingual-cased
```
(Para outras tasks ajuste o código em `inference.py` trocando o tipo de pipeline.)

## Testes

```bash
pytest -q
```

## Extensões Sugeridas
- Adicionar caching de modelo
- Guardar hash do dataset
- Validar repetição de n-gramas (funções em `evaluation.py`)

## Métricas e Qualidade
| Dimensão | Meta |
|----------|------|
| Corretude | Execução sem exceções |
| Clareza | Funções coesas, nomes descritivos |
| Performance | Sem loops Python desnecessários |
| Segurança | Sem segredos hardcoded |
| Reprodutibilidade | Versões registradas no JSON final |

## Licença
MIT
