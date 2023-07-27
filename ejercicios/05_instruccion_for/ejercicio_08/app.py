import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón Mostrar pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        '''
        En matemáticas, un número primo es un número natural mayor que 1
        que tiene únicamente dos divisores positivos distintos: él mismo y el 1.
        '''
        contador_divisores = 0

        while True:
            dato = prompt("", "Ingresa un numero:")
            try:
                dato = int(dato)
                break
            except Exception:
                alert('', 'Dato no numericoo')

        mensaje = f"El numero '{dato}' "

        for i in range(dato):
            if (dato % (i+1)) == 0:
                contador_divisores += 1

        if contador_divisores == 2:
            mensaje += "es un numero primo"
        else:
            mensaje += "no es un numero primo"

        alert("", mensaje)



if __name__ == "__main__":
    app = App()
    app.mainloop()