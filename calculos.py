from tkinter import font
from numpy.lib import math
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tkinter
import tkinter.filedialog
from tkinter.constants import END
from tkinter import filedialog
from tkinter import ttk
window = tkinter.Tk()
from random import random, randrange
pd.set_option("display.max_rows", None, "display.max_columns", None)
window.title("Calculos")
window.geometry("850x550")
df= pd.read_csv('output.csv')
#valores
items= ["Filomiau","Terrariano","Bengala Lunar","Espectro estelar","ADEE","Celebrador V2","Ultimo Prisma",
"Baculo del portal lunar","Baculo de cristal arcoiris","Semillera","Relampago de Ortigas","Pistola de avispas",
"Venus Magnum"," Florecillas","Lanzahojas","Lanzagranadas","Gancho de espinas","Brillo nocturno","Caleidoscopio",
"Anochecer","Luz Estelar","Stynger","Hacha de mano poseida","piedra del sol","Ojo de golem","Rayo calorifico",
"Baculo de tierra", "puno de golem","Tsunami","Baculo de tempestades","Tifon de cuchillas","Flairon", "Arma de burbujas","fallo","no se encontro invocador"]
resultList={"items": [], "invocadores": []}
#combo select item
listaDespegableItems = ttk.Combobox(window, width=30)
listaDespegableItems.place(x=30,y=50)
listaDespegableItems['values']=items
#tabla
table = ttk.Treeview(window, style="mystyle.Treeview", columns=(
    "#1", "#2", "#3"),show='headings') 
table.heading("#1", text="i") 
table.heading("#2", text="invocador")
table.heading("#3", text="item")
table.column("#1", width=30)  
table.column("#2", width=150)
table.column("#3", width=150)
table.place(x=473, y=40, height=360)

def llenarTabla():
    for i in range(100000):
        table.insert('','end',values=(i,df['invocadores'].get(i),df['items'].get(i)))

def llenarVisual():
    tkinter.Label(window,text="Analisis con 1000 datos",font=12).place(x=33,y=160)
    tkinter.Label(window,text="casos favorables = ",font=12).place(x=33,y=190)
    tkinter.Label(window,text="probabilidad = ",font=12).place(x=33,y=210)
    tkinter.Label(window,text="Analisis con 5000 datos",font=12).place(x=33,y=240)
    tkinter.Label(window,text="casos favorables = ",font=12).place(x=33,y=270)
    tkinter.Label(window,text="probabilidad = ",font=12).place(x=33,y=300)
    tkinter.Label(window,text="probabilidad = ",font=12).place(x=33,y=390)
    tkinter.Label(window,text="Analisis con 10000 datos",font=12).place(x=33,y=330)
    tkinter.Label(window,text="casos favorables = ",font=12).place(x=33,y=360)
    tkinter.Label(window,text="probabilidad = ",font=12).place(x=33,y=470)
    tkinter.Label(window,text="Analisis con 100000 datos",font=12).place(x=33,y=410)
    tkinter.Label(window,text="casos favorables = ",font=12).place(x=33,y=440)

