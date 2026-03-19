import tkinter as tk

# creando la ventana base
rootwidth = 500
rootheight = 500
root = tk.Tk()
root.title("Test")
root.geometry("500x500")
root.resizable(False,False)

# haciendo el primer canvas del mismo tamaño que la ventana base
canvas1 = tk.Canvas(root,bg="blue",height=500,width=500)
canvas1.pack()

# boton de prueba 
boton1 = tk.Button(canvas1, text=("test"),height=2,width=8,command=lambda:print("test"))
boton1.place(x= 10, y = 10)

root.mainloop()
