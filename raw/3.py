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
    Label(text="SETTLEMENT SHEET",bg="grey").grid(row=0, column=3)

##############################################################
    self.row_list = ["Sales Person's Name","Settlement Sheet Number","Settlement Sheet Date","Route Name and Code"]
    
    row = 1
    wid = 20

    for value in self.row_list:
  	  Label(text=value, relief=RIDGE,  width=wid).grid(row=row, column=0)
  	  row += 1

    for row_num in range(1,len(self.row_list)+1):
  	  Entry(bg="white", relief=SUNKEN, width=wid).grid(row=row_num, column=1)

    Label(text='').grid(row=8, column=0)

##############################################################

    column_values = ['Product Description', 'Previous Returns','Load From Warehouse', 'Total Stock On Truck', 'Current Returns', 'Theoretical Sales', 'Actual Sales', 'Variance']
    row_values = ['Soda Water', 'Tonic Water',  'Lemonade', 'Total']

    col = 0
    
    row = 9
    for value in column_values:
      Label(text=value, relief=RIDGE,  width=wid).grid(row=row, column=col)
      col = col+1

    Label(text="Mixers 250ml", bg="orange",relief=RIDGE,  width=wid).grid(row=row+1, column=0)

    col = 0
    for row_num in range (row+2,len(row_values)+row+2):
      for col_num in range (len(column_values)): 
        Entry(bg="white",   relief=SUNKEN, width=wid).grid(row=row_num, column=col_num)


    for value in row_values:
      Label(text=value, relief=RIDGE,  width=wid).grid(row=row+2, column=0)
      row = row+1

##############################################################

    row_values = ['Applemax', 'Cali Cola',  'Hubbly Bubbly', 'Swift Limon', 'Ginger Beer', 'Swift Mixedberry', 'Swift Naartjie','Grape Max', 'Mint Max', 'Max Combo', 'Total']

    Label(text="Carbonates 350ml", bg="orange",relief=RIDGE,  width=wid).grid(row=row+2, column=0)

    col = 0
    for row_num in range (row+3,len(row_values)+row+3):
      for col_num in range (len(column_values)): 
        Entry(bg="white",   relief=SUNKEN, width=wid).grid(row=row_num, column=col_num)


    for value in row_values:
      Label(text=value, relief=RIDGE,  width=wid).grid(row=row+3, column=0)
      row = row+1


##############################################################

    row_values = ['Orange OLE', 'Pineapple',  'Black Currant', 'Cream Soda', 'Raspberry', 'Total']

    Label(text="Motts 1L", bg="orange",relief=RIDGE,  width=wid).grid(row=row+3, column=0)

    col = 0
    for row_num in range (row+4,len(row_values)+row+4):
      for col_num in range (len(column_values)): 
        Entry(bg="white",   relief=SUNKEN, width=wid).grid(row=row_num, column=col_num)


    for value in row_values:
      Label(text=value, relief=RIDGE,  width=wid).grid(row=row+4, column=0)
      row = row+1

##############################################################

    row_values = ['Orange OLE', 'Pineapple',  'Black Currant', 'Cream Soda', 'Raspberry', 'Total']

    Label(text="Motts 2L", bg="orange",relief=RIDGE,  width=wid).grid(row=row+4, column=0)

    col = 0
    for row_num in range (row+5,len(row_values)+row+5):
      for col_num in range (len(column_values)): 
        Entry(bg="white",   relief=SUNKEN, width=wid).grid(row=row_num, column=col_num)


    for value in row_values:
      Label(text=value, relief=RIDGE,  width=wid).grid(row=row+5, column=0)
      row = row+1

root = tk.Tk()
root.geometry("1000x700")

app = Application(root)
app.master.title('Californian Beverages LTD')
root.mainloop()
