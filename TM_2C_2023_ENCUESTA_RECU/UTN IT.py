import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
UTN Tecnologies, una reconocida software factory 
se encuentra en la busqueda de ideas para su proximo desarrollo en python, 
que promete revolucionar el mercado. 

Las posibles aplicaciones son las siguientes: 
# Inteligencia artificial (IA),
# Realidad virtual/aumentada (RV/RA), 
# Internet de las cosas (IOT) o 
# Procesamiento de lenguaje natural (NLP).

Para ello, realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas:

A) Programar el boton "Cargar empleado" para poder ingresar los siguientes datos:
    * nombre del empleado
    * edad (no menor a 18)
    * genero (Masculino - Femenino - Otro)
    * tecnologia (IA, RV/RA, IOT, NLP)   

En esta opción, se ingresaran empleados hasta que el usuario lo desee.

B) Al presionar el boton mostrar se deberan listar todos 
los datos de los empleados y su posición en la lista (por terminal) 

Del punto C solo debera realizar 3 informes. Para determinar que informe hacer, tenga en cuenta lo siguiente:
    46499481
    44970498    

    Informe 1- Tome el ultimo numero de su DNI Personal y restele 
    el primer numero. Debera realizar ese informe. 
    En caso de que la resta de negativa, tome el valor positivo de esa resta. 
    
    Informe 2- Tome el ultimo numero de su DNI Personal y restarselo 
    al numero 9. En caso de que la resta de 9, realizara 
    el informe 7. En caso de que la resta de 8, realizara el informe 6. 
    En caso de que la resta de 3, realizara el informa 4.

    Informe 3- Si su DNI personal termina en un numero par, realizará el informe 9. 
    En caso contrario realizar el informe 8.

    Realizar los informes correspondientes a los numeros obtenidos. EL RESTO DE LOS INFORMES LOS DEBE IGNORAR. 
C) 
    0) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
    #!X 1) - Cantidad de empleados de género masculino u otro que votaron por NLP, cuya edad no supere los 35 años.
    #!X 2) - Tecnología que mas se votó.
    #!X 3) - Género que predomina en la empresa.
    #!X 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.  
    #!X 5) - Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre 
    #        entre los 33 y 40.
    #!X 6) - Nombre y género de los empleados que votaron por RV/RA con menor edad.
    #!X 7) - Nombre y tecnología que votó, de los empleados de género masculino con mayor edad.
    #!X 8) - Nombre y edad de los empleados que votaron IA o IOT, cuya edad supere la edad promedio de los que votaron por 
    #        esas tecnologias.
    #!X 9) - Nombre y edad de los empelados de género otro que votaron por NLP, cuya edad este por debajo de la edad promedio 
    #        de ese género.
'''
class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN IT - ENCUESTA")
        self.minsize(320, 200)

        self.label_title = customtkinter.CTkLabel(master=self, text="UTN IT - ENCUESTA", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar encuesta", command=self.btn_cargar_encuesta_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")
        self.btn_mostrar_todos = customtkinter.CTkButton(master=self, text="Mostrar todos", command=self.btn_mostrar_todos_on_click)
        self.btn_mostrar_todos.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_1 = customtkinter.CTkButton(master=self, text="Informe 1", command=self.btn_mostrar_informe_1)
        self.btn_informe_1.grid(row=4, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_2 = customtkinter.CTkButton(master=self, text="Informe 2", command=self.btn_mostrar_informe_2)
        self.btn_informe_2.grid(row=5, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_3 = customtkinter.CTkButton(master=self, text="Informe 3", command=self.btn_mostrar_informe_3)
        self.btn_informe_3.grid(row=6, pady=10, columnspan=2, sticky="nsew")

        self.nombres = ["Juan", "María", "Pedro", "Ana", "Luis", "Carla", "Diego", "Laura", "José", "Marta",
                    "Gabriel", "Elena", "Pablo", "Lucía", "Ricardo", "Valeria", "Fernando", "Sofía", "Hugo", "Clara"]

        self.edades = [25, 30, 45, 38, 42, 25, 49, 32, 19, 49,
                    32, 22, 29, 27, 19, 49, 27, 22, 29, 27]
        
        self.generos = ["Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", 
                        "Otro", "Marta", "Masculino", "Otro", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", 
                        "Femenino", "Masculino", "Femenino"]
        
        self.tecnologias = ["IOT", "RV/RA", "NLP", "IA", "NLP", "IOT", "RV/RA", "IOT", "IA", "NLP",
                    "RV/RA", "RV/RA", "IOT", "RV/RA", "IA", "IOT", "NLP", "IOT", "IA", "IA"]    
        
        #PUEDE MODIFICAR LOS DATOS A SU ANTOJO, A EFECTOS DE REALIZAR PRUEBAS
        
    def btn_mostrar_todos_on_click(self):
        '''
        B) Al presionar el boton mostrar se deberan listar todos 
        los datos de los empleados y su posición en la lista (por terminal) 
        '''
        for i in range(len(self.nombres)):
            mensaje = \
            f'''
            nombre -> {self.nombres[i]}
            edad -> {self.edades[i]} años
            genero -> {self.generos[i]}
            tecnologia -> {self.tecnologias[i]}
            posicion en la lista -> {i+1}
            --------------------------------------
            '''
            print(mensaje)

    def btn_mostrar_informe_1(self):
        #1) - Cantidad de empleados de género masculino u otro que votaron por NLP, cuya edad no supere los 35 años.
        hom_otros_nlp_35 = 0

        for i in range(len(self.nombres)):
            if ((self.generos[i] == 'Otro' or self.generos[i] == 'Masculino') and 
                self.edades[i] < 36):
                hom_otros_nlp_35 += 1

        #2) - Tecnología que mas se votó.
        contador_ia = 0
        contador_rvra = 0
        contador_iot = 0
        contador_nlp = 0

        for i in range(len(self.tecnologias)):
            match self.tecnologias[i]:
                case "IA":
                    contador_ia += 1
                case "IOT":
                    contador_iot += 1
                case "NLP":
                    contador_nlp += 1
                case _:
                    contador_rvra += 1

        contador_rvra = 6
        flag = True
        lista_contadores = ['IA', 'IOT', 'NLP', 'RV/RA']
        lista_contadores_tecnologias = [contador_ia, contador_iot, contador_nlp, contador_rvra]
        tecno_mas_usada = []

        for i in range(len(lista_contadores)):
            if flag or lista_contadores_tecnologias[i] > mayor_tecno:
                flag = False
                mayor_tecno = lista_contadores_tecnologias[i]
                tecno_mas_usada = [lista_contadores[i]]
            elif lista_contadores_tecnologias[i] == mayor_tecno:
                tecno_mas_usada.append(lista_contadores[i])

        # 5) - Porcentaje de empleados que no votaron por IA, 
        # siempre y cuando su género no sea Femenino o su edad se encuentre 
        # entre los 33 y 40. (YO SOBRE EL TOTAL. DSPS LOS PIBES, SOBRE LO Q DEFIENDAN)

        fem_no_ia = 0

        for i in range(len(self.nombres)):
            if ((self.edades[i] > 32 and self.edades[i] < 41) and self.generos[i] != 'Femenino'
                and self.tecnologias[i] != 'IA'):
                fem_no_ia += 1

        if len(self.generos) != 0:
            porcentaje_fem_no_ia = fem_no_ia * 100 / len(self.generos)

        #7) - Nombre y tecnología que votó, de los empleados de género masculino con mayor edad.
        flag_age_m = True

        for i in range(len(self.nombres)):
            if (flag_age_m or self.edades[i] > masc_mas_viejo) and self.generos[i] == 'Masculino':
                flag_age_m = False
                masc_mas_viejo = self.edades[i] 
                name_masc_mas_viejo = self.nombres[i] 

        if not(flag_age_m):
            print(f'name: {masc_mas_viejo} || edad: {name_masc_mas_viejo}')

        for i in range(len(self.nombres)):
            if self.generos[i] == 'Masculino' and self.edades[i] == masc_mas_viejo:
                print(f'name: {self.nombres[i]} || edad: {self.edades[i]}')

        # 9) Nombre y edad de los empelados de género 
        # otro que votaron por NLP, cuya edad este por debajo de la edad promedio 
        acum_edades = 0
        for i in range(len(self.edades)):
            acum_edades += self.edades[i]

        if len(self.edades) != 0:
            edad_promedio = acum_edades * 100 / len(self.edades)

            for i in range(len(self.nombres)):
                if (self.generos[i] != 'Otro' and
                    self.tecnologias[i] == 'NLP' and edad_promedio < edad_promedio):
                    print(f'nombre -> {self.nombres[i]} || edad -> {self.edades[i]}')

    def btn_mostrar_informe_2(self):
        pass

    def btn_mostrar_informe_3(self):
        pass        

    def btn_cargar_encuesta_on_click(self):
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()