#!/usr/bin/python3
import tkinter as tk
from tkinter import * 
import sys

class Application(tk.Frame):
  
  def __init__(self, master=None):
    tk.Frame.__init__(self, master)
    self.grid()
    self.master = master
    self.createWidgets()
    t = SimpleTable(self, 10,8)
    t.grid()
    t.set(0,0,"Product Description")
    t.set(0,1,"Previous Returns")
    t.set(0,2,"Load From Warehouse")
    t.set(0,3,"Total Stock On Truck")
    t.set(0,4,"Current Returns")
    t.set(0,5,"Theoretical Sales")
    t.set(0,6,"Actual Sales")
    t.set(0,7,"Variance")

  def createWidgets(self):
    self.sheetName = Label(self, text='SETTLEMENT SHEET')
    self.sheetName.grid()
    
    def printTxt():
      f = open('cbl.csv', 'w')
      sys.stdout = f
      print("SalesPerson Name : " + salesPerson.get())
      print("Settlement Sheet Number : " + sheetNumber.get())
      print("Settlement Sheet Date : " + sheetDate.get())
      print("Route Name and Code : " + route.get())

    Label(self, text="Sales Person's Name :").grid(row=1)
    salesPerson = Entry(self)
    salesPerson.grid(row=1,column=1)
    
    Label(self, text="Settlement Sheet Number :").grid(row=2)
    sheetNumber = Entry(self)
    sheetNumber.grid(row=2,column=1)

    Label(self, text="Settlement Sheet Date :").grid(row=3)
    sheetDate = Entry(self)
    sheetDate.grid(row=3,column=1)
    Label(self, text="Route Name & Code :").grid(row=4)
    route = Entry(self)
    route.grid(row=4,column=1)
    ok = tk.Button(self, text='Ok', command=printTxt) 
    ok.grid(row=4,column=2)


class SimpleTable(tk.Frame):
    def __init__(self, parent, rows=10, columns=3):
        # use black background so it "peeks through" to 
        # form grid lines
        tk.Frame.__init__(self, parent, background="black")
        self._widgets = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                label = tk.Label(self, text="%s/%s" % (row, column),borderwidth=0, width=18)
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                current_row.append(label)
            self._widgets.append(current_row)

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)

        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid()

    def set(self, row, column, value):
        widget = self._widgets[row][column]
        widget.configure(text=value)



root = tk.Tk()
#root.geometry("1000x600")

app = Application(root)
app.master.title('Californian Beverages LTD')
root.mainloop()


