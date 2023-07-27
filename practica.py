from os import system 
system("cls")

'''
Hacer contraseña que tenga mayuscula y que contenga minimo 3 numeros
y guardarla en una lista de contraseñas
'''

class Bloques_Constraseñas:
    def __init__(self) -> None:
        self.contraseñas = []
        self.contador_numeros = 0
        self.contador_mayusculas = 0

    def pedir_dato(self, msj):
        return input(msj)

    def contar_numeros(self, password:str):
        self.contador_numeros = 0
        for i in range(len(password)):
            if password[i].isdigit() == True:
                self.contador_numeros += 1

    def contar_mayusculas(self, password:str):
        self.contador_mayusculas = 0
        for i in range(len(password)):
            if password[i].isalpha() == True:
                if password[i] == password[i].upper():
                    self.contador_mayusculas += 1

    def verificar_x_nums_o_mayusc(self, atributo, cant_nums):
        if atributo >= cant_nums:
            return True
        else:
            return False

    def contraseña_final(self, msj, msj2):
        while True:
            print(self.contraseñas)
            while True:
                contra = self.pedir_dato(msj)
                self.contar_numeros(contra)
                self.contar_mayusculas(contra)
                nums = self.verificar_x_nums_o_mayusc(self.contador_numeros, 3)
                mayusc = self.verificar_x_nums_o_mayusc(self.contador_mayusculas, 1)

                if nums == True and mayusc == True:
                    break
            self.contraseñas.append(contra)
            print(self.contraseñas)

            if self.pedir_dato(msj2) == 'no':
                break

contraseñas_bloque_uno = Bloques_Constraseñas()
contraseñas_bloque_uno.contraseña_final('Ingrese contraseña: '\
                                        '(minimo 1 mayusc y 3 numeros): ',
                                        'Desea ingresar otra contraseña a '\
                                        'la lista? (no para cortar): ')