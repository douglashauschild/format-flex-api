from datetime import datetime
import re

def format_date(date_str: str, input_format: str = "%Y-%m-%d", output_format: str = "%d/%m/%Y") -> str:
    return datetime.strptime(date_str, input_format).strftime(output_format)

def format_datetime(datetime_str: str, input_format: str = "%Y-%m-%d %H:%M:%S", output_format: str = "%d/%m/%Y %H:%M:%S") -> str:
    return datetime.strptime(datetime_str, input_format).strftime(output_format)

def format_time(time_str: str, input_format: str = "%H:%M:%S", output_format: str = "%H:%M") -> str:
    return datetime.strptime(time_str, input_format).strftime(output_format)

def format_cpf(cpf: str) -> str:
    cpf = re.sub(r'\D', '', cpf)
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

def format_cnpj(cnpj: str) -> str:
    cnpj = re.sub(r'\D', '', cnpj)
    return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"

def format_cep(cep: str) -> str:
    cep = re.sub(r'\D', '', cep)
    return f"{cep[:5]}-{cep[5:]}"

def format_phone(phone: str) -> str:
    phone = re.sub(r'\D', '', phone)
    if len(phone) == 11:
        return f"({phone[:2]}) {phone[2:7]}-{phone[7:]}"
    elif len(phone) == 10:
        return f"({phone[:2]}) {phone[2:6]}-{phone[6:]}"
    return phone

def uppercase(text: str) -> str:
    return text.upper()

def lowercase(text: str) -> str:
    return text.lower()
