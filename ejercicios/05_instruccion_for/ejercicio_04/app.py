from os import system 
system("cls")

import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import itertools
import random

'''
Al presionar el botón Mostrar pedir valores y mostrar 
la cantidad de oportunidades que tenemos para ingresar datos (10 en total)
por prompt hasta que el usuario ingrese el valor 9 (se deberá utilizar 'BREAK').
En caso de que se pidan 10 veces y no se haya ingresado el valor 9, tambien se termina el bucle.
'''


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def parseador_casero(self, string_parametro):
        bandera_entero = False

        if string_parametro != None:
            for dato in string_parametro:
                if (dato == '0' or dato == '1' or dato == '2' or dato == '3' or 
                    dato == '4' or dato == '5' or dato == '6' or 
                    dato == '7' or dato == '8' or dato == '9'):
                    bandera_entero = True
                else:
                    bandera_entero = False
                    break

        if bandera_entero:
            return int(string_parametro)
        else:
            return string_parametro


    def btn_mostrar_on_click(self):
        intentos = 10

        for i in range(intentos):
            mensaje = f'Ingrese un numero (9 para terminar) intentos: {intentos}: '
            dato = prompt('', mensaje)

            while dato.isdigit() == False:
                mensaje = f'NUMERO NO VALIDO. Ingrese un numero (9 para terminar) intentos: {intentos}: '
                dato = prompt('', mensaje)
            dato = int(dato)

            if dato == 9:
                break
            intentos -= 1


    # def btn_mostrar_on_click(self):
    '''
    Al presionar el botón Mostrar pedir valores por prompt 
    hasta que el usuario ingrese el valor 9 (se deberá utilizar 'BREAK').
    '''

    #     # None representa la ausencia de valor

    #     #SOLUCION 1
    #     bucle = itertools.count()
    #     for i in bucle: #-> Es un generador infinito de numeros. De 0 a infinito; de 1 en 1
    #         print(bucle)
    #         dato = prompt('', 'Ingrese algo (9 para parar): ')
    #         dato = self.parseador_casero(dato)

    #         if dato == 9:
    #             break

    #     #SOLUCION 2
    #     for i in itertools.repeat(None): #-> None es el objeto que se iterará; como no hay objeto, va None
    #         dato = prompt('', 'Ingrese algo (9 para parar): ')
    #         dato = self.parseador_casero(dato)

    #         if dato == 9:
    #             break

    #     #SOLUCION 3
    #     for i in iter(int, ''): #-> solucion de gpt, no termino de entender la funcion iter
    #         dato = prompt('', 'Ingrese algo (9 para parar): ')
    #         dato = self.parseador_casero(dato)

    #         if dato == 9:
    #             break



if __name__ == "__main__":
    app = App()
    app.mainloop()