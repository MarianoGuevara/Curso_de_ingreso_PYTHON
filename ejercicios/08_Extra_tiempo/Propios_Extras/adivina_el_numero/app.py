import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random


'''
Adivina el número (v 1.0):
Al comenzar el juego generamos un número secreto del 1 al 100, 
en la pantalla del juego dispondremos de un cuadro de texto 
para ingresar un número y un botón “Verificar”, 
si el número ingresado es el mismo que el número secreto se dará por terminado
el juego con un mensaje similar a este: 

“Ganaste en X intentos”.
de no ser igual se debe informar si 
“falta…”  para llegar al número secreto  o si 
“se pasó…”  del número secreto.
'''

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.txt_numero = customtkinter.CTkEntry(master=self)
        self.txt_numero.grid(row=0, column=1)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar",
                                            command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

        self.numero_secreto = random.randrange(1, 100)
        self.numero_intento = 0


    def alertar_msj(self, msj):
        alert('', msj)


    def obtener_input(self, caja):
        return caja.get()


    def transformar_a_entero(self, dato):
        try:
            return int(dato)
        except:
            return False


    def generar_numero_aleatorio(self, rango_min, rango_max):
        self.numero_secreto = random.randint(rango_min, rango_max)


    def verificar_igualdad_2_nums(self, num1, num2):
        if num1 == False:
            self.alertar_msj('No es numero')
        elif num1 == num2:
            self.alertar_msj(f'Igual!! Ganó en: {self.numero_intento} intentos')
            self.numero_intento = 0
            self.generar_numero_aleatorio(1, 100)
        elif num1 > num2:
            self.alertar_msj('Se pasó...')
        elif num1 < num2:
            self.alertar_msj('Falta...')


    def btn_mostrar_on_click(self):
        print(self.numero_secreto)
        self.numero_intento += 1

        num_ing = self.obtener_input(self.txt_numero)
        num_ing = self.transformar_a_entero(num_ing)

        self.verificar_igualdad_2_nums(num_ing, self.numero_secreto)



if __name__ == "__main__":
    app = App() 
    app.mainloop()