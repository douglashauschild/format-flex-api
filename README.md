# FormatFlex API

Uma API moderna, flexível e leve para formatação de dados, construída com FastAPI.
Perfeita para integrar rapidamente formatações comuns de dados em seus projetos.

![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![Last Commit](https://img.shields.io/github/last-commit/douglashauschild/formatflex_api)
![Test Status](https://github.com/douglashauschild/formatflex_api/actions/workflows/test.yml/badge.svg)


## 📦 Funcionalidades

- Formatação de datas (data, hora, data e hora)
- Formatação de CPF e CNPJ
- Formatação de CEP
- Formatação de telefones (fixo e móvel)
- Conversão de texto para MAIÚSCULO e minúsculo

## 🚀 Como executar localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/douglashauschild/formatflex_api.git
cd formatflex_api
```

### 2. Criar e ativar ambiente virtual (recomendado)
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Executar a API
```bash
uvicorn app.main:app --reload
```

# 📖 Documentação
Após iniciar a aplicação, acesse:
- http://127.0.0.1:8000/docs → Swagger UI
- http://127.0.0.1:8000/redoc → ReDoc


# ✅ Testes automatizados
Execute os testes com:
```bash
pytest
```

# 📁 Estrutura do Projeto
```bash
formatflex_api/
├── app/
│   ├── main.py
│   ├── formatters.py
├── tests/
│   ├── test_formatters.py
├── requirements.txt
├── README.md
```

# 💡 Exemplo de uso
**POST** ```/format/cpf ```

Body:
```bash json
{ "value": "12345678909" }
```
Resposta:
```bash json
{ "formatted": "123.456.789-09" }
```

➡️ Para mais exemplos e detalhes, consulte a demo online:
https://formatflexapi-production.up.railway.app/docs