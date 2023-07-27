import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random
from os import system 
system("cls")

'''
Enunciado:

Una importante empresa dediada a la produccion de alfajores nos solicita una aplicacion que les 
permita controlar la produccion, dicha aplicacion contara con dos botones 

    - ALFAJOR ACEPTADO
    - ALFAJOR DESCARTADO

Mediante los cuales se registrara la cantidad total de alfajores producidos. 

Por tratarse de una produccion artesanal, cada alfajor puede variar su peso, por lo cual es importante
poder registrar el mismo al momento ACEPTARLO o DESCARTARLO. Los pesos deberan ser numeros flotantes 
positivos. 

EL ALFAJOR SERÁ ACEPTADO SI Y SOLO SI SU PESO ES MAYOR A 20 GRAMOS

Al presionar el botón "Generar Informe" se deberá mostrar mediante alert 
la siguiente información:

	A - Cantidad total de alfajores fabricados
	B - Cantidad total de alfajores aceptados
	C - Cantidad total de alfajores rechazados
	D - Peso promedio de los alfajores aceptados
	E - Peso promedio de los alfajores rechazados
    F - Materia prima total utilizada * -> acumulador de peso en gramos
    E - Materia prima total desperdiciada * -> acumulador de peso en gramos 

    *(Tener en cuenta que la cocion produce una merma de 15% del peso)
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.txt_peso_articulo = customtkinter.CTkEntry(master=self, 
                                                placeholder_text="Peso Alfajor")
        self.txt_peso_articulo.grid(row=1, padx=20, pady=20)

        self.btn_aceptar = customtkinter.CTkButton(master=self, text="VERIFICAR", 
                                            command=self.btn_aceptar_o_reject)
        self.btn_aceptar.grid(row=2, pady=10, columnspan=2, sticky="news")

        self.btn_generar_informe_notas = customtkinter.CTkButton(master=self, 
                                                text="Generar Informe de Notas",
                                                command=self.btn_generar_informe_on_click)
        self.btn_generar_informe_notas.grid(row=5, pady=20, columnspan=2, sticky="news")

        self.lista_pesos_rechazados = []
        self.cantidad_aceptados = 0
        self.acum_peso_aceptados = 0
        self.lista_pesos_aceptados = []
        self.cantidad_rechazados = 0
        self.acum_peso_rechazados = 0

        self.alfajores_totales = 0

    def alertar_msj(self, msj):
        alert('', msj)

    def leer_dato(self):
        txt_box = self.txt_peso_articulo.get()
        return txt_box 

    def parseador_flotante(self, dato):
        try:
            return float(dato)
        except Exception:
            return False

    def chequear_peso(self, dato, peso):
        if dato > peso:
            return True
        else:
            return False

    def pedir_alfajor(self, msj_no_num, gramos_minimos):
        dato = self.leer_dato()
        dato = self.parseador_flotante(dato)
        if dato == False:
            self.alertar_msj(msj_no_num)
        else:
            self.alfajores_totales += 1
            booleano = self.chequear_peso(dato, gramos_minimos)
            if booleano == True:
                self.cantidad_aceptados += 1
                self.acum_peso_aceptados += dato
                self.agregar_a_lista(self.lista_pesos_aceptados, dato)
            else:
                self.cantidad_rechazados += 1
                self.acum_peso_rechazados += dato
                self.agregar_a_lista(self.lista_pesos_rechazados, dato)

    def agregar_a_lista(self, lista_alfajores:list, alfajor):
        lista_alfajores.append(alfajor)

    def btn_aceptar_o_reject(self):
        self.pedir_alfajor('El dato ingresado no es flotante. No puede ser ni'\
                    ' aceptado ni rechazado', 20)
        self.txt_peso_articulo.delete(0, tkinter.END)

    def sacar_promedio(self, dividendo, divisor):
        try:
            return dividendo / divisor
        except Exception:
            return 'Imposible realizar el promedio'

    def btn_generar_informe_on_click(self):
        promedio_aceptados = self.sacar_promedio(self.acum_peso_aceptados,
                                                self.cantidad_aceptados)
        promedio_rechazados = self.sacar_promedio(self.acum_peso_rechazados,
                                                self.cantidad_rechazados)
        msj =\
        '''
        - Cantidad total de alfajores fabricados: {0}
        - Cantidad total de alfajores aceptados: {1}
        - Cantidad total de alfajores rechazados: {2}
        - Peso promedio de los alfajores aceptados: {3}
        - Peso promedio de los alfajores rechazados: {4}
        - Materia prima total utilizada: {5}
        - Materia prima total desperdiciada: {6}
        '''.format(self.alfajores_totales, self.cantidad_aceptados, 
            self.cantidad_rechazados, promedio_aceptados, promedio_rechazados,
            self.acum_peso_aceptados, self.acum_peso_rechazados)

        self.alertar_msj(msj)

if __name__ == "__main__":
    app = App()
    app.mainloop()    