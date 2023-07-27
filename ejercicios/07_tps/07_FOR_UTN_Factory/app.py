import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")


    def btn_validar_on_click(self):
        postulantes = 3

        no_binarios_mid_age_ssr = 'No hay no binarios que cumplan'
        nombre_jr_mas_joven = 'No hay juniors'

        cantidad_m = 0
        cantidad_f = 0
        cantidad_nb = 0
        acumulador_edad_m = 0
        acumulador_edad_f = 0
        acumulador_edad_nb = 0

        cantidad_js = 0
        cantidad_net = 0
        cantidad_py = 0

        bandera_junior = False

        for i in range(postulantes):
            nombre = prompt(f"postulante '{i+1}'", 'Nombre: ')

            while True:
                edad = prompt(f"postulante '{i+1}'", 'Edad (+18): ')
                try:
                    edad = int(edad)
                    if edad > 17:
                        break
                except:
                    alert("", "No es numero")

            while True:
                genero = prompt(f"postulante '{i+1}'", 'Genero (F-M-NB): ')
                if genero == 'F' or genero == 'M' or genero == 'NB':
                    break

            while True:
                tecnologia = prompt(f"postulante '{i+1}'", 'tecnologia (PYTHON - JS - ASP.NET): ')
                if tecnologia == 'PYTHON' or tecnologia == 'JS' or tecnologia == 'ASP.NET':
                    break

            while True:
                puesto = prompt(f"postulante '{i+1}'", 'puesto (Jr - Ssr - Sr): ')
                if puesto == 'Jr' or puesto == 'Ssr' or puesto == 'Sr':
                    break

            if (genero == 'NB' and (tecnologia == 'ASP.NET' or tecnologia == 'JS')
                and (edad > 24 and edad < 41) and puesto == 'Ssr'):
                    no_binarios_mid_age_ssr += 1

            if puesto == 'Jr':
                if bandera_junior == False:
                    nombre_jr_mas_joven = nombre
                    edad_jr_mas_joven = edad
                    bandera_junior = True
                else:
                    if edad > edad_jr_mas_joven:
                        nombre_jr_mas_joven = nombre
                        edad_jr_mas_joven = edad

            match genero:
                case 'M':
                    acumulador_edad_m += edad
                    cantidad_m += 1
                case 'F':
                    acumulador_edad_f += edad
                    cantidad_f += 1
                case _:
                    acumulador_edad_nb += edad
                    cantidad_nb += 1

            match tecnologia:
                case 'PYTHON':
                    cantidad_py += 1
                case 'JS':
                    cantidad_js += 1
                case _:
                    cantidad_net += 1


        if cantidad_js == cantidad_net and cantidad_js == cantidad_py:
            tecnologia_mas_usada = 'LAS 3 IGUALES'
        elif cantidad_js > cantidad_net and cantidad_js > cantidad_py:
            tecnologia_mas_usada = 'JAVASCRIPT'
        elif cantidad_py > cantidad_net:
            tecnologia_mas_usada = 'PYTHON'
        else:
            tecnologia_mas_usada = 'ASP.NET'

        if cantidad_m != 0:
            promedio_m = acumulador_edad_f / cantidad_f
        else:
            promedio_m = 'No hay hombres'
        
        if cantidad_f != 0:
            promedio_f = acumulador_edad_m / cantidad_m
        else:
            promedio_f = 'No hay mujeres'
        
        if cantidad_nb != 0:
            promedio_nb = acumulador_edad_nb / cantidad_nb
        else:
            promedio_nb = 'No hay no binarios'

        porcentaje_m = cantidad_m * 100 / postulantes
        porcentaje_f = cantidad_f * 100 / postulantes
        porcentaje_nb = cantidad_nb * 100 / postulantes

        mensaje_final = \
        f'''
            -Cantidad de nb que programan en ASP.NET o JS 
            cuya edad este entre 25 y 40, que se hayan postulado para
            un puesto Ssr: {no_binarios_mid_age_ssr}

            -Nombre del postulante Jr con menor edad: {nombre_jr_mas_joven}

            -Promedio de edades por género: 
                *masculino: {promedio_m:.2f}
                *femenino: {promedio_f:.2f}
                *no binario: {promedio_nb:.2f}

            -Tecnologia con mas postulantes: {tecnologia_mas_usada}

            -Porcentaje de postulantes de cada genero: 
                *masculino: {porcentaje_m:.2f} %
                *femenino: {porcentaje_f:.2f} %
                *no binario: {porcentaje_nb:.2f} % 
        '''

        alert('', mensaje_final)



if __name__ == "__main__":
    app = App()
    app.mainloop()