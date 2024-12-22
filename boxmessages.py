from tkinter import messagebox
import re

def show_error(title, message):
    messagebox.showerror(title, message)

def show_warning(title, message):
    return messagebox.askyesno(title, message)

def validate_date(date_str):
    pattern = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$"
    if re.match(pattern, date_str):
        return True
    return False

def validate_fields(client, date, service_value):
    if not client.get():
        show_warning("Atenção", "O campo 'Cliente' está vazio. Deseja prosseguir mesmo assim?")
        return False
    if not date.get():
        show_warning("Atenção", "O campo 'Data' está vazio. Deseja prosseguir mesmo assim?")
        return False
    if not validate_date(date.get()):
        show_error("Erro", "O campo 'Data' não está no formato correto. Use o formato DD/MM/AAAA.")
        return False
    if not service_value.get():
        show_warning("Atenção", "O campo 'Valor Total' está vazio. Deseja prosseguir mesmo assim?")
        return False
    if not validate_money(service_value.get()):
        show_error("Erro", "O campo 'Valor Total' não está no formato correto. Exemplo: R$ 1.000,00")
        return False
    return True

def validate_money(value_if_allowed):
    if re.match(r"^\d+([.,]\d{1,2})?$", value_if_allowed):
        return True
    return False
