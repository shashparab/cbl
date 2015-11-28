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

    self.quitButton = tk.Button(self, text='Quit', command=self.quit)
    self.quitButton.grid()




root = tk.Tk()
root.geometry("1000x600")

app = Application(root)
app.master.title('Californian Beverages LTD')
root.mainloop()