def probabilidadEmpirica():
    salida=''
    casosFavorables=0
    casoAcomprobar= listaDespegableItems.get()
    result=""
    #1000 observaciones
    for i in range (1000) :
        df['invocadores'].get(i)
        if(df['invocadores'].get(i)=="Senor de la luna"):
            salida= df['items'].get(i) 
            result=salida
            if(result==casoAcomprobar):
                casosFavorables=casosFavorables+1  
        if(df['invocadores'].get(i)=="Plantera"):
            salida= df['items'].get(i) 
            result=salida
            if(result==casoAcomprobar):
                casosFavorables=casosFavorables+1
        if(df['invocadores'].get(i)=="Emperatriz de la luz"):
            salida= df['items'].get(i) 
            result=salida
            if(result==casoAcomprobar):
                casosFavorables=casosFavorables+1   
        if(df['invocadores'].get(i)=="Golem"):
            salida= df['items'].get(i) 
            result=salida
            if(result==casoAcomprobar):
                casosFavorables=casosFavorables+1 
        if(df['invocadores'].get(i)=="Duque Fishron"):
            salida= df['items'].get(i) 
            result=salida
            if(result==casoAcomprobar):
                casosFavorables=casosFavorables+1
        if(df['invocadores'].get(i)=="none"):
            result="no se encontro invocador"
            if(result==casoAcomprobar):
                casosFavorables=casosFavorables+1
    total=casosFavorables/1000
    tkinter.Label(window,text=casosFavorables,font=12).place(x=170,y=190)
    tkinter.Label(window,text=total,font=12).place(x=150,y=210)
    #5000 observaciones
    for i in range (5000) :
        df['invocadores'].get(i)
        if(df['invocadores'].get(i)=="Senor de la luna"):
            salida= df['items'].get(i) 
            result=salida
            if(result==casoAcomprobar):
                casosFavorables=casosFavorables+1
            
        if(df['invocadores'].get(i)=="Plantera"):
            salida= df['items'].get(i) 
            result=salida
            if(result==casoAcomprobar):
                casosFavorables=casosFavorables+1
            
        if(df['invocadores'].get(i)=="Emperatriz de la luz"):
            salida= df['items'].get(i) 
            result=salida
            if(result==casoAcomprobar):
                casosFavorables=casosFavorables+1
            
        if(df['invocadores'].get(i)=="Golem"):
            salida= df['items'].get(i) 
            result=salida
            if(result==casoAcomprobar):
                casosFavorables=casosFavorables+1

            
        if(df['invocadores'].get(i)=="Duque Fishron"):
            salida= df['items'].get(i) 
            result=salida
            if(result==casoAcomprobar):
                casosFavorables=casosFavorables+1
        if(df['invocadores'].get(i)=="none"):
            result="no se encontro invocador"
            if(result==casoAcomprobar):
                casosFavorables=casosFavorables+1
    total=casosFavorables/5000   
    tkinter.Label(window,text=casosFavorables,font=12).place(x=170,y=270)
    tkinter.Label(window,text=total,font=12).place(x=150,y=300)
    #10000 observaciones
    for i in range (10000) :
        df['invocadores'].get(i)
        if(df['invocadores'].get(i)=="Senor de la luna"):
            salida= df['items'].get(i) 
            result=salida
            if(result==casoAcomprobar):
                casosFavorables=casosFavorables+1
            
        if(df['invocadores'].get(i)=="Plantera"):
            salida= df['items'].get(i) 
            result=salida
            if(result==casoAcomprobar):
                casosFavorables=casosFavorables+1
            
        if(df['invocadores'].get(i)=="Emperatriz de la luz"):
            salida= df['items'].get(i) 
            result=salida
            if(result==casoAcomprobar):
                casosFavorables=casosFavorables+1
            
        if(df['invocadores'].get(i)=="Golem"):
            salida= df['items'].get(i) 
            result=salida
            if(result==casoAcomprobar):
                casosFavorables=casosFavorables+1

            
        if(df['invocadores'].get(i)=="Duque Fishron"):
            salida= df['items'].get(i) 
            result=salida
            if(result==casoAcomprobar):
                casosFavorables=casosFavorables+1
        if(df['invocadores'].get(i)=="none"):
            result="no se encontro invocador"
            if(result==casoAcomprobar):
                casosFavorables=casosFavorables+1
    total=casosFavorables/10000   
    tkinter.Label(window,text=casosFavorables,font=12).place(x=170,y=360)
    tkinter.Label(window,text=total,font=12).place(x=150,y=390)
    #100000 observaciones
    for i in range (100000) :
        df['invocadores'].get(i)
        if(df['invocadores'].get(i)=="Senor de la luna"):
            salida= df['items'].get(i) 
            result=salida
            if(result==casoAcomprobar):
                casosFavorables=casosFavorables+1
            
        if(df['invocadores'].get(i)=="Plantera"):
            salida= df['items'].get(i) 
            result=salida
            if(result==casoAcomprobar):
                casosFavorables=casosFavorables+1
            
        if(df['invocadores'].get(i)=="Emperatriz de la luz"):
            salida= df['items'].get(i) 
            result=salida
            if(result==casoAcomprobar):
                casosFavorables=casosFavorables+1
            
        if(df['invocadores'].get(i)=="Golem"):
            salida= df['items'].get(i) 
            result=salida
            if(result==casoAcomprobar):
                casosFavorables=casosFavorables+1

            
        if(df['invocadores'].get(i)=="Duque Fishron"):
            salida= df['items'].get(i) 
            result=salida
            if(result==casoAcomprobar):
                casosFavorables=casosFavorables+1
        if(df['invocadores'].get(i)=="none"):
            result="no se encontro invocador"
            if(result==casoAcomprobar):
                casosFavorables=casosFavorables+1
    total=casosFavorables/100000   
    tkinter.Label(window,text=casosFavorables,font=12).place(x=170,y=440)
    tkinter.Label(window,text=total,font=12).place(x=150,y=470)
    llenarVisual()
    END

tkinter.Button(window,text="llenar Tabla",font=12,command=llenarTabla).place(x=33,y=80)
tkinter.Button(window,text="Generar Datos",font=12,command=probabilidadEmpirica).place(x=33,y=120)
window.mainloop()