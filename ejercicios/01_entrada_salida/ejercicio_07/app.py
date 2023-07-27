import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: entrada_salida_07
---
Enunciado:
Al presionar el botón  que corresponde a cada operación (suma, resta, multiplicación, y división), 
se deberán obtener los valores contenidos en las cajas de texto (txtOperadorA y txtOperadorB), 
transformarlos en números enteros, realizar dicha operación y luego mostrar el resultado 
de la misma utilizando el Dialog Alert. Ej: "El resultado de la …… es: 755"  
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.operacion_actual = 'presione un operador'

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Operador A")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_operador_a = customtkinter.CTkEntry(master=self)
        self.txt_operador_a.grid(row=0, column=1)
        
        self.label2 = customtkinter.CTkLabel(master=self, text="Operador B")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_operador_b = customtkinter.CTkEntry(master=self)
        self.txt_operador_b.grid(row=1, column=1)

        self.btn_sumar = customtkinter.CTkButton(master=self, text="Sumar", command=self.btn_sumar_on_click)
        self.btn_sumar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_restar = customtkinter.CTkButton(master=self, text="Restar", command=self.btn_restar_on_click)
        self.btn_restar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.btn_multiplicar = customtkinter.CTkButton(master=self, text="Multiplicar", command=self.btn_multiplicar_on_click)
        self.btn_multiplicar.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_dividir = customtkinter.CTkButton(master=self, text="Dividir", command=self.btn_dividir_on_click)
        self.btn_dividir.grid(row=5, pady=10, columnspan=2, sticky="nsew")

        self.btn_calcular = customtkinter.CTkButton(master=self, 
                                        text="Calcular", command=self.btn_clickear_boton)
        self.btn_calcular.grid(row=6, pady=10, columnspan=2, sticky="nsew")

        self.label3 = customtkinter.CTkLabel(master=self, text='Presione un operador')
        self.label3.grid(row=7, column=0, padx=20, pady=10)


    def label_nuevo(self, texto):
        self.label3.grid_forget()
        self.label3 = customtkinter.CTkLabel(master=self, text=texto)
        self.label3.grid(row=7, column=0, padx=20, pady=10)


    def obtener_valor_label(self, atributo_clase):
        return atributo_clase.get()


    def transformar_valor_a_entero(self, valor_entero):
        valor_entero = int(valor_entero)
        return valor_entero


    def alertar_mensaje(self, mensaje):
        alert("", mensaje)


    def btn_sumar_on_click(self):
        app.label_nuevo('suma')
        self.operacion_actual = 'sumar'


    def btn_restar_on_click(self):
        app.label_nuevo('resta')
        self.operacion_actual = 'restar'


    def btn_multiplicar_on_click(self):
        app.label_nuevo('multiplicar')
        self.operacion_actual = 'multiplicacion'


    def btn_dividir_on_click(self):
        app.label_nuevo('dividir')
        self.operacion_actual = 'dividir'


    def llamar_a_operador(self, a,b):
        if self.operacion_actual == 'sumar':
            return a + b
        elif self.operacion_actual == 'restar':
            return a - b
        elif self.operacion_actual == 'multiplicacion':
            return a * b
        elif self.operacion_actual == 'dividir':
            return a / b


    def btn_clickear_boton(self):
        try:
            n_uno = app.obtener_valor_label(self.txt_operador_a)
            n_dos = app.obtener_valor_label(self.txt_operador_b)

            n_uno = app.transformar_valor_a_entero(n_uno)
            n_dos = app.transformar_valor_a_entero(n_dos)

            app.llamar_a_operador(n_uno, n_dos)

            app.alertar_mensaje(f'El resultado de la suma entre {n_uno}'\
                f' y {n_dos} es de: {app.llamar_a_operador(n_uno, n_dos)}')
        except Exception:
            app.alertar_mensaje('ERROR')



if __name__ == "__main__":
    app = App()
    app.mainloop()