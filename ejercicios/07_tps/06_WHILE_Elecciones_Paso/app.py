import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
'''
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")


    def btn_validar_on_click(self):
        bandera_votos = False
        cantidad_cantidatos = 0
        acumulador_edad_cantidatos = 0
        acumulador_votos = 0

        while True:
            nombre = prompt("", "Nombre: ")

            while True:
                edad = prompt('', 'Edad: ')
                try:
                    edad = int(edad)
                    if edad > 24:
                        break
                except Exception:
                    alert('', 'Edad debe ser numero')

            while True:
                votos = prompt('', 'Cantidad de votos recibidos: ')
                try:
                    votos = int(votos)
                    if votos > -1:
                        break
                except Exception:
                    alert('', 'Edad debe ser numero')

            if bandera_votos == False or votos > max_votos:
                max_votos = votos
                nombre_max_votos = nombre
            if bandera_votos == False or votos < min_votos:
                min_votos = votos
                nombre_min_votos = nombre
                edad_min_votos = edad
                bandera_votos = True

            acumulador_edad_cantidatos += edad
            cantidad_cantidatos += 1

            acumulador_votos += votos

            seguir = question('', 'Desea ingresar otro candidato?: ')
            if seguir == False:
                break

        promedio_edades_candidatos = acumulador_edad_cantidatos / cantidad_cantidatos

        mensaje = \
        '''
        -Nombre del candidato con más votos: {0}
        -Candidato con menos votos...
            *Nombre: {1}
            *Edad: {2} años
        -Promedio de edades de los candidatos: {3} años
        -Total de votos emitidos: {4}
        '''.format(nombre_max_votos, nombre_min_votos, edad_min_votos,
                promedio_edades_candidatos, acumulador_votos)

        print(mensaje)



if __name__ == "__main__":
    app = App()
    app.mainloop()