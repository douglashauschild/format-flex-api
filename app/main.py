from fastapi import FastAPI
from pydantic import BaseModel
from app import formatters
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="FormatFlex API", description="API para formatação de dados.", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextInput(BaseModel):
    text: str

class FormatInput(BaseModel):
    value: str

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à FormatFlex API"}

@app.post("/format/date")
def format_date(data: FormatInput):
    return {"formatted": formatters.format_date(data.value)}

@app.post("/format/datetime")
def format_datetime(data: FormatInput):
    return {"formatted": formatters.format_datetime(data.value)}

@app.post("/format/time")
def format_time(data: FormatInput):
    return {"formatted": formatters.format_time(data.value)}

@app.post("/format/cpf")
def format_cpf(data: FormatInput):
    return {"formatted": formatters.format_cpf(data.value)}

@app.post("/format/cnpj")
def format_cnpj(data: FormatInput):
    return {"formatted": formatters.format_cnpj(data.value)}

@app.post("/format/cep")
def format_cep(data: FormatInput):
    return {"formatted": formatters.format_cep(data.value)}

@app.post("/format/phone")
def format_phone(data: FormatInput):
    return {"formatted": formatters.format_phone(data.value)}

@app.post("/format/uppercase")
def uppercase(data: TextInput):
    return {"formatted": formatters.uppercase(data.text)}

@app.post("/format/lowercase")
def lowercase(data: TextInput):
    return {"formatted": formatters.lowercase(data.text)}
