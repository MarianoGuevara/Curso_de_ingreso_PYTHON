import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón 'Mostrar' pedir un número. Mostrar los números pares desde 
el 1 al número ingresado, y mostrar la cantidad de números pares encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        mensaje_pares = ''
        contador_pares = 0

        while True:
            dato = prompt("", "Ingresa un numero:")
            try:
                dato = int(dato)
                break
            except Exception:
                alert('', 'Dato no numericoo')

        for i in range(dato):
            if ((i+1) % 2) == 0:
                contador_pares += 1

                if mensaje_pares == '':
                    mensaje_pares += str(i+1) 
                else:
                    mensaje_pares += ', ' + str(i+1) 

        mensaje_pares = f'CANTIDAD DE PARES: {contador_pares}\n' + mensaje_pares

        alert("", mensaje_pares)


if __name__ == "__main__":
    app = App()
    app.mainloop()