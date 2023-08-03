from os import system 
system("cls")

import warnings
warnings.filterwarnings("ignore", category=UserWarning)

import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
#El profesor OAK de pueblo paleta quiere que construyas un modelo prototipico de 
pokedex con algunos pokemones de prueba.

A) Para ello deberas programar el boton "Cargar Pokedex" para poder cargar 10 pokemones.
Los datos que deberas pedir para los pokemones son:
    * El nombre del pokemon
    * El tipo de su elemento (Agua, Psiquico, Electrico)
    * Poder de ataque (validar que sea mayor a 50 y menor a 200)

B) Al presionar el boton mostrar se deberan listar los pokemones y su posicion en la lista (por terminal) 
y mostrar los informe del punto C.

Del punto C solo debera realizar 3 informes. Para determinar que informe hacer, tenga en cuenta lo siguiente:
    Informe 1- Tome el ultimo numero de su DNI Personal (Ej 4) y realice ese informe (Ej, Realizar informe 4)

    Informe 2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al
    numero 9 (Ej 9-4 = 5). En caso de que su DNI 
    finalice con el numero 0, debera realizar el informe 9.

    Informe 3- Tome la suma de los ultimos dos numeros de su DNI personal, en 
    caso de ser un numero par, tomara el numero par 
    mas chico que su ultimo digito del DNI (en caso de que su ultimo digito sea 2, 
    resolvera el ejercicio 8). En caso contrario, si es impar, 
    tomara el numero impar posterior (en caso de que su ultimo digito sea 9,
    resolvera el ejercicio 1)
    En caso de que el numero sea el mismo obtenido en el informe 2, 
    realizara el siguiente informe en la lista.

    Realiza el informe correspondiente al numero obtenido.

EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 

