
import pandas as pd

import tkinter
import tkinter.filedialog
from tkinter.constants import END
from tkinter import filedialog
from tkinter import ttk
window = tkinter.Tk()
from random import random, randrange
pd.set_option("display.max_rows", None, "display.max_columns", None)
window.title("generador de datos")
window.geometry("200x200")
#valores
invocadores=["Senor de la luna","Plantera","Emperatriz de la luz","Golem","Duque Fishron","none"]
resultList={"items": [], "invocadores": []}
def generarRandom():
    invoker=len(invocadores)
    aux2=0
    salida=[]
    aux=0
    result=""
    for i in range (100000) :
        aux2=randrange(invoker)
        if(aux2==0):
            salida=["Filomiau","Terrariano","Bengala Lunar","Espectro estelar","ADEE","Celebrador V2","Ultimo Prisma",
            "Baculo del portal lunar","Baculo de cristal arcoiris","fallo"] 
            aux=randrange(len(salida))
            result=salida[aux]
        if(aux2==1):
            salida=["Semillera","Relampago de Ortigas","Pistola de avispas","Venus Magnum"," Florecillas"
            ,"Lanzahojas","Lanzagranadas","Gancho de espinas","fallo"] 
            aux=randrange(len(salida))
            result=salida[aux]
        if(aux2==2):
            salida=["Brillo nocturno","Caleidoscopio","Anochecer","Luz Estelar","fallo"] 
            aux=randrange(len(salida))
            result=salida[aux] 
        if(aux2==3):
            salida=["Stynger","Hacha de mano poseida","piedra del sol","Ojo de golem","Rayo calorifico",
            "Baculo de tierra", "puño de golem","fallo"] 
            aux=randrange(len(salida))
            result=salida[aux]
        if(aux2==4):
            salida=["Tsunami","Baculo de tempestades","Tifon de cuchillas","Flairon", "Arma de burbujas","fallo"] 
            aux=randrange(len(salida))
            result=salida[aux]
        if(aux2==5):
            result="no se encontro invocador"
        salida.clear()
        
        resultList['invocadores'].append(invocadores[aux2])
        resultList['items'].append(result)
    df =    pd.DataFrame(resultList)
    df.to_csv('./output.csv')
        
          

    END

tkinter.Button(window,text="generar datos",font=12,command=generarRandom).place(x=50,y=70)
window.mainloop()