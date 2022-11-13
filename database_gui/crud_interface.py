import tkinter as tk
from tkinter import ttk

import crud as crud


class MainDB:
    def __init__(self, win):
        self.db_obj = crud.DbApp()
        # components
        self.code_label = tk.Label(win, text='Product code:')
        self.name_label = tk.Label(win, text="Product's name")
        self.price_label = tk.Label(win, text='Price')

        self.code_text = tk.Entry(bd=3)
        self.name_text = tk.Entry()
        self.price_text = tk.Entry()
        self.register_btn = tk.Button(
            win, text='Register', command=self.register_products)
        self.update_btn = tk.Button(
            win, text='Update', command=self.update_product)
        self.delete_btn = tk.Button(
            win, text='Delete', command=self.delete_product)
        self.clear_btn = tk.Button(
            win, text='Clear', command=self.clear_screen)
        # ----- TreeView Component  --------------------------------------------
        self.column_data = ("Code", "Name", "Price")
        self.tree_products = ttk.Treeview(win,
                                          columns=self.column_data,
                                          selectmode='browse')

        self.vert_scrollbar = ttk.Scrollbar(win,
                                            orient="vertical",
                                            command=self.tree_products.yview)
        self.vert_scrollbar.pack(side='right', fill='x')

        self.tree_products.configure(yscrollcommand=self.vert_scrollbar.set)

        self.tree_products.heading("Code", text="Code")
        self.tree_products.heading("Name", text="Name")
        self.tree_products.heading("Price", text="Price")

        self.tree_products.column("Code", minwidth=0, width=100)
        self.tree_products.column("Name", minwidth=0, width=100)
        self.tree_products.column("Price", minwidth=0, width=100)

        self.tree_products.pack(padx=10, pady=10)

        self.tree_products.bind("<<TreeviewSelect>>",
                                self.present_selected_records)
        # ---------------------------------------------------------------------
        # positioning of components in the window
        # ---------------------------------------------------------------------
        self.code_label.place(x=100, y=50)
        self.code_text.place(x=250, y=50)

        self.name_label.place(x=100, y=100)
        self.name_text.place(x=250, y=100)

        self.price_label.place(x=100, y=150)
        self.price_text.place(x=250, y=150)

        self.register_btn.place(x=100, y=200)
        self.update_btn.place(x=200, y=200)
        self.delete_btn.place(x=300, y=200)
        self.clear_btn.place(x=400, y=200)

        self.tree_products.place(x=100, y=300)
        self.vert_scrollbar.place(x=605, y=300, height=225)
        self.load_initial_data()
# -----------------------------------------------------------------------------

    def present_selected_records(self, event):
        self.clear_screen()
        for selection in self.tree_products.selection():
            item = self.tree_products.item(selection)
            code, name, price = item["values"][0:3]
            self.code_text.insert(0, code)
            self.name_text.insert(0, name)
            self.price_text.insert(0, price)
# -----------------------------------------------------------------------------

    def load_initial_data(self):
        try:
            self.id = 0
            self.iid = 0
            records = self.db_obj.select_data()
            print("************ data available in the DB ***********")
            for item in records:
                code = item[0]
                name = item[1]
                price = item[2]
                print("Code = ", code)
                print("name = ", name)
                print("Price  = ", price, "\n")

            self.tree_products.insert('', 'end',
                                      iid=self.iid,
                                      values=(code,
                                              name,
                                              price))
            self.iid = self.iid + 1
            self.id = self.id + 1
            print('Base Data')
        except:
            print('No data to load yet')
# -----------------------------------------------------------------------------
# Read Screen Data
# -----------------------------------------------------------------------------

    def read_fields(self):
        try:
            print("************ available data ***********")
            code = int(self.code_text.get())
            print('code', code)
            name = self.name_text.get()
            print('name', name)
            price = float(self.price_text.get())
            print('price', price)
            print('Data Read Successful!')
        except:
            print('Could not read data.')
        return code, name, price
# -----------------------------------------------------------------------------
# Register Product
# -----------------------------------------------------------------------------

    def register_products(self):
        try:
            print("************ available data ***********")
            code, name, price = self.read_fields()
            self.db_obj.inserirDados(code, name, price)
            self.tree_products.insert('', 'end',
                                      iid=self.iid,
                                      values=(code,
                                              name,
                                              price))
            self.iid = self.iid + 1
            self.id = self.id + 1
            self.clear_screen()
            print('Product Registered Successfully!')
        except:
            print('Unable to register.')
# -----------------------------------------------------------------------------
# Update Product
# -----------------------------------------------------------------------------

    def update_product(self):
        try:
            print("************ available data ***********")
            code, name, price = self.read_fields()
            self.db_obj.UpdateDados(code, name, price)
            # reload data on screen
            self.tree_products.delete(*self.tree_products.get_children())
            self.load_initial_data()
            self.clear_screen()
            print('Product Updated Successfully!')
        except:
            print('Unable to update.')
# -----------------------------------------------------------------------------
# Delete Product
# -----------------------------------------------------------------------------

    def delete_product(self):
        try:
            print("************ available data ***********")
            code, name, price = self.read_fields()
            self.db_obj.delete_data(code)
            # reload data on screen
            self.tree_products.delete(*self.tree_products.get_children())
            self.load_initial_data()
            self.clear_screen()
            print('Product Deleted Successfully!')
        except:
            print('Unable to delete product.')
# -----------------------------------------------------------------------------
# Clear the screen
# -----------------------------------------------------------------------------

    def clear_screen(self):
        try:
            print("************ available data ***********")
            self.code_text.delete(0, tk.END)
            self.name_text.delete(0, tk.END)
            self.price_text.delete(0, tk.END)
            print('Clear Fields!')
        except:
            print('Unable to clear fields.')


# -----------------------------------------------------------------------------
# Main Program
# -----------------------------------------------------------------------------
window = tk.Tk()
main = MainDB(window)
window.title('Welcome to Database Application')
window.geometry("720x600+10+10")
window.mainloop()
# -----------------------------------------------------------------------------
