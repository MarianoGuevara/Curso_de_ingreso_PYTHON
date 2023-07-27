import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random


'''
nombre:
apellido:
---
Ejercicio: instrucion_if_10
---
Enunciado:
Al presionar el botón  'Calcular', se deberá calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
    6, 7, 8, 9 y 10 ---> Promoción directa, la nota es ...
    4 y 5           ---> Aprobado, la nota es ...
    1, 2 y 3        ---> Desaprobado, la nota es ...

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def alertar_mensaje(self, mensaje, nota):
        alert('', f'La nota {nota} está: {mensaje}')


    def generar_num_aleatorio(self):
        return random.randint(1, 10)


    def verificar_reprobado(self, nota):
        if nota < 4:
            self.alertar_mensaje('REPROBADA', nota)


    def verificar_aprobado(self, nota):
        if nota > 3 and nota < 6:
            self.alertar_mensaje('APROBADA', nota)


    def verificar_promocion(self, nota):
        if nota > 5:
            self.alertar_mensaje('PROMOCIONADA', nota)


    def verificar_nota(self, nota):
        self.verificar_reprobado(nota)
        self.verificar_aprobado(nota)
        self.verificar_promocion(nota)


    def btn_mostrar_on_click(self):
        # numero_nota = self.generar_num_aleatorio()
        # self.verificar_nota(numero_nota)
        edad = int(prompt('', 'edad: '))
        print(not(edad > 12 and edad < 18))
        # if not(edad > 12 and edad < 18):
        #     print("NO ES adolescente")


if __name__ == "__main__":
    app = App()
    app.mainloop()