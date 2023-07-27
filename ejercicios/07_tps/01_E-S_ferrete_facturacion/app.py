import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Para el departamento de facturación:
    A.	Ingresar tres precios de productos y mostrar la suma de los mismos.
    B.	Ingresar tres precios de productos y mostrar el promedio de los mismos.
	C.	ingresar tres precios de productos sumarlos y mostrar precio final (más IVA 21%).
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Producto 1")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_importe_1 = customtkinter.CTkEntry(master=self)
        self.txt_importe_1.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Producto 2")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_importe_2 = customtkinter.CTkEntry(master=self)
        self.txt_importe_2.grid(row=1, column=1)

        self.label_3 = customtkinter.CTkLabel(master=self, text="Producto 3")
        self.label_3.grid(row=2, column=0, padx=20, pady=10)
        
        self.txt_importe_3 = customtkinter.CTkEntry(master=self)
        self.txt_importe_3.grid(row=2, column=1)

        self.btn_total = customtkinter.CTkButton(master=self, text="TOTAL", command=self.btn_total_on_click)
        self.btn_total.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_promedio = customtkinter.CTkButton(master=self, text="PROMEDIO", command=self.btn_promedio_on_click)
        self.btn_promedio.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_total_iva = customtkinter.CTkButton(master=self, text="TOTAL c/IVA", command=self.btn_total_iva_on_click)
        self.btn_total_iva.grid(row=5, pady=10, columnspan=2, sticky="nsew")


    def leer_txt_box(self, text_box):
        return text_box.get()


    def verificar_entero(self, dato):
        try:
            return int(dato)
        except:
            return False


    def verificar_tres_parametros(self, param1, param2, param3, igualdad):
        if (param1 == igualdad or param2 == igualdad or param3 == igualdad):
            return False


    def leer_y_transformar_a_entero(self, text_box):
        dato = self.leer_txt_box(text_box)
        dato = self.verificar_entero(dato)
        return dato


    def lectura_de_textboxs(self):
        importe_uno = self.leer_y_transformar_a_entero(self.txt_importe_1)
        importe_dos = self.leer_y_transformar_a_entero(self.txt_importe_2)
        importe_tres = self.leer_y_transformar_a_entero(self.txt_importe_3)

        enteros = self.verificar_tres_parametros(importe_uno, importe_dos, importe_tres)
        return enteros


    def sumar_3_datos(self, dato_uno, dato_dos, dato_tres):
        return dato_uno + dato_dos + dato_tres


    def btn_total_on_click(self):
        importe_uno = self.leer_y_transformar_a_entero(self.txt_importe_1)
        importe_dos = self.leer_y_transformar_a_entero(self.txt_importe_2)
        importe_tres = self.leer_y_transformar_a_entero(self.txt_importe_3)

        enteros = self.verificar_tres_parametros(importe_uno, importe_dos, importe_tres, False)

        if enteros == False:
            mensaje = 'Algun ingreso no es numero entero'
        else:
            importe_total = self.sumar_3_datos(importe_uno, importe_dos, importe_tres) 
            mensaje = f'La suma de los 3 importes es: {importe_total}'

        alert('', mensaje)


    def btn_promedio_on_click(self):
        importe_uno = self.leer_y_transformar_a_entero(self.txt_importe_1)
        importe_dos = self.leer_y_transformar_a_entero(self.txt_importe_2)
        importe_tres = self.leer_y_transformar_a_entero(self.txt_importe_3)

        enteros = self.verificar_tres_parametros(importe_uno, importe_dos, importe_tres, False)

        if enteros == False:
            mensaje = 'Algun ingreso no es numero entero'
        else:
            importe_total = self.sumar_3_datos(importe_uno, importe_dos, importe_tres) 
            mensaje = f'El promedio de los 3 importes es: {importe_total/3}'

        alert('', mensaje)


    def btn_total_iva_on_click(self):
        importe_uno = self.leer_y_transformar_a_entero(self.txt_importe_1)
        importe_dos = self.leer_y_transformar_a_entero(self.txt_importe_2)
        importe_tres = self.leer_y_transformar_a_entero(self.txt_importe_3)

        enteros = self.verificar_tres_parametros(importe_uno, importe_dos, importe_tres, False)

        if enteros == False:
            mensaje = 'Algun ingreso no es numero entero'
        else:
            importe_total = self.sumar_3_datos(importe_uno, importe_dos, importe_tres) 
            iva = (importe_total / 100) * 21
            importe_total_con_iva = importe_total + iva
            mensaje = f'La suma de los 3 importes con iva es: {importe_total_con_iva}'

        alert('', mensaje)



if __name__ == "__main__":
    app = App()
    app.mainloop()