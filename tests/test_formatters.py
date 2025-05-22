import pytest
from app import formatters

def test_format_cpf():
    assert formatters.format_cpf("12345678909") == "123.456.789-09"

def test_format_cnpj():
    assert formatters.format_cnpj("12345678000195") == "12.345.678/0001-95"

def test_format_cep():
    assert formatters.format_cep("12345678") == "12345-678"

def test_format_phone_mobile():
    assert formatters.format_phone("11987654321") == "(11) 98765-4321"

def test_format_phone_landline():
    assert formatters.format_phone("1134567890") == "(11) 3456-7890"

def test_uppercase():
    assert formatters.uppercase("abc") == "ABC"

def test_lowercase():
    assert formatters.lowercase("ABC") == "abc"

def test_format_date():
    assert formatters.format_date("2025-05-22") == "22/05/2025"

def test_format_datetime():
    assert formatters.format_datetime("2025-05-22 14:30:00") == "22/05/2025 14:30:00"

def test_format_time():
    assert formatters.format_time("14:30:00") == "14:30"
