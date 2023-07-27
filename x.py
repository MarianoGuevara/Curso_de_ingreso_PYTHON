from os import system 
system("cls")

import tkinter
from tkinter.simpledialog import askstring as prompt

dato = prompt('', 'Numero: ')
try:
    dato = int(dato)
    print(f'El dato ingresado es un numerico entero: ({dato})')
except ValueError:
    try:
        dato = float(dato)
        print(f'El dato ingresado es un flotante: ({dato})')
    except Exception:
        print(f'El dato ingresado es un string o intransformable: ({dato})')
except TypeError:
    print(f'El dato ingresado es un none: ({dato})')
else:
    print('Listo')