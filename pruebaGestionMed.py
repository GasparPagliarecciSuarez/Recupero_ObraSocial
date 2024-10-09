import tkinter as tk
from tkinter import messagebox, ttk

class Aplicacion:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)
        self.frame.pack()

        self.entrada_buscar = tk.Entry(self.frame)
        self.entrada_buscar.pack()

        self.boton_buscar = tk.Button(self.frame, text="Buscar", command=self.buscar_medico)
        self.boton_buscar.pack()

        self.tree = ttk.Treeview(self.frame, columns=("codigo", "apellido"), show="headings")
        self.tree.heading("codigo", text="Código")
        self.tree.heading("apellido", text="Apellido")
        self.tree.pack()

        self.medicos = [("001", "Gonzalez"), ("002", "Fernandez"), ("003", "Lopez")]  # Ejemplo de médicos
        self.cargar_medicos()

    def cargar_medicos(self):
        # Cargar todos los médicos en el Treeview
        for medico in self.medicos:
            self.tree.insert('', 'end', values=medico)

    def buscar_medico(self):
        busqueda = self.entrada_buscar.get().strip().lower()  # Eliminar espacios y convertir a minúsculas

        # Si el campo de búsqueda está vacío, restaurar todos los médicos
        if not busqueda:
            self.limpiar_treeview()  # Función que reinicia el Treeview
            self.cargar_medicos()  # Función que carga todos los médicos de la base de datos
            return  # Salimos de la función

        medico_encontrado = False

        # Filtramos la búsqueda
        for item in self.tree.get_children():
            valores = self.tree.item(item, 'values')  # Obtenemos los valores de cada fila
            codigo = valores[0].lower()  # Código del médico en minúsculas
            apellido = valores[1].lower()  # Apellido del médico en minúsculas

            # Verificamos si el texto de búsqueda está en el código o el apellido
            if busqueda in codigo or busqueda in apellido:
                medico_encontrado = True
            else:
                self.tree.detach(item)  # Ocultamos los médicos que no coinciden

        # Si no se encontró ningún médico que coincida, mostramos una advertencia
        if not medico_encontrado:
            messagebox.showwarning("Atención", "No se encontró el médico.")

    def limpiar_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()
