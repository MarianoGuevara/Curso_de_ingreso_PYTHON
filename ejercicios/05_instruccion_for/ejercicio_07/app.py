import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón Mostrar pedir un número. mostrar 
los números divisores desde el 1 al número ingresado, 
y mostrar la cantidad de números divisores encontrados.
'''

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        '''
        Al presionar el botón Mostrar pedir un número. mostrar los números 
        divisores desde el 1 al número ingresado, 
        y mostrar la cantidad de números divisores encontrados.
        '''
        mensaje_divisores = ''
        contador_divisores = 0

        while True:
            dato = prompt("", "Ingresa un numero:")
            try:
                dato = int(dato)
                break
            except Exception:
                alert('', 'Dato no numericoo')

        for i in range(dato):
            if (dato % (i+1)) == 0:
                contador_divisores += 1

                if mensaje_divisores == '':
                    mensaje_divisores += str(i+1) 
                else:
                    mensaje_divisores += ', ' + str(i+1) 

        mensaje_divisores = f'CANTIDAD DE DIVISORES DEL '\
        f'NUMERO "{dato}": {contador_divisores}\n' + mensaje_divisores

        alert("", mensaje_divisores)




if __name__ == "__main__":
    app = App()
    app.mainloop()