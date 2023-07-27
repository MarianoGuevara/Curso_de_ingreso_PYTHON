from tkinter.simpledialog import askstring as prompt

class ListasNumeros:
    def __init__(self, l1_uno, l1_dos, l1_tres, l2_uno, l2_dos, l2_tres) -> None:
        self.lista_uno = [l1_uno, l1_dos, l1_tres]
        self.lista_dos = [l2_uno, l2_dos, l2_tres]

        self.lista_uno_suma = int(self.unir_parametros(self.lista_uno[0], 
                                                    self.lista_uno[1], self.lista_uno[2]))
        self.lista_dos_suma = int(self.unir_parametros(self.lista_dos[0], 
                                                    self.lista_dos[1], self.lista_dos[2]))

        self.listas_suma = str(self.sumar_parametros(self.lista_uno_suma, self.lista_dos_suma))

        self.listas_suma_lista = []
        self.listas_suma_lista.append(self.listas_suma[0])
        self.listas_suma_lista.append(self.listas_suma[1])
        self.listas_suma_lista.append(self.listas_suma[2])


    def sumar_parametros(self, param1, param2):
        return param1 + param2


    def sumar_caracteristicas(self, lista1, lista2, index):
        return lista1[index] + lista2[index]


    def unir_parametros(self, param1, param2, param3):
        return f"{param1}{param2}{param3}"



def parsear(dato):
    try:
        return int(dato)
    except Exception:
        return False


def pedir_prompt(msj):
    return prompt('', msj)


def pedir_entero_prompt(msj):
    while True:
        dato = pedir_prompt(msj)
        dato = parsear(dato)
        if dato != False:
            break
        print("Dato no numerico")
    return dato


l1_uno = pedir_entero_prompt('Lista 1 posicion 1:')
l1_dos = pedir_entero_prompt('Lista 1 posicion 2:')
l1_tres = pedir_entero_prompt('Lista 1 posicion 3:')

l2_uno = pedir_entero_prompt('Lista 2 posicion 1:')
l2_dos = pedir_entero_prompt('Lista 2 posicion 2:')
l2_tres = pedir_entero_prompt('Lista 2 posicion 3:')

ejercicio = ListasNumeros(l1_uno, l1_dos, l1_tres, l2_uno, l2_dos, l2_tres)

print(ejercicio.lista_uno)
print(ejercicio.lista_dos)
print(ejercicio.listas_suma)
print(ejercicio.listas_suma_lista)