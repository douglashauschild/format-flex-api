# format-flex-api

A flexible and extensible API built with Python to handle formatting, parsing, and validation of structured inputs such as CPF, CNPJ, phone numbers, and more.

![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![Last Commit](https://img.shields.io/github/last-commit/douglashauschild/formatflex_api)
![Test Status](https://github.com/douglashauschild/formatflex_api/actions/workflows/test.yml/badge.svg)

## 🚀 Getting Started

### 📦 Requirements

- Python 3.9+
- pip or Poetry (recommended)

### 🛠️ Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/douglashauschild/format-flex-api.git
cd format-flex-api
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
### ▶️ Running the API
Start the server (assuming FastAPI + Uvicorn):
```bash
uvicorn app.main:app --reload
```
The API will be available at: http://localhost:8000
### 🧪 Running Tests
```bash
pytest
```
## 💡 Features
- Format and validate structured inputs (CPF, CNPJ, phone, dates, etc.)
- Modular and easy-to-extend service architecture
- Clear separation between routing, logic, and models
- JSON input/output with FastAPI (or Flask)
## 📁 Project Structure
```bash
format-flex-api/
├── app/
│    ├── main.py
│    ├── formatters.py
├── tests/
│    ├── test_formatters.py
├── requirements.txt
└── README.md
```
## 🧪 Next Steps
- Add OpenAPI documentation
- Improve unit test coverage
- Include authentication middleware
- Package as reusable PyPI module

## 👨🏻‍💻 Author
Douglas Hauschild  
[LinkedIn](https://www.linkedin.com/in/douglas-hauschild-66449122b/) | [GitHub](https://github.com/douglashauschild)

> Feel free to fork and customize this project to build your own Telegram bot!
