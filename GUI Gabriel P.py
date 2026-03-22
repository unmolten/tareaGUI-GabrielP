import tkinter as tk
from tkinter import PhotoImage
import pygame

# Funciones a llamar mas adelante.
def encontrarfactores(num):
    #esta funcion es complicada. para encontrar factores usualmente se usa la libreria math e iteracion, pero aqui no se podra
    #este metodo es extremadamente ineficiente para numeros grandes y puede llegar al limite de recursividad 
    #try se usa para la restriccion de solo aceptar numeros enteros. pero causa que numeros grandes no se puedan usar.
    try:
        num = int(num)
        return encontrarfactores_aux(abs(num))
    except:
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
fotopersonal = PhotoImage(file="fotomia.png")
fotopersonalsmall = fotopersonal.subsample(3,3)
fotoarea = PhotoImage(file="fotoarea.png")
fotoareasmall = fotoarea.subsample(2,2)

def cerrarventana(vent):
    vent.destroy()
    vent.grab_release()
    root.deiconify()


# Funcion para todo lo relacionado con la ventana de analisis de numeros
def abrirvent_analisisnums():
    #para no lidear con funciones con self y clases (indeciso si se pueden usar o no), es mas facil evitar que se hagan mas ventanas.
    #al cerrar la ventana secundaria regresa el acceso a la ventana principal.

    #Creacion de ventana adicional
    ventananums = tk.Toplevel()
    ventananums.title("Analisis de números")
    ventananums.geometry("400x400")
    ventananums.resizable(False,False)
    ventananums.focus()
    ventananums.grab_set()

    #Canvas
    canvas2 = tk.Canvas(ventananums,bg="#7AA7CC",height=400,width=400)
    canvas2.pack()

    # Botones, entradas y labels

    label3 = tk.Label(canvas2, text="Ingresar Número:",justify="center",padx=1,pady=1,relief="flat",bg="#7AA7CC",font=("",11))
    label3.place(relx=0.5,rely=0.5,anchor="center")
    
    entradanum = tk.Entry(canvas2,justify="center")
    entradanum.place(relx=0.5,rely=0.555,anchor="center")

    label2 = tk.Label(canvas2, text="Pares de factores:",justify="center",padx=3,pady=3,relief="flat",bg="#7AA7CC",font=("",13))
    label2.place(relx=0.5,rely=0.165,anchor="center")

    labelnums = tk.Label(canvas2,text="",justify="center",padx=5,pady=5,relief="groove",height=5,width=35,wraplength=235,font=("",11))
    labelnums.place(relx=0.5,rely=0.315,anchor="center")


    # Boton para cerrar la ventana
    btcerrar1 = tk.Button(canvas2,text=("Regresar al menu"),justify="center",padx=2,pady=2,overrelief=("ridge"),
                          command=lambda: cerrarventana(ventananums))
    btcerrar1.place(anchor="nw",x=10,y=10)

    # Boton para mostrar resultado
    btcalcular = tk.Button(canvas2,text=("Calcular "),justify="center",padx=2,pady=2,overrelief=("ridge"),
                            command=lambda: labelnums.config(text=encontrarfactores(entradanum.get())))
    btcalcular.place(anchor="center", rely = 0.625,relx=0.5)



# Funcion para lo relacionado a la ventana de la ficha
def abrirvent_ficha():
    # Igual modalidad que el resto de las ventanas.
    # Solo aqui se usa pygame para el audio, sorprendente mente solo se usa en 3 lineas.
    pygame.mixer.init()
    pygame.mixer.music.load("musica.mp3") 
    biografia = "Hola! Soy Gabriel, un estudiante en el Instituto Tecnológico de Costa Rica, soy de Cartago y estoy estudiando Ingieneria en Computadores " \
    "Honestamente no se que más decir sobre mi, puedo decir que tengo 2 gatos, pero ya nada más viene a la mente."
    datos = "Gabriel Picado J. Edad: 18 \n Carne: 2026012441"
    datosmusica = "Actualmente estoy escuchando: \n Banda: Jamiroquai \n Género: Acid Jazz / Funk \n Click me!"
    ventanaficha = tk.Toplevel()
    ventanaficha.title("Sobre mi")
    ventanaficha.geometry("600x500")
    ventanaficha.resizable(False,False)
    ventanaficha.focus()
    ventanaficha.grab_set()

    # Canvas y fondo
    canvas3 = tk.Canvas(ventanaficha,height=500,width=600)
    canvas3.pack()
    fondo2 = tk.Label(canvas3,image=imagenfondo2)
    fondo2.place(x=-10,y=0)

    # Botones, entradas y labels

    # Datos personales
    labeldatos = tk.Label(canvas3,text=datos,padx=3,pady=3,relief="groove",font=("",12))
    labeldatos.place(relx=0.17,rely=0.1,anchor="nw")
    # Biografia pequeña
    labelbiografia = tk.Label(canvas3, text=biografia,justify="center",padx=3,pady=3,relief="groove",height=8,width=33,
                              wraplength=250,font=("",11))
    labelbiografia.place(relx=0.1,rely=0.35,anchor="w")
    # Datos Musica
    btmusica = tk.Button(canvas3,text=datosmusica,padx=3,pady=3,relief="raised",font=("",11),overrelief="groove",
                         command=lambda:pygame.mixer.music.play(0))
    btmusica.place(relx=0.15,rely=0.575,anchor="nw")
    # Foto personal
    foto1 = tk.Label(canvas3,image=fotopersonalsmall,relief="raised")
    foto1.place(relx=0.625,rely=0.35,anchor="w")
    # Foto del Mapa
    foto2 = tk.Label(canvas3,image=fotoareasmall,relief="raised")
    foto2.place(relx=0.6325,rely=0.7,anchor="w")

    # Boton para regresar a la ventana de menu
    btcerrar1 = tk.Button(canvas3,text=("Regresar al menu"),justify="center",padx=2,pady=2,overrelief=("ridge"),
                          command=lambda: cerrarventana(ventanaficha))
    btcerrar1.place(anchor="nw",x=10,y=10)



# Canvas y fondo del menu principal.
canvas1 = tk.Canvas(root,bg="#5D94C1",height=500,width=500)
canvas1.pack()
fondo1 = tk.Label(canvas1,image=imagenfondo1)
fondo1.place(x=-10,y=0)

# Elementos del menu principal

#Texto de bienvenida
label1 = tk.Label(canvas1, text="Hola! Selecciona una opcion:",justify="center",padx=5,pady=5,relief="groove",height=2,width=35,
                  font=(16))
label1.place(relx=0.5,rely=0.3,anchor="center",)

#Boton para abrir la ventana de Analisis de numeros
btnumeros = tk.Button(canvas1, text=("Analisis de números"),justify="center",padx=5,pady=5,overrelief=("ridge"),
                      command=lambda:abrirvent_analisisnums())
btnumeros.place(relx=0.145,rely=0.94,anchor="sw")

#Boton para abrir la ficha personal
btficha = tk.Button(canvas1, text=("Ficha Personal"),justify="center",padx=10,pady=5,overrelief=("ridge"),
                    command=lambda:abrirvent_ficha())
btficha.place(relx=0.520,rely=0.94,anchor="s")

#Boton para abrir la ventana de Animacion
btanimacion = tk.Button(canvas1, text=("Animación"),justify="center",padx=15,pady=5,overrelief=("ridge"),
                        command=lambda:print("test"))
btanimacion.place(relx=0.845,rely=0.94,anchor="se")

root.mainloop()