C) NOMBRE TIPO PODER ATAQUE
    #! 0) - Cantidad de pokemones de tipo Fuego cuyo poder de 
    pelea con un 10% extra supere los 100 puntos.
    #! 1) - Cantidad de pokemones de tipo Electrico cuyo poder de pelea con 
    un 15% menos este entre los 100 y los 150 puntos.
    #! 2) - Nombre y Poder del pokemon de tipo electrico con el poder mas alto.
    #! 3) - Nombre y Poder del pokemon de tipo psiquico con el poder mas bajo.
    #! 4) - Porcentaje de pokemones de tipo agua con mas de 100 puntos de poder 
    (Sobre el total de pokemones ingresados).
    #! 5) - Porcentaje de pokemones de tipo psiquico con poder de pelea 
    inferior o igual a 150 (sobre el total de pokemones ingresados).
    #! 6) - tipo de los pokemones del tipo que mas pokemones posea. 
    #! 7) - tipo de los pokemones del tipo que menos pokemones posea. 
    #! 8) - Listado de todos los pokemones cuyo poder de pelea supere el valor promedio.
    #! 9) - el promedio de poder de todos los pokemones de tipo Electrico.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA - Pokedex")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="Pokedex 🎮", 
                                                font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        self.image = tk.PhotoImage(file='UTN_Ayudantia_Python_Ingreso/Simulacro_mejorado/Logo_UTN_App.png')
        
        self.top_banner = customtkinter.CTkLabel(master = self, image = self.image, text = 'Banner')
        self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, 
                                    columnspan = 2, rowspan = 1, sticky = 'we')

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Pokedex", 
                                            command=self.btn_cargar_pokedex_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_informe_1 = customtkinter.CTkButton(master=self, text="Informe 1", 
                                                command=self.btn_mostrar_informe_1)
        self.btn_informe_1.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_2 = customtkinter.CTkButton(master=self, text="Informe 2",
                                                    command=self.btn_mostrar_informe_2)
        self.btn_informe_2.grid(row=4, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_3 = customtkinter.CTkButton(master=self, text="Informe 3",
                                                    command=self.btn_mostrar_informe_3)
        self.btn_informe_3.grid(row=5, pady=10, columnspan=2, sticky="nsew")

        self.lista_nombre_pokemones = ["Pikachu", "Charizard", "Bulbasaur", 
                                    "Squirtle", "Jigglypuff", "Psyduck", "Eevee", 
                                    "Gengar", "Mewtwo", "Vaporeon"]
        self.lista_poder_pokemones = [80, 150, 70, 90, 60, 100, 75, 120, 180, 95]

        self.lista_tipo_pokemones = ["eléctrico", "fuego", "planta", "agua", 
                                    "normal", "agua", "normal", "fantasma", "psíquico", "agua"]


    def btn_mostrar_informe_1(self):
        '''
        Son listas paralelas, da lo mismo cual recorra, todas deben tener 
        el mismo len
        '''

        # PUNTO 9
        acumulador_poderes_elect = 0
        contador_pokemones_elect = 0
        for i in range(len(self.lista_poder_pokemones)):
            if self.lista_tipo_pokemones[i] == 'eléctrico':
                acumulador_poderes_elect += self.lista_poder_pokemones[i]
                contador_pokemones_elect += 1

        promedio_poder_pokemones_electricos = acumulador_poderes_elect / contador_pokemones_elect


        # PUNTO 8
        acumulador_poderes = 0
        for i in range(len(self.lista_poder_pokemones)):
            acumulador_poderes += self.lista_poder_pokemones[i]

        promedio_poder_pokemones = acumulador_poderes / len(self.lista_poder_pokemones)

        lista_pokes_upper_average = []
        for i in range(len(self.lista_poder_pokemones)):
            if self.lista_poder_pokemones[i] > promedio_poder_pokemones:
                lista_pokes_upper_average.append(self.lista_nombre_pokemones[i])


        # PUNTO 7
        tipos_pokemones_sin_repetidos = []
        flag_tipo_menos_repetido = True

        tipos_pokemones_sin_repetidos = set(self.lista_tipo_pokemones)

        for tipo in tipos_pokemones_sin_repetidos:
            contador_actual = 0
            for i in range(len(self.lista_tipo_pokemones)):
                if self.lista_tipo_pokemones[i] == tipo:
                    contador_actual += 1

            if flag_tipo_menos_repetido == True or contador_actual < tipo_menos_repetido_int:
                tipo_menos_repetido_int = contador_actual
                tipo_menos_repetido = self.lista_tipo_pokemones[i]


        # PUNTO 6
        tipos_pokemones_sin_repetidos = []
        flag_tipo_mas_repetido = True

        tipos_pokemones_sin_repetidos = set(self.lista_tipo_pokemones)

        for tipo in tipos_pokemones_sin_repetidos:
            contador_actual = 0
            for i in range(len(self.lista_tipo_pokemones)):
                if self.lista_tipo_pokemones[i] == tipo:
                    contador_actual += 1

            if flag_tipo_mas_repetido == True or contador_actual > tipo_mas_repetido_int:
                tipo_mas_repetido_int = contador_actual
                tipo_mas_repetido = self.lista_tipo_pokemones[i]


        # PUNTO 5
        pokemones_totales = len(self.lista_tipo_pokemones)
        pokes_psico_menos_num = 0

        for i in range(len(self.lista_nombre_pokemones)):
            if self.lista_tipo_pokemones[i] == 'psíquico' and self.lista_poder_pokemones[i] < 151:
                pokes_psico_menos_num += 1

        porcentaje_psico_menos_num = pokes_psico_menos_num * 100 / pokemones_totales


        # PUNTO 4
        pokemones_totales = len(self.lista_tipo_pokemones)
        pokes_agua_mas_cien = 0

        for i in range(len(self.lista_nombre_pokemones)):
            if self.lista_tipo_pokemones[i] == 'agua' and self.lista_poder_pokemones[i] > 99:
                pokes_agua_mas_cien += 1

        porcentaje_agua_mas_cien = pokes_agua_mas_cien * 100 / pokemones_totales


        # PUNTO 3
        flag_pokemon_psico = True
        for i in range(len(self.lista_tipo_pokemones)):
            if flag_pokemon_psico == True or self.lista_poder_pokemones[i] < poke_psico_mas_debil:
                flag_pokemon_psico = False
                poke_psico_mas_debil = self.lista_poder_pokemones[i]


        # PUNTO 2
        flag_pokemon_elect = True
        for i in range(len(self.lista_tipo_pokemones)):
            if flag_pokemon_elect == True or self.lista_poder_pokemones[i] > poke_elect_mas_fuerte:
                flag_pokemon_elect = False
                poke_elect_mas_fuerte = self.lista_poder_pokemones[i]


        # PUNTO 1
        pokemones_elect_en_rango = 0
        for i in range(len(self.lista_tipo_pokemones)):
            if self.lista_tipo_pokemones[i] == 'eléctrico':
                descuento = float(self.lista_poder_pokemones[i]) * 0.15
                poder_disminuido = float(self.lista_poder_pokemones[i]) - descuento

                if poder_disminuido > 99 and poder_disminuido < 151:
                    pokemones_elect_en_rango += 1


        # PUNTO 0
        pokemones_fuego_mayor_cien = 0
        for i in range(len(self.lista_tipo_pokemones)):
            if self.lista_tipo_pokemones[i] == 'fuego':
                aumento = float(self.lista_poder_pokemones[i]) * 0.10
                poder_aumentado = float(self.lista_poder_pokemones[i]) + aumento

                if poder_aumentado > 100:
                    pokemones_fuego_mayor_cien += 1


        mensaje = \
        '''
        -Cantidad de pokemones de tipo Fuego cuyo poder de 
        pelea con un '10%' extra supere los 100 puntos: {0}

        -Cantidad de pokemones de tipo Electrico cuyo poder de pelea con 
        un 15% menos este entre los 100 y los 150 puntos: {1}

        -Nombre y Poder del pokemon de tipo electrico con el poder mas alto: {2}

        -Nombre y Poder del pokemon de tipo psiquico con el poder mas bajo: {3}

        -Porcentaje de pokemones de tipo agua con mas de 100 puntos de poder: {4:.2f}

        -Porcentaje de pokemones de tipo psiquico con poder de pelea
        inferior o igual a 150 (sobre el total de pokemones ingresados): {5:.2f}

        -Tipo de los pokemones del tipo que mas pokemones posea: {6}

        -Tipo de los pokemones del tipo que menos pokemones posea: {7}

        -Listado de todos los pokemones cuyo poder de pelea supere el valor promedio: {8}

        -El promedio de poder de todos los pokemones de tipo Electrico: {9}
        '''.format(pokemones_fuego_mayor_cien, pokemones_elect_en_rango, poke_elect_mas_fuerte,
                poke_psico_mas_debil, porcentaje_agua_mas_cien, porcentaje_psico_menos_num, 
                tipo_mas_repetido, tipo_menos_repetido,
                lista_pokes_upper_average, promedio_poder_pokemones_electricos)

        alert('', mensaje)

    def btn_mostrar_informe_2(self):
        print(self.lista_nombre_pokemones)
        # self.lista_nombre_pokemones.append('Marian')
        print(self.lista_nombre_pokemones)
        alert("2","2")

    def btn_mostrar_informe_3(self):
        alert("3","3")

    def btn_cargar_pokedex_on_click(self):
        pokemones = 2
        for i in range(pokemones):
            while True:
                nombre_pokemon = prompt('', 'Nombre del pokemon: ')
                if nombre_pokemon.isalpha() == True:
                    break
                else:
                    alert("", "Dato debe ser caracteres")

            while True:
                elemento_pokemon = prompt('', 'Elemento del pokemon (agua, psíquico, eléctrico): ')
                if (elemento_pokemon == 'agua' or elemento_pokemon == 'psíquico' or
                    elemento_pokemon == 'eléctrico'):
                    break
                else:
                    alert("", "Dato debe ser 'agua, psíquico, eléctrico'")

            while True:
                poder_ataque_pokemon = prompt('', 'Poder de ataque del pokemon: ')
                try:
                    poder_ataque_pokemon = int(poder_ataque_pokemon)
                    
                    if poder_ataque_pokemon > 49 or poder_ataque_pokemon < 201:
                        break
                except:
                    alert("", "Dato debe ser numerico")

        self.lista_nombre_pokemones.append(nombre_pokemon)
        self.lista_tipo_pokemones.append(poder_ataque_pokemon)
        self.lista_poder_pokemones.append(poder_ataque_pokemon)


if __name__ == "__main__":
    app = App()
    app.mainloop()