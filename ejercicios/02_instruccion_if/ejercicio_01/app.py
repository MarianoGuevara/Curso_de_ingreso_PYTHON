import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: instrucion_if_01
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener contenido en la caja de texto txt_edad, transformarlo en número, 
si coincide con el valor 18, mostrar el mensaje “Usted tiene 18 años” utilizando el Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def alertar_mensaje(self, mensaje):
        alert('', mensaje)


    def transformar_a_entero(self, entero):
        try:
            return int(entero)
        except ValueError:
            self.alertar_mensaje('No se ingreso un entero')
            return False


    def verificar_condicion_18_años(self, entero):
        if entero != False:
            if entero == 18:
                return True
            else:
                return False
        else:
            return -1


    def imprimir_mensaje_segun_booleano(self, booleano):
        if booleano == True:
            self.alertar_mensaje("Ud. tiene 18 años")
        elif booleano == False:
            self.alertar_mensaje("Ud. NO tiene 18 años")


    def leer_caja_texto(self, caja_texto):
        try:
            return caja_texto.get()
        except Exception:
            self.alertar_mensaje('Caja texto no reconocida u oro error')
            return False


    def btn_mostrar_on_click(self):
        edad = self.leer_caja_texto(self.txt_edad)
        edad = self.transformar_a_entero(edad)

        booleano = self.verificar_condicion_18_años(edad)
        self.imprimir_mensaje_segun_booleano(booleano)


if __name__ == "__main__":
    app = App()
    app.mainloop()