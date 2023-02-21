import random
import string
import os

users = ['Danie Molina', 'Denis Medina', 'Mohammed Ali', 'Juan Retamal', 'Leon Montero', 'Enrique Diaz', 'Julio Alegria', 'Roberto Cariqueo', 'Luis Alvarez', 'Cristian Saavedra']

def create_account(user):
    # Crea una lista con caracteres permitidos
    characters = string.ascii_letters + string.digits
    # Genera una contraseña
    password = ''.join(random.choice(characters) for i in range(8))
    return { 'name': user, 'password': password }

def validate_phone(num):
    phone_ok = False
    if num.isdigit() and len(num) == 8:
        phone_ok = True
    return phone_ok

accounts = []
for user in users:
    accounts.append(create_account(user))
    phone_ok = True
    last_user = accounts[-1]
    while phone_ok:
        print(f'Usuario {last_user["name"]} se asignó la siguiente contraseña: {last_user["password"]}')
        phone = input('Ingrese teléfono de contacto: ')
        if validate_phone(phone):
            last_user['phone'] = phone
            phone_ok = False
        os.system("cls" if os.name == "nt" else "clear")
print(accounts)