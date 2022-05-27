from ast import Try
from lib2to3.pgen2.token import VBAREQUAL
from ntpath import join
import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

from matplotlib.pyplot import draw, fill
from clases import *
import pymongo


#Funcion para abrir archivos
def abrir_archivos():
    archivo = filedialog.askopenfilename(title="abrir", initialdir="C:/", filetypes=(("Archivos de Texto", ".txt"),("Archivos Excel",".xlsx"),("Archivos JSON",".json")))
    print(archivo)

def guardar_archivos():
    archivo = filedialog.asksaveasfilename(title="Guardar", initialdir="C:/", filetypes=(("Archivos de Texto", ".txt"),("Archivos Excel",".xlsx"),("Archivos JSON",".json")))
    print(archivo)

#
#Funcion para abrir el manual de usuario en el apartado de ayuda
def open_Ayuda_manual():
    os.startfile(".\Desktop\grafos_python\ayuda\manual_usuario_graphac")

#Funcion para abrir mas sobre grafos en el apartado de ayuda
def open_Ayuda_Grafos():
    os.startfile("https://es.wikipedia.org/wiki/Grafo")

    
#Ventana Principal
ventana = Tk()
ventana.geometry("600x600")
ventana.title("GraphAC")
ventana.iconbitmap('')
canvas3 = Canvas(ventana, width=400, height=450, bg="#B3B6B7")
canvas3.pack(fill=BOTH, expand=YES)


ancho = 40
li = []
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0,128, 0)

width = 550
height = 570
center = height//2

#por copiar
# image1 = image.new()

#Crear grafo
g = grafo()
l = []
#
#
#

#Informcacion del vertice
def click(event):
    for event in g.listav:
        if event.x > vert.x and event.x < vert.x + ancho and event.y > vert.y and event.y < vert.y + ancho:
            info = Toplevel()
            info.title('Informacion del Punto')
            l1 = Label(info, text='Nombre').grid(row=0, column=0)
            l2 = Label(info, text=vert.nombre).grid(row=0,column=1)


#Agregar nodo al mapa usando doble click
def dobleclick(event):
    ingreso = Toplevel()
    ingreso.title('Agregar Punto')
    tnombre = Label(ingreso, text='Ingrese nombre del vertice:')
    tnombre.grid(row=0, column=0)
    nombrev = Entry(ingreso)
    nombrev.grid(row=0, column=1)

    agregar = Button(ingreso, text="Agregar", command=lambda: agregarv(event.x, event.y, nombrev.get(), ingreso))
    agregar.grid(row=3, columnspan=2)

def agregarv(x, y, nombre, ingreso):
    try:
        gradoa = float(100)
        if (gradoa < 1):
            ingreso.destroy()
            messagebox.showerror("ERROR", "El grado de accidentalidad no está permitido")
        else:
            vtemp = vertice(nombre, x, y)
            g.agregarVertice(vtemp)
            ingreso.destroy()
            actualizar()
    except ValueError:
        ingreso.destroy()
        messagebox.showerror("ERROR", "Usted no digitó un grado de accidentalidad correcto")

def AgregarA(frm, to, distancia, x1, y1, x2, y2):
    atemp = arista(frm, to, distancia, x1, y1, x2, y2)
    g.agregarArista(atemp)
    actualizar()

def clickrelacion():
    vrelacion = Toplevel()
    vrelacion.title("Agregar Ruta")
    opciones1 = Listbox(vrelacion, exportselection=0)
    opciones2 = Listbox(vrelacion, exportselection=0)
    for v in g.listav:
        opciones1.insert(END, v.nombre)
        opciones2.insert(END, v.nombre)
    opciones1.pack(side=LEFT)
    opciones2.pack(side=LEFT)

    t3=Label(vrelacion, text="Ingrese el peso")
    t3.pack()
    nv3=Entry(vrelacion)
    nv3.pack()

    relacionar2 = Button(vrelacion, text="Dirigida", command=lambda: relacion(opciones1.get(opciones1.curselection()), 
                                                                              opciones2.get(opciones2.curselection()),nv3.get(), vrelacion))
    relacionar2.pack()
    relacionar3 = Button(vrelacion, text="No Dirigida", command=lambda: relacion_No_Dirijida(opciones1.get(opciones1.curselection()), 
                                                                              opciones2.get(opciones2.curselection()),nv3.get(), vrelacion))
    relacionar3.pack()

def relacion(nv1, nv2, nv3, vrelacion):
    if (nv1 == nv2):
        vrelacion.destroy()
        messagebox.showinfo("Denegado", "No puede seleccionar el mismo punto de interés")
    else:
        for v in g.listav:
            a = v
            for v in g.listav:
                if(nv2 == v.nombre):
                    b = v
                    a.vecino(b)
                    d = int(nv3)
                    AgregarA(a, b, d, a.x, a.y, b.x, b.y)
                    vrelacion.destroy()
            actualizar()

 #Eliminar vertices
def clickeliminarv():
    veliminar = Toplevel()
    veliminar.title("Eliminar Punto")
    t1 = Label(veliminar, text="Nombre punto de interes")
    t1.pack()
    opciones = Listbox(veliminar, exportselection=0)
    for v in g.listav:
        opciones.insert(END, v.nombre)
    opciones.pack()
    nombrev = Entry(veliminar)
    nombrev.pack()
    eliminar = Button(veliminar, text="Eliminar", command=lambda: eliminarv(nombrev.get(), veliminar))
    eliminar.pack()
    eliminar2 = Button(veliminar, text="Elimina desde listas", command=lambda: eliminarv(opciones.get(opciones.curselection()), veliminar))
    eliminar2.pack()

def eliminarv(nombrev, veliminar):
    a=1

def actualizar():
    num = ancho / 2

    canvas3.delete("all")
    for i in range(len(g.listav)):
        canvas3.create_oval(g.listav[i].x, g.listav[i].y, g.listav[i].x + ancho, g.listav[i].y + ancho, fill="#3498D8", width=0)
        canvas3.create_oval(g.listav[i].x+5, g.lista[i].y+5, g.lista[i].x + ancho-5, g.listav[i].y + ancho-5, fill="#3498D8", activefill="#E67E22")

        draw.ellipse([g.lista[i].x-120, g.listav[i].y-120, g.listav[i].x-120 + ancho, g.listav[i].y-120 + ancho], fill="#3498D8", outline="green")
        draw2.ellipse([g.lista[i].x, g.listav[i].y, g.listav[i].x + ancho, g.listav[i].y + ancho], fill="#3498D8", outline="green" )
    
    for i in range(len(g.listaA)):
        if g.listaA[i].x1 >= g.listaA[i].x2 and g.listaA[i].y1 > g.listaA[i].y2:
            canvas3.create_line(g.listaA[i].x1 + num, g.listaA[i].y1, g.listaA[i].x2 + ancho, g.listaA[i].y2 + num, width=3, fill="#A3E4D7", arrow="last", smooth=True)
            draw.line([g.listaA[i].x1-120 + num, g.listaA[i].y1-120, g.listaA[i].x2-120 + ancho, g.listaA[i].y2-120 + num], fill="#A3E4D7", width=3, joint=None)
            draw2.line([g.listaA[i].x1 + num, g.listaA[i].y1, g.listaA[i].x2 + ancho, g.listaA[i].y2 + num], fill="#A3E4D7", width=3, joint=None)
        
        if g.listaA[i].x1 > g.listaA[i].x2 and g.listaA[i].y1 < g.listaA[i].y2:
            canvas3.create_line(g.listaA[i].x1 + num, g.listaA[i].y1 + ancho, g.listaA[i].x2 + ancho, g.listaA[i].y2 + num, width=3, fill="#A3E4D7", arrow="last", smooth=True)
            draw.line([g.listaA[i].x1-120 + num, g.listaA[i].y1-120 + ancho, g.listaA[i].x2-120 + ancho, g.listaA[i].y2-120 + num], fill="#A3E4D7", width=3, joint=None)
            draw2.line([g.listaA[i].x1 + num, g.listaA[i].y1 + ancho, g.listaA[i].x2 + ancho, g.listaA[i].y2 + num], fill="#A3E4D7", width=3, joint=None)
        
        if g.listaA[i].x1 <= g.listaA[i].x2 and g.listaA[i].y1 > g.listaA[i].y2:
            canvas3.create_line(g.listaA[i].x1 + num, g.listaA[i].y1, g.listaA[i].x2, g.listaA[i].y2 + num, width=3, fill="#A3E4D7", joint=None)
            draw.line([g.listaA[i].x1-120 + num, g.listaA[i].y1-120, g.listaA[i].x2-120, g.listaA[i].y2-120 + num], fill="#A3E4D7", width=3, joint=None)












canvas3.bind('<Double-1', dobleclick)





#Barra de menús
barraMenu=Menu(ventana)

#Menu y submenus para Archivo
menuArchivo=Menu(barraMenu)
    #Submenu del submenu nuevo grafo
submenu_nuevografo=Menu(menuArchivo, tearoff=False)
submenu_nuevografo.add_command(label="Personalizado")
submenu_nuevografo.add_command(label="Aleatorio")
menuArchivo.add_cascade(label = "Nuevo Grafo", menu=submenu_nuevografo)
##########################################
menuArchivo.add_command(label="Abrir", command=abrir_archivos)
menuArchivo.add_command(label="Cerrar", command=ventana.destroy)
menuArchivo.add_command(label="Guardar", command=guardar_archivos)
menuArchivo.add_command(label="Guardar como")
    #Submenu del submenu Exportar datos
submenu_exportar=Menu(menuArchivo, tearoff=False)
submenu_exportar.add_command(label="Excel")
submenu_exportar.add_command(label="Imagen")
submenu_exportar.add_command(label="PDF")
menuArchivo.add_cascade(label = "Exportar datos", menu=submenu_exportar)
##########################################
menuArchivo.add_command(label="Importar datos")
menuArchivo.add_command(label="Inicio")
menuArchivo.add_command(label="Imprimir")

#Menu y submenus para Editar
menuEditar=Menu(barraMenu)
menuEditar.add_command(label="Deshacer")
    #Submenu del submenu Nodo
submenu_nodo=Menu(menuEditar, tearoff=False)
submenu_nodo.add_command(label="Agregar")
submenu_nodo.add_command(label="Editar")
submenu_nodo.add_command(label="Eliminar")
menuEditar.add_cascade(label = "Nodo", menu=submenu_nodo)
###########################################
submenu_arco=Menu(menuEditar, tearoff=False)
submenu_arco.add_command(label="Agregar")
submenu_arco.add_command(label="Editar")
submenu_arco.add_command(label="Eliminar")
menuEditar.add_cascade(label = "Arco", menu=submenu_arco)

#Menu y submenus para Analizar
menuAnalizar=Menu(barraMenu)
    #Submenu del submenu Algoritmos
submenu_alg=Menu(menuEditar, tearoff=False)
submenu_alg.add_command(label="Algoritmo 1")
submenu_alg.add_command(label="Algoritmo 2")
submenu_alg.add_command(label="Algoritmo 3")
menuAnalizar.add_cascade(label = "Algoritmos", menu=submenu_alg)

#Menu y submenu para Herramientas
menuHerramienta=Menu(barraMenu)
menuHerramienta.add_command(label="Ejecución")

#Menu y submenu para Aplicacion
menuAplicacion=Menu(barraMenu)
menuAplicacion.add_command(label="Aplicacion 1")

#Menu y submenu para Ventana
menuVentana=Menu(barraMenu)
menuVentana.add_command(label="Gráfica")
menuVentana.add_command(label="Tabla")

#Menu y submenu para Ayuda
menuAyuda=Menu(barraMenu)
menuAyuda.add_command(label="Ayuda", command=open_Ayuda_manual)
menuAyuda.add_command(label="Acerca de Grafos", command=open_Ayuda_Grafos)

#Aqui se agregan a los menus para abrir en modo cascada
barraMenu.add_cascade(label="Archivo",menu=menuArchivo)
barraMenu.add_cascade(label="Editar",menu=menuEditar)
barraMenu.add_cascade(label="Analizar",menu=menuAnalizar)
barraMenu.add_cascade(label="Herramientas",menu=menuHerramienta)
barraMenu.add_cascade(label="Aplicacion",menu=menuAplicacion)
barraMenu.add_cascade(label="Ventana",menu=menuVentana)
barraMenu.add_cascade(label="Ayuda",menu=menuAyuda)

ventana.config(menu=barraMenu)

ventana.mainloop()


