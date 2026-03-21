import tkinter as tk
from tkinter import PhotoImage
import pygame as pg

# Funciones a llamar mas adelante.

def encontrarfactores(num):
    #esta funcion es complicada. para encontrar factores usualmente se usa la libreria math e iteracion, pero aqui no se podra
    #este metodo es extremadamente ineficiente para numeros grandes y puede llegar al limite de recursividad 
    #try se usa para la restriccion de solo aceptar numeros enteros.
    if isinstance(num,int):
        return encontrarfactores_aux(abs(num))
    else:
        return "Numero Invalido."
    
def encontrarfactores_aux(num, diviactual=1):
    #era necesario usar una lista para almenos almacenar las tuplas de los pares. no le vi manera de retornarlo sin una lista y que no
    #se viera feo o me diera error sin importar lo que hiciera.
    if diviactual ** 2 > num:
        return []
    else:
        resultados =  encontrarfactores_aux(num, diviactual + 1)
        if num % diviactual == 0:
            resultados.append((diviactual, num //diviactual))
        return resultados
    
# Creando la ventana base
root = tk.Tk()
root.title("Tarea Interfáz Gráfica Gabriel P")
root.geometry("500x500")
root.resizable(False,False)

# Imagenes para los fondos 
imagenfondo1 = PhotoImage(file="fondo1.png")
imagenfondo2 = PhotoImage(file="fondo2.png")

def ventana_analisisnums():
    #para no lidear con funciones con self y clases (indeciso si se pueden usar o no), es mas facil evitar que se hagan mas ventanas.
    #al cerrar la ventana secundaria regresa el acceso a la ventana principal.

    #Creacion de ventana adicional
    ventananums = tk.Toplevel()
    ventananums.title("Analisis de números")
    ventananums.geometry("400x400")
    ventananums.resizable(False,False)
    ventananums.focus()
    ventananums.grab_set()

    #Canvas y fondo
    canvas2 = tk.Canvas(ventananums,bg="#5D94C1",height=400,width=400)
    canvas2.pack()
    fondo2 = tk.Label(canvas2,image=imagenfondo2)
    fondo2.place(x=0,y=0)

    # Botones y entradas

    # Boton para cerrar la ventana

    # ARREGLAR LA ENTRADA Y VERIFICACION DE LAS RESTRICCIONES.
    numeroentrada = tk.IntVar()
    entradanum = tk.Entry(canvas2,justify="center",textvariable=numeroentrada)
    entradanum.place(relx=0.5,rely=0.4,anchor="center")
    numuser = numeroentrada.get()

    label2 = tk.Label(canvas2, text="Pares de factores:",justify="center",padx=5,pady=5,relief="groove",height=2,width=35,
                  font=(11))
    
    label2.place(relx=0.5,rely=0.3,anchor="center",)
    
    btcerrar1 = tk.Button(canvas2,text=("Regresar al menu"),justify="center",padx=2,pady=2,overrelief=("ridge"),
                          command=lambda: ventananums.destroy())
    btcerrar1.place(anchor="nw",x=10,y=10)

    btcalcular = tk.Button(canvas2,text=("Calcular "),justify="center",padx=2,pady=2,overrelief=("ridge"),
                           command=lambda: print(numuser))
    btcalcular.place(anchor="s", rely = 0.8,relx=0.9)

    

# Canvas y fondo del menu principal.
canvas1 = tk.Canvas(root,bg="#5D94C1",height=500,width=500)
canvas1.pack()
fondo1 = tk.Label(canvas1,image=imagenfondo1)
fondo1.place(x=0,y=0)


# Elementos del menu principal

#Texto de bienvenida
label1 = tk.Label(canvas1, text="Hola! Selecciona una opcion:",justify="center",padx=5,pady=5,relief="groove",height=2,width=35,
                  font=(16))
label1.place(relx=0.5,rely=0.3,anchor="center",)

#Boton para abrir la ventana de Analisis de numeros
btnumeros = tk.Button(canvas1, text=("Analisis de números"),justify="center",padx=5,pady=5,overrelief=("ridge"),
                      command=lambda:ventana_analisisnums())
btnumeros.place(relx=0.145,rely=0.94,anchor="sw")

#Boton para abrir la ficha personal
btficha = tk.Button(canvas1, text=("Ficha Personal"),justify="center",padx=10,pady=5,overrelief=("ridge"),
                    command=lambda:print("test"))
btficha.place(relx=0.520,rely=0.94,anchor="s")

#Boton para abrir la ventana de Animacion
btanimacion = tk.Button(canvas1, text=("Animación"),justify="center",padx=15,pady=5,overrelief=("ridge"),
                        command=lambda:print("test"))
btanimacion.place(relx=0.845,rely=0.94,anchor="se")

root.mainloop()
