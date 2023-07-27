import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def alertar_dato(self, msj):
        alert('', msj)


    def pedir_dato_prompt(self, msj):
        dato = prompt("", msj)
        return dato


    def parsear_dato(self, dato):
        try:
            return int(dato)
        except:
            return False


    def btn_comenzar_ingreso_on_click(self):
        mensaje = ""
        acumulador_negativos = 0
        acumulador_positivos = 0
        contador_negativos = 0
        contador_positivos = 0
        contador_ceros = 0
        loop = True

        while loop:
            dato_usuario = self.pedir_dato_prompt('Ingrese un dato: ')

            if dato_usuario == None:
                loop = False
            else:
                dato_usuario = self.parsear_dato(dato_usuario)

                if dato_usuario == False :
                    alert('', 'Ingrese un valor numerico valido')
                else:
                    if dato_usuario < 0:
                        acumulador_negativos += dato_usuario
                        contador_negativos += 1
                    else:
                        contador_positivos += 1
                        acumulador_positivos += dato_usuario
                        if dato_usuario == 0:
                            contador_ceros += 1

                    diferencia = acumulador_positivos - acumulador_positivos

        mensaje =\
        '''
        suma acumulada de los negativos: {0}
        suma acumulada de los positivos: {1}
        Cantidad de números positivos: {2}
        Cantidad de números negativos: {3}
        Cantidad de ceros: {4}
        Diferencia entre números positivos y negativos: {5}
        '''.format(acumulador_negativos, acumulador_positivos,
                contador_positivos, contador_negativos,
                contador_ceros, diferencia)

        if mensaje != "":
            self.alertar_dato(mensaje)

if __name__ == "__main__":
    app = App()
    app.mainloop()
