from tkinter import *
from os import path as ps
from selenium import webdriver as wb
import time

root = Tk()
root.title('Web Crawler GUI')
root_height = 500
root_width = 500
root.geometry(f'{root_height}x{root_width}')
root.iconbitmap(r'static\img\favicon.ico')
text_entry = Entry(root, width=50)
text_entry.insert(0,'Enter the name of the chemical')
text_entry.pack()

def get_compount():
    compound = text_entry.get()
    
    url = r'https://pubchem.ncbi.nlm.nih.gov/compound/{}'.format(compound)
    x = ps.abspath('msedgedriver.exe')
    driver = wb.Edge(x)
    driver.get(url)

plotline_btn = Button(root, text='Submit', command=get_compount)
plotline_btn.pack(padx=20, pady=25)

root.mainloop()