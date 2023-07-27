import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
2.	El departamento de Construcción Rural requiere una herramienta 
que facilite el calculo de materiales necesarios 
a la hora de realizar un alambrado perimetral, se le solicita al usuario
que ingrese el ancho y el largo del terreno.

    A. Informar los metros cuadrados del terreno y los metros lineales del perimetro
    B. Informar la cantidad de postes de quebracho Grueso de 2.4 mts 
    (van cada 250 mts lineales y en las esquinas).
    C. Informar la cantidad de postes de quebracho Fino de 2.2 mts 
    (van cada 12 mts lineales, si en ese lugar no se encuentra el poste grueso).
    D. Informar la cantidad de varillas (van cada 2 mts lineales).
    E. Informar la cantidad de alambre alta resistencia 17/15 considerando 7 hilos. 

    EJ 36 MTS X 24 MTS 
    (G)Poste Quebracho Grueso de 2.4 mts
    (F)Poste Quebracho Fino de 2.2 mts
    (V)Varillas

    G V V V V V F V V V V V F V V V V V G
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    F                                   F
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    G V V V V V F V V V V V F V V V V V G
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Largo")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_largo = customtkinter.CTkEntry(master=self)
        self.txt_largo.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Ancho")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_ancho = customtkinter.CTkEntry(master=self)
        self.txt_ancho.grid(row=1, column=1)

        self.btn_calcular = customtkinter.CTkButton(master=self, text="CALCULAR", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=3, pady=10, columnspan=2, sticky="nsew")


    def leer_txt_box(self, text_box):
        return text_box.get()


    def verificar_float(self, dato):
        try:
            return float(dato)
        except:
            return False


    def leer_y_transformar_a_entero(self, text_box):
        dato = self.leer_txt_box(text_box)
        dato = self.verificar_float(dato)
        return dato


    def btn_calcular_on_click(self):
        '''
        D. Varillas -> no especifica
        E. Cantidad de alambre alta resistencia -> fumaron de la buena
        '''

        largo = self.leer_y_transformar_a_entero(self.txt_largo)
        ancho = self.leer_y_transformar_a_entero(self.txt_ancho)

        if largo == False or ancho == False:
            mensaje = 'Algun dato no es numerico'
        else:
            metros_cuadrados = largo * ancho
            metros_lineales = (largo*2) + (ancho*2)

            quebracho_grueso = metros_lineales // 250
            quebracho_grueso = quebracho_grueso + 4

            quebracho_fino = metros_lineales // 12
            quebracho_fino = quebracho_fino - quebracho_grueso

            varillas = metros_lineales // 2
            varillas = varillas - (quebracho_grueso + quebracho_fino)

            mensaje =\
            '''
            metros cuadrados: {0}
            metros lineales: {1}
            quebracho grueso: {2}
            quebracho fino: {3}
            varillas: {4}
            '''.format(metros_cuadrados, metros_lineales, quebracho_grueso,
                        quebracho_fino, varillas)
        alert('', mensaje)



if __name__ == "__main__":
    app = App()
    app.mainloop()