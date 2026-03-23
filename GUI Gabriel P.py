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
    
# A pesar de que esta fucion tenga demasiados argumentos, es util para tener la ventana por separado.
# Como se trabajan con 2 distintos circulos no es tan facil hacer esto, ademas tomo mucha investigacion
# ya que usualmente esto se hace en pygame pero aqui tambien funciona.
def mover(circ1,circ2,canv,dx1,dy1,dx2,dy2,slider):

    vel = slider.get()
    x1, y1, x2, y2 = canv.coords(circ1)
    x3, y3, x4, y4 = canv.coords(circ2)
    # Revisar colisiones entre si e invertir velocidades horizontales, si chocan verticalmente se oponen
    if x1 <= x4 and x2 >= x3 and y1 <= y4 and y2 >= y3:
        dx1, dx2 = dx2, dx1 # Se tienen que cambiar los 2 valores a la vez porque si no, hay problemas
        dy1, dy2 = dy2, dy1
    # Revisar colisiones con las paredes para el circulo 1 y se ponen las direcciones inversas
    if x1 <= 0 or x2 >= 300:
        dx1 = -dx1
    if y1 <= 0 or y2 >= 250:
        dy1 = -dy1
    # revisar colisiones circulo 2
    if x3<= 0 or x4 >= 300:
        dx2 = -dx2
    if y3<= 0 or y4 >= 250:
        dy2 = -dy2

    # Honestamente no se como hacer que los circulos no se queden atascados con las paredes, ya no encuentro nada más pero es muy minimo.
    canv.move(circ1,dx1,dy1)
    canv.move(circ2,dx2,dy2)

    # Se usa la velocidad para hacer la animacion aparentar mas rapida
    # Por alguna razon solo se actualizaba la velocidad cuando movia el mouse?
    # Investigando, me di cuenta que tuvo que ser algo con windows y el tiempo, honestamente no se.
    root.after(45 -vel ,mover,circ1,circ2,canv,dx1,dy1,dx2,dy2,slider)


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


# Funcion para cerrar las ventanas 
def cerrarventana(vent):
    pygame.mixer.init()
    pygame.mixer.quit()
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
    canvasnums = tk.Canvas(ventananums,bg="#7AA7CC",height=400,width=400)
    canvasnums.pack()

    # Botones, entradas y labels

    label3 = tk.Label(canvasnums, text="Ingresar Número:",justify="center",padx=1,pady=1,relief="flat",bg="#7AA7CC",font=("",11))
    label3.place(relx=0.5,rely=0.7,anchor="center")
    
    entradanum = tk.Entry(canvasnums,justify="center")
    entradanum.place(relx=0.5,rely=0.755,anchor="center")

    label2 = tk.Label(canvasnums, text="Pares de factores:",justify="center",padx=3,pady=3,relief="flat",bg="#7AA7CC",font=("",13))
    label2.place(relx=0.5,rely=0.115,anchor="center")

    labelnums = tk.Label(canvasnums,text="",justify="center",padx=5,pady=5,relief="groove",height=10,width=35,wraplength=250,font=("",11))
    labelnums.place(relx=0.5,rely=0.40,anchor="center")


    # Boton para cerrar la ventana
    btcerrar = tk.Button(canvasnums,text=("Regresar al menu"),justify="center",padx=2,pady=2,overrelief=("ridge"),
                          command=lambda: cerrarventana(ventananums))
    btcerrar.place(anchor="nw",x=10,y=10)

    # Boton para mostrar resultado
    btcalcular = tk.Button(canvasnums,text=("Calcular "),justify="center",padx=2,pady=2,overrelief=("ridge"),
                            command=lambda: labelnums.config(text=encontrarfactores(entradanum.get())))
    btcalcular.place(anchor="center", rely = 0.825,relx=0.5)



