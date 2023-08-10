import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
from os import system 
system("cls")

'''
Un gimnasio quiere medir el progreso de sus clientes:

A) Para ello deberas programar el boton "Cargar Clientes" para poder cargar los siguientes datos:
    * Nombre
    * edad (entre 18 y 70 años)
    * Maximo peso levantado en press de banca (No debe ser negativo)
    * Genero (Masculino - Femenino - Otro) 
    En esta opcion se agregaran clientes hasta que el usuario lo desee.

B) Al presionar el boton mostrar se deberan listar todos los datos de los clientes y su posición en la lista (por terminal) 

Del punto C solo debera realizar 3 informes. Para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    Informe 1- Tome el ultimo numero de su DNI Personal (Ej 4) y realice ese informe (Ej, Realizar informe 4)

    Informe 2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). En caso de que su DNI 
    finalice con el numero 0, debera realizar el informe 9.

    Informe 3- Tome la suma de los ultimos dos numeros de su DNI personal, en caso de ser un numero par, tomara el numero par 
    mas chico que su ultimo digito del DNI (en caso de que su ultimo digito sea 2, resolvera el ejercicio 8). En caso contrario, 
    si es impar, tomara el numero impar posterior (en caso de que su ultimo digito sea 9, resolvera el ejercicio 1)
    En caso de que el numero sea el mismo obtenido en el informe 2, realizara el siguiente informe en la lista.
    En caso de que la suma sea 0, realizara el informe 7.

    Realizar los informes correspondientes a los numeros obtenidos. EL RESTO DE LOS INFORMES LOS DEBE IGNORAR. 
C) 
    #! 0) - Nombre y género de la persona de género Masculino u Otro que menos peso levantó en press.
    #! 1) - Nombre y edad de la persona de género Femenino que mas peso levantó en press.
    #! 2) - Cantidad de clientes de género otro que tengan entre 25 y 40 años, que hayan levantado mas de 50 kilos en press.
    #! 3) - Cantidad de personas de género Masculino o Femenino cuya edad supere los 35 años, y que el peso levantado en press
            este entre 25 y 40 kg.
    #! 4) - Género que mas asiste al gimnasio.
    #! 5) - Género que menos asiste al gimnasio.
    #! 6) - Nombre de todos los clientes (cualquier género) cuya edad supere la edad promedio de los Masculinos.
    #! 7) - Nombre de todos los clientes de género Femenino cuya edad este por debajo de la edad promedio de todos los clientes.
    #! 8) - Porcentaje de clientes que levantaron mas de 70 kg en press y cuyo género sea Masculino.  
    #! 9) - Porcentaje de clientes que levantaron entre 40 kg y 50 kg en press y cuyo género no sea Masculino.
'''

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("UTN FRA - Fuerza, bruto")
        self.minsize(320, 200)

        self.label_title = customtkinter.CTkLabel(master=self, text="Fuerza, bruto", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

        self.image = tk.PhotoImage(file='UTN_Ayudantia_Python_Ingreso/TM_2C_2023_GIMNASIO/gym.png')
        
        self.top_banner = customtkinter.CTkLabel(master = self, image = self.image, text = 'Banner')
        self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, columnspan = 2, rowspan = 1, sticky = 'we')

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Cliente", command=self.btn_cargar_cliente_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")
        self.btn_mostrar_todos = customtkinter.CTkButton(master=self, text="Mostrar todos", command=self.btn_mostrar_todos_on_click)
        self.btn_mostrar_todos.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_1 = customtkinter.CTkButton(master=self, text="Informe 1", command=self.btn_mostrar_informe_1)
        self.btn_informe_1.grid(row=4, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_2 = customtkinter.CTkButton(master=self, text="Informe 2", command=self.btn_mostrar_informe_2)
        self.btn_informe_2.grid(row=5, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_3 = customtkinter.CTkButton(master=self, text="Informe 3", command=self.btn_mostrar_informe_3)
        self.btn_informe_3.grid(row=6, pady=10, columnspan=2, sticky="nsew")

        self.nombres = ["Juan", "María", "Carlos", "Laura", "Pedro", "Ana", "Luis", "Marta", "Andrés", "Sofía", "Diego", 
                        "Elena", "Hugo", "Clara", "Gabriel"]

        self.edades = [30, 25, 22, 27, 35, 28, 31, 24, 29, 26, 33, 23, 32, 21, 34]

        self.press_banca = [80, 65, 70, 55, 95, 60, 100, 45, 85, 75, 90, 70, 75, 50, 110]

        self.generos = ["Masculino", "Femenino", "Masculino", "Femenino", "Otro", "Femenino", "Masculino", "Femenino", 
                        "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Otro", "Masculino"]        

    def btn_mostrar_todos_on_click(self):
        print("Nombre-Genero-Edad-Peso Press-Indice")
        for i in range (len(self.edades)):
            nombre = self.nombres[i]
            genero = self.generos[i]
            edad = self.edades[i]
            peso_press = self.press_banca[i]
            print(f"{nombre}-{genero}-{edad}-{peso_press}-{i}")

        #PUNTO C

        if len(self.edades) > 0:

            #! 0) - Nombre y género de la persona de género Masculino u Otro que menos peso levantó en press.        
            bandera_primer_press = False
            
            for i in range(len(self.press_banca)):
                genero = self.generos[i]
                peso_press = self.press_banca[i]
                if genero == "Masculino" or genero == "Otro":
                    if bandera_primer_press == False or peso_press < minimo_peso_press:
                        minimo_peso_press = peso_press
                        bandera_primer_press = True
            
            if bandera_primer_press == True:
                print(f"El menor peso levantado por persona de genero masculino/otro es {minimo_peso_press} kg")
                print("La/Las personas de sexo masculino/otro que menos levantaron en press banca son:")
                for i in range(len(self.press_banca)):
                    genero = self.generos[i]
                    peso_press = self.press_banca[i]
                    nombre = self.nombres[i]
                    if (genero == "Masculino" or genero == "Otro") and peso_press == minimo_peso_press:
                        print(f"{nombre}-{genero}")
            else:
                print("No hay ninguna persona de sexo masculino u otro en el sistema")

            #! 1) - Nombre y edad de la persona de género Femenino que mas peso levantó en press.
            bandera_primer_press = False
            
            for i in range(len(self.press_banca)):
                genero = self.generos[i]
                peso_press = self.press_banca[i]
                if genero == "Femenino":
                    if bandera_primer_press == False or peso_press > maximo_peso_press:
                        maximo_peso_press = peso_press
                        bandera_primer_press = True
            
            if bandera_primer_press == True:
                print(f"El mayor peso levantado por persona de genero femenino es {maximo_peso_press} kg")
                print("La/Las personas de sexo femenino que más levantaron en press banca son:")
                for i in range(len(self.press_banca)): #para ver si alguien mas tiene el mismo peso
                    genero = self.generos[i]
                    peso_press = self.press_banca[i]
                    edad = self.edades[i]
                    nombre = self.nombres[i]
                    if genero == "Femenino" and peso_press == maximo_peso_press:
                        print(f"{nombre}-{edad}")
            else:
                print("No hay ninguna persona de sexo femenino en el sistema")


            #! 2) - Cantidad de clientes de género otro que tengan entre 25 y 40 años, que hayan levantado
            #  mas de 50 kilos en press.
            contador_otro_25_a_40 = 0

            for i in range(len(self.generos)):
                genero = self.generos[i]
                edad = self.edades[i]
                peso_press = self.press_banca[i]

                if genero == "Otro" and (edad >= 25 and edad <= 40) and peso_press > 50:
                    contador_otro_25_a_40 += 1
                
            print(f"La cantidad de clientes de género otro que tengan entre 25 y 40 años y que hayan levantado mas de 50 kilos en press es de: {contador_otro_25_a_40} clientes")

            #! 3) - Cantidad de personas de género Masculino o Femenino cuya edad supere los 35 años, y que el peso levantado en press este entre 25 y 40 kg.
            contador_masc_fem_25_40 = 0

            for i in range(len(self.generos)):
                genero = self.generos[i]
                edad = self.edades[i]
                peso_press = self.press_banca[i]

                if (genero == "Masculino" or genero == "Femenino") and (peso_press >= 25 and peso_press <= 40) and edad > 35:
                    contador_masc_fem_25_40+=1
                
            print(f"La cantidad de personas de género Masculino o Femenino cuya edad supere los 35 años, y que el peso levantado en press este entre 25 y 40 kg es de: {contador_masc_fem_25_40} clientes")

            #! 4) - Género que mas asiste al gimnasio.
            contador_femenino = 0
            contador_masculino = 0
            contador_otro = 0

            for genero in self.generos:
                match genero:
                    case "Masculino":
                        contador_masculino+=1
                    case "Femenino":
                        contador_femenino+=1
                    case other:
                        contador_otro+=1

            if contador_femenino > contador_masculino and contador_femenino > contador_otro:
                print("El genero que más asiste al gimnasio es el femenino")
            elif contador_masculino > contador_otro and contador_masculino > contador_femenino:
                print("El genero que más asiste al gimnasio es el masculino")
            else:
                print("El genero que más asiste es otro")

            #! 5) - Género que menos asiste al gimnasio.
            contador_femenino = 0
            contador_masculino = 0
            contador_otro = 0

            for genero in self.generos:
                match genero:
                    case "Masculino":
                        contador_masculino+=1
                    case "Femenino":
                        contador_femenino+=1
                    case other:
                        contador_otro+=1

            if contador_masculino < contador_femenino and contador_otro < contador_femenino:
                print("El genero que menos asiste al gimnasio es el femenino")
            elif contador_otro < contador_masculino and contador_femenino < contador_masculino:
                print("El genero que menos asiste al gimnasio es el masculino")
            else:
                print("El genero que menos asiste es otro")

            #! 6) - Nombre de todos los clientes (cualquier género) cuya edad supere la edad promedio de los Masculinos. -> En este ejercicio puede existir la ambiguedad de que si no hay ningun masculino el promedio no existe ya que no se puede dividir por cero por ende ¿Se muestran todos los clientes o no se muestra ninguno?
            acumulador_edad_masculino = 0
            contador_masculino = 0

            for i in range(len(self.generos)):
                genero = self.generos[i]
                edad = self.edades[i]

                if genero == "Masculino":
                    acumulador_edad_masculino += edad
                    contador_masculino += 1

            if contador_masculino > 0:
                promedio_edad_masculino = acumulador_edad_masculino / contador_masculino

                print(f"Promedio de edad {promedio_edad_masculino} años")
                print(f"Nombres de las personas que superan la edad promedio de los masculinos")
                for i in range(len(self.edades)):
                    edad = self.edades[i]
                    nombre = self.nombres[i]

                    if promedio_edad_masculino == edad:
                        print(f"{nombre}")
            else:
                print("No se pudo calcular el promedio porque no hay masculinos en el sistema por lo que no se puede mostrar ningun cliente")


            #! 7) - Nombre de todos los clientes de género Femenino cuya edad este por debajo de la edad promedio de todos los clientes
            acumulador_edades = 0
            contador = 0 #Se puede usar el len también directamente
            bandera_femenino = False #Totalmente opcional (no vamos a evaluar tan critico pero si alguno la usa es un plus), sólo la vamos a usar para mejorar la interacción con el usuario así que no hace falta evaluar

            for edad in self.edades:
                acumulador_edades+=edad
                contador+=1 #Puede usar el len también directamente

            promedio_edad = acumulador_edades / contador

            print(f"Promedio de edad de todos los clientes {promedio_edad} años")
            print(f"Nombres de las personas de genero femenino que no superan la edad promedio de todos los clientes")
            for i in range(len(self.edades)):
                edad = self.edades[i]
                genero = self.generos[i]

                if genero == "Femenino":
                    print(f"{nombre}")
                    bandera_femenino = True

            if bandera_femenino == False:
                print("No hay personas de genero femenino en el sistema.")

            #! 8) - Porcentaje de clientes que levantaron mas de 70 kg en press y cuyo género sea Masculino. -> ¿Hablamos del porcentaje sobre los masculinos o sobre el total? (¿divido sobre contador general o el porcentaje está condicionado?)
            
            contador_masculino_peso_pesado = 0
            contador = 0 #Se puede usar el len también directamente

            for i in range(len(self.press_banca)):
                peso_press = self.press_banca[i]
                genero = self.generos[i]

                if genero == "Masculino" and peso_press > 70:
                    contador_masculino_peso_pesado+=1
                contador += 1 #Se puede usar el len también directamente

            porcentaje_masculino_peso_pesado = contador_masculino_peso_pesado * 100 / contador
            
            print(f"El porcentaje de clientes que levantaron mas de 70 kg en press y cuyo género sea Masculino es de:{porcentaje_masculino_peso_pesado}%")

            #! 9) - Porcentaje de clientes que levantaron entre 40 kg y 50 kg en press y cuyo género no sea Masculino -> ¿Hablamos del porcentaje sobre los no masculinos o sobre el total? (¿divido sobre contador general o el porcentaje está condicionado?)

            contador_no_masculino_40_50 = 0
            contador = 0 #Se puede usar el len también directamente

            for i in range(len(self.press_banca)):
                peso_press = self.press_banca[i]
                genero = self.generos[i]

                if genero !="Masculino" and (peso_press >= 40 and peso_press <= 50):
                    contador_no_masculino_40_50+=1
                contador+=1 #Se puede usar el len también directamente

            porcenaje_no_masculino_40_50 = contador_no_masculino_40_50 * 100 / contador
            
            print(f"El porcentaje de clientes que levantaron mas de 70 kg en press y cuyo género no sea Masculino es de:{porcenaje_no_masculino_40_50}%")
        else:
            print("Las listas están vacias por ende no se puede realizar ningun filtro")

    def btn_mostrar_informe_1(self):
        pass

    def btn_mostrar_informe_2(self):
        pass

    def btn_mostrar_informe_3(self):
        pass

    def btn_cargar_cliente_on_click(self):
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()