from tkinter import *
import csv
import os

root = Tk()

class InventoryManagement(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.master.title('Inventory Management')
        self.grid()
        self.items = []
        root.geometry("650x450")

        self.load_inventory() 
        self.itemCount = len(self.items)
        
        Label(self, text='Search (Product Name): ').grid(row=0, column=1, padx=6, pady=20, sticky=E)
        
        self._box1 = StringVar()
        self._input = Entry(self, width=20, textvariable=self._box1)
        self._input.grid(row=0, column=2, padx=8, pady=20, sticky=W)

        self.btn1 = Button(self, text='Search', command=self.searchInventory)
        self.btn1.grid(row=0, column=3, padx=8, pady=20, sticky=W)

        self.btn2 = Button(self, text='Reset', command=self.clearSearch)
        self.btn2.grid(row=0, column=4, padx=4, pady=20, sticky=W)


        self.scroll = Scrollbar(self)
        self.scroll.grid(row=3, column=4)
        self.text = Text(self, width=60, height=10, wrap=WORD, yscrollcommand=self.scroll.set)
        self.text.grid(row=3, column=0, columnspan=5, padx=20, pady=20)
        self.scroll.config(command=self.text.yview)

        Label(self, text="Item Count: " + str(self.itemCount)).grid(row=4, column=0, pady=5, sticky=N)

        Label(self, text='Product Name ').grid(row=6, column=0, padx=6, pady=6, sticky=W)
        
        self._box3 = StringVar()
        self._input = Entry(self, width=20, textvariable=self._box3)
        self._input.grid(row=6, column=1, padx=8, pady=10, sticky=E)

        Label(self, text='Count ').grid(row=10, column=0, padx=6, pady=6, sticky=E)

        self._box4 = StringVar()
        self._input = Entry(self, width=20, textvariable=self._box4)
        self._input.grid(row=10, column=1, padx=8, pady=10, sticky=W)

        self.btn3 = Button(self, text='Add Item', command=self.addItem)
        self.btn3.grid(row=11, column=1, padx=5, pady=20, sticky=W)

        self.btn4 = Button(self, text='Edit Item', command=self.editItem)
        self.btn4.grid(row=11, column=2, padx=5, pady=20, sticky=W)

        self.btn5 = Button(self, text='Delete Item', command=self.deleteItem)
        self.btn5.grid(row=11, column=3, padx=5, pady=20, sticky=W)

        self.text.insert(END, 'Product Name' + '\t\t' + 'Count' + '\t\t\n')
        self.text.insert(END, '------------------------------------------------------------')
        self.text.configure(state="disabled")

        self.populate_inventory_display()

    def load_inventory(self):
        if os.path.exists('output.csv'):
            with open('output.csv', mode='r') as file:
                reader = csv.reader(file)
                self.items = [(row[0], row[1]) for row in reader if row]  
        else:
            print("CSV file not found!")  
            self.items = []

    def populate_inventory_display(self):
        """Display the loaded products in the Text widget."""
        self.text.configure(state="normal")
        for item in self.items:
            self.text.insert(END, item[0] + '\t\t\t\t' + item[1] + '\t\t\n')
        self.text.configure(state="disabled")

    def addItem(self):
        self.text.configure(state="normal")
        self.text.delete(1.0, END)
        self.text.insert(END, 'Product Name' + '\t\t\t\t' + 'Count' + '\t\t\n')
        self.text.insert(END, '------------------------------------------------------------')

        product_name = self._box3.get()
        count = self._box4.get()

        if product_name != '' and count != '':
            record = (product_name, count)
            self.items.append(record)

            for item in self.items:
                self.text.insert(END, item[0] + '\t\t\t\t' + item[1] + '\t\t\n')
        else:
            self.text.delete(1.0, END)
            self.text.insert(END, 'Error: One or more fields have been left blank.')

        self._box3.set('')
        self._box4.set('')
        self._input.focus_set()
        self.text.configure(state="disabled")

    def searchInventory(self):
        self.text.configure(state="normal")
        self.text.delete(1.0, END)
        self.text.insert(END, 'Product Name' + '\t\t\t\t' + 'Count' + '\t\t\n')
        self.text.insert(END, '------------------------------------------------------------')

        searchVal = self._box1.get()

        for item in self.items:
            if item[0].lower() == searchVal.lower():  
                self.text.insert(END, item[0] + '\t\t\t\t' + item[1] + '\t\t\n')

        self.text.configure(state="disabled")

    def clearSearch(self):
        self._box1.set('')

    def editItem(self):
        self.text.configure(state="normal")
        self._box3.set('')
        self._box4.set('')

        searchVal = self._box1.get()

        for item in self.items:
            if item[0].lower() == searchVal.lower():
                self.items.remove(item)
                self._box3.set(item[0])
                self._box4.set(item[1])

        self._box1.set('')
        self._input.focus_set()
        self.text.configure(state="disabled")

    def deleteItem(self):
        self.text.configure(state="normal")
        self.text.delete(1.0, END)
        self.text.insert(END, 'Product Name' + '\t\t\t\t' + 'Count' + '\t\t\n')
        self.text.insert(END, '------------------------------------------------------------')

        searchVal = self._box1.get()

        for item in self.items:
            if item[0].lower() == searchVal.lower():
                self.items.remove(item)

        for item in self.items:
            self.text.insert(END, item[0] + '\t\t\t\t' + item[1] + '\t\t\n')

        self._box1.set('')
        self.text.configure(state="disabled")

def main():
    InventoryManagement().mainloop()

main()
