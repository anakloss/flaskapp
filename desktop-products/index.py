from tkinter import Tk, LabelFrame, Label, Entry, Button, ttk, END, Toplevel,\
    StringVar
import sqlite3


class Product:

    db_name = 'database.db'

    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def get_products(self):
        # Limpiar la tabla
        records = self.tree.get_children()  # Obtiene registros de la tabla
        for element in records:
            self.tree.delete(element)

        # Realiza consulta
        query = 'SELECT * FROM product ORDER BY name DESC'
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tree.insert('', 0, text=row[1], values=row[2])

    def validation(self):
        return len(self.name.get()) != 0 and len(self.price.get()) != 0

    def add_product(self):
        if self.validation():
            query = 'INSERT INTO product VALUES(NULL, ?, ?)'
            param = (self.name.get(), self.price.get())
            self.run_query(query, param)
            self.message['text'] = "El producto {} ha sido agregado satifactoriamente".format(
                self.name.get())

            self.name.delete(0, END)
            self.price.delete(0, END)
        else:
            self.message['text'] = "Nombre y Precio son requeridos"

        self.get_products()

    def delete_product(self):
        self.message['text'] = ''
        try:
            # Busca ID del elemento seleccionado en Treeview
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Por favor seleccione un registro'
            return

        self.message['text'] = ''
        name = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM product WHERE name=?'
        self.run_query(query, (name,))
        self.message['text'] = 'El registro {} ha sido eliminado satisfactoriamente'.format(name)

        self.get_products()

    def edit_product(self):
        self.message['text'] = ''
        try:
            # Busca ID del elemento seleccionado en Treeview
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Por favor seleccione un registro'
            return

        self.message['text'] = ''
        name = self.tree.item(self.tree.selection())['text']
        old_price = self.tree.item(self.tree.selection())['values'][0]

        # -------------- NEW WINDOW --------------
        self.edit_wind = Toplevel()
        self.edit_wind.title("Editar producto")

        # Old name
        Label(self.edit_wind, text='Nombre anterior: ').grid(row=0, column=1)
        Entry(self.edit_wind, textvariable=StringVar(
            self.edit_wind, value=name), state='readonly').grid(row=0, column=2)
        # New name
        Label(self.edit_wind, text='Nombre nuevo: ').grid(row=1, column=1)
        new_name = Entry(self.edit_wind)
        new_name.grid(row=1, column=2)

        # Old pice
        Label(self.edit_wind, text='Precio anterior: ').grid(row=2, column=1)
        Entry(self.edit_wind, textvariable=StringVar(
            self.edit_wind, value=old_price), state='readonly').grid(row=2, column=2)
        # New price
        Label(self.edit_wind, text='Precio nuevo: ').grid(row=3, column=1)
        new_price = Entry(self.edit_wind)
        new_price.grid(row=3, column=2)

        Button(self.edit_wind, text="Actualizar",
            command=lambda: self.edit_records(
                new_name.get(), name, new_price.get(), old_price)).grid(
            row=4, column=2, sticky='w')

    def edit_records(self, new_name, name, new_price, old_price):
        query = 'UPDATE product SET name=?, price=? WHERE name=? AND price=?'
        param = (new_name, new_price, name, old_price)
        self.run_query(query, param)
        self.edit_wind.destroy()
        self.message['text'] = 'El registro {} ha sido actualizado satisfactoriamente'.format(name)
        self.get_products()

    def __init__(self, window):
        self.wind = window
        self.wind.title("Productos App")

        # -------------- FRAME --------------
        frame = LabelFrame(self.wind, text="Registrar un nuevo producto")
        frame.grid(row=0, column=0, columnspan=3, padx=10, pady=20)
        # frame.pack()

        # === LABELS y ENTRY ===
        Label(frame, text="Nombre: ").grid(row=1, column=0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row=1, column=1)

        Label(frame, text="Precio: ").grid(row=2, column=0)
        self.price = Entry(frame)
        self.price.grid(row=2, column=1)

        # -------------- BUTTONS --------------
        Button(frame, text="Guardar producto", command=self.add_product).grid(
            row=3, columnspan=2, sticky='we')

        # -------------- OUTPUT MESSAGES --------------
        self.message = Label(text='', fg='red')
        self.message.grid(row=3, column=0, columnspan=2, sticky='we')

        # -------------- TABLE --------------
        self.tree = ttk.Treeview(height=10, columns=2)
        self.tree.grid(row=4, column=0, columnspan=2)
        self.tree.heading('#0', text='Nombre', anchor='center')
        self.tree.heading('#1', text='Precio', anchor='center')

        # -------------- BUTTONS --------------
        Button(text="Eliminar", command=self.delete_product).grid(
            row=5, column=0, sticky='we')
        Button(text="Editar", command=self.edit_product).grid(
            row=5, column=1, sticky='we')

        self.get_products()


if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()
