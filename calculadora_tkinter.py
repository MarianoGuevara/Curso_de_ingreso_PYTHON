import tkinter as tk
import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("CALCULADORA")
        self.minsize(200, 200)

        self.nombres = ['1', '2', '+', '3', '4', '-', '5', '6', 'x',
                        '7', '8', '/', '9', '0', '=']

        self.rows = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]

        self.columns = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

        for i in range(len(self.rows)):
            self.btn_numerico = customtkinter.CTkButton(master=self,
                            text=self.nombres[i], command=lambda contenido=self.nombres[i]: self.boton_numerico(contenido))
            self.btn_numerico.grid(row=self.rows[i], 
                                    column=self.columns[i], pady=10, padx=10)

        self.label_title = customtkinter.CTkLabel(master=self, 
                        text="Calculadora", font=("Arial", 15, "bold"))
        self.label_title.grid(row=1, column=1, padx=10, pady=10)

        self.label_title = customtkinter.CTkLabel(master=self, 
                        text="Basica", font=("Arial", 15, "bold"))
        self.label_title.grid(row=1, column=3, padx=10, pady=10)

        # state='disabled'
        self.txt_screen = customtkinter.CTkEntry(master=self)
        self.txt_screen.grid(row=1, column=2, pady=10, padx=10)

    def insertar_en_txt_box(self, txt, dato):
        txt.insert(0, dato)

    def boton_numerico(self, contenido):
        match contenido:
            case '1':
                self.insertar_en_txt_box(self.txt_screen, '1')
            case '2':
                self.insertar_en_txt_box(self.txt_screen, '2')
            case '3':
                pass
            case '4':
                pass
            case '5':
                pass
            case '6':
                pass
            case '7':
                pass
            case '8':
                pass
            case '9':
                pass
            case '0':
                pass

    def boton_dos(self):
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()