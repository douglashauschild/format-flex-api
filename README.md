# FormatFlex API

Uma API moderna e flexível para formatação de dados, construída com FastAPI.

## 📦 Funcionalidades

- ✅ Formatar datas
- ✅ Formatar data e hora
- ✅ Formatar apenas hora
- ✅ Formatar CPF
- ✅ Formatar CNPJ
- ✅ Formatar CEP
- ✅ Formatar telefone (móvel e fixo)
- ✅ Transformar texto em MAIÚSCULO
- ✅ Transformar texto em minúsculo

## 🚀 Como rodar o projeto

### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
cd formatflex_api
```

### 2. Criar e ativar ambiente virtual (opcional, mas recomendado)
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Rodar a API
```bash
uvicorn app.main:app --reload
```

# 📖 Acessar a documentação Swagger
Abra no navegador:
- http://127.0.0.1:8000/docs → Swagger UI
- http://127.0.0.1:8000/redoc → ReDoc


# ✅ Como rodar os testes automatizados
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

# 💡 Exemplos de uso
**POST** ```/format/cpf ```

Body:
```bash json
{ "value": "12345678909" }
```
Resposta:
```bash json
{ "formatted": "123.456.789-09" }
```