# Funcion para lo relacionado a la ventana de la ficha
def abrirvent_ficha():
    # Igual modalidad que el resto de las ventanas.
    # Solo aqui se usa pygame para el audio, sorprendentemente no se usa tanto.
    pygame.mixer.init()
    pygame.mixer.music.load("musica.mp3") 
    biografia = "Hola! Soy Gabriel, un estudiante en el Instituto Tecnológico de Costa Rica, soy de Cartago y estoy estudiando Ingieneria en Computadores " \
     "Honestamente no se que más decir sobre mi, puedo decir que tengo 2 gatos, pero ya nada más me viene a la mente."
    datos = "Gabriel Picado J. Edad: 18 \n Carne: 2026012441"
    datosmusica = "Actualmente estoy escuchando: \n Banda: Jamiroquai \n Género: Acid Jazz / Funk \n \n Click me!"
    ventanaficha = tk.Toplevel()
    ventanaficha.title("Sobre mi")
    ventanaficha.geometry("600x500")
    ventanaficha.resizable(False,False)
    ventanaficha.focus()
    ventanaficha.grab_set()

    # Canvas y fondo
    canvasficha = tk.Canvas(ventanaficha,height=500,width=600)
    canvasficha.pack()
    fondo2 = tk.Label(canvasficha,image=imagenfondo2)
    fondo2.place(x=-10,y=0)

    # Botones, entradas y labels

    # Datos personales
    labeldatos = tk.Label(canvasficha,text=datos,padx=3,pady=3,relief="groove",font=("",12))
    labeldatos.place(relx=0.17,rely=0.1,anchor="nw")
    # Biografia pequeña
    labelbiografia = tk.Label(canvasficha, text=biografia,justify="center",padx=3,pady=3,relief="groove",height=8,width=33,
                              wraplength=250,font=("",11))
    labelbiografia.place(relx=0.1,rely=0.35,anchor="w")

    # Foto personal
    foto1 = tk.Label(canvasficha,image=fotopersonalsmall,relief="raised")
    foto1.place(relx=0.625,rely=0.35,anchor="w")
    # Foto del Mapa
    foto2 = tk.Label(canvasficha,image=fotoareasmall,relief="raised")
    foto2.place(relx=0.6325,rely=0.7,anchor="w")

    # Boton Musica
    btmusica = tk.Button(canvasficha,text=datosmusica,padx=3,pady=3,relief="raised",font=("",11),overrelief="groove",
                         command=lambda:pygame.mixer.music.play(0))
    btmusica.place(relx=0.15,rely=0.575,anchor="nw")
    # Boton para regresar a la ventana de menu
    btcerrar = tk.Button(canvasficha,text=("Regresar al menu"),justify="center",padx=2,pady=2,overrelief=("ridge"),
                          command=lambda: cerrarventana(ventanaficha))
    btcerrar.place(anchor="nw",x=10,y=10)

# Funcion para la animacion
def abrir_animacion():
    # Posiciones iniciales para los circulos
    x1,x2,y1,y2 =10,50,10,50
    x3,x4,y3,y4 = 160,120,40,80

    #Ventana para la animacion
    ventanaanim = tk.Toplevel(bg="gray")
    ventanaanim.title("Animación")
    ventanaanim.geometry("400x400")
    ventanaanim.resizable(False,False)
    ventanaanim.focus()
    ventanaanim.grab_set()

    #Canvas para la animacion
    canvasanim= tk.Canvas(ventanaanim,height=250,width=300,bg="#303030")
    canvasanim.pack(pady=50)
    circulo1 = canvasanim.create_oval(x1,y1,x2,y2,width=1,fill="red",outline="red")
    circulo2 = canvasanim.create_oval(x3,y3,x4,y4,width=1,fill="green",outline="green")

    # slider para la velocidad
    slidervel = tk.Scale(ventanaanim,from_=30,to=1,orient="horizontal")
    slidervel.place(anchor="center",relx=0.5,rely=0.815)
    slidervel.set(15)

    # No tengo ni la menor idea porque tira un error al cerrar la ventana. pero por lo menos cierra bien
    btcerrar = tk.Button(ventanaanim,text=("Regresar al menu"),justify="center",padx=2,pady=2,overrelief=("ridge"),
                          command=lambda: cerrarventana(ventanaanim))
    btcerrar.place(anchor="nw",x=10,y=10)
    mover(circulo1,circulo2,canvasanim,6,5,7,8,slidervel)

# Elementos del menu principal

# Canvas y fondo del menu principal.
canvas1 = tk.Canvas(root,bg="#5D94C1",height=500,width=500)
canvas1.pack()
fondo1 = tk.Label(canvas1,image=imagenfondo1)
fondo1.place(x=-10,y=0)

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
                        command=lambda:abrir_animacion())
btanimacion.place(relx=0.845,rely=0.94,anchor="se")


root.mainloop()
