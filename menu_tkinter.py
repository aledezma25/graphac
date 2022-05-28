from __future__ import division
from encodings import utf_8
from re import sub
# from tkinter.tix import IMAGETEXT
from tokenize import PlainToken
from tracemalloc import start
from turtle import colormode, position
import json
#
from math import sqrt
import matplotlib.pyplot as plt
import networkx as nx
# 
from ast import Try
from lib2to3.pgen2.token import VBAREQUAL
import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

from matplotlib.pyplot import imread, fill
from PIL import Image, ImageDraw
from clases import *
import pymongo

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

width = 350
height = 390
center = height//2

image1=Image.new("RGB",(width, height), red)
image2=Image.new("RGB",(width+120,height+20), red)
draw = ImageDraw.Draw(image1)
draw2 =ImageDraw.Draw(image2)

#Crear grafo
g = grafo()
l = []

#Funcion para abrir archivos
def abrir_archivos():
    archivo = filedialog.askopenfilename(title="abrir", initialdir="C:/", filetypes=(("Archivos de Texto", ".txt"),("Archivos Excel",".xlsx"),("Archivos JSON",".json")))
    print(archivo)

def guardar_archivos():
    archivo = filedialog.asksaveasfilename(title="Guardar", initialdir="C:/", filetypes=(("Archivos de Texto", ".txt"),("Archivos Excel",".xlsx"),("Archivos JSON",".json")))
    print(archivo)

def aleatorio():
    class Dupla: # Se define esta clase dupla para hacer mas sencillo el acceso a los valores X Y de cada nodo o vertice
        def _init_(self, x, y):
            self.x = x
            self.y = y
    def CalcDis(Dup1, Dup2):# Usando una ecuacion simple calculamos la distancia de cada arista en base a sus vertices
        return sqrt(pow((Dup1.x - Dup2.x), 2) + pow((Dup1.y - Dup2.y), 2))  # calcula la distancia entre dos puntos

    G = nx.Graph() # Se crea un grafo nulo
    vertices_G = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
    # se crean todos los vertices
    G.add_nodes_from(vertices_G)# se le asignan dichos vertices o nodos al grafo
    aristas_G = [('A', 'B'), ('A', 'C'), ('A', 'F'), ('A', 'G'), ('B', 'D'), ('B', 'E'), ('B', 'G'), ('B', 'H'),
                ('C', 'D'), ('C', 'F'), ('C', 'G'), ('D', 'E'), ('D', 'F'), ('D', 'G'), ('D', 'H'), ('D', 'J'),
                ('D', 'K'), ('E', 'G'), ('E', 'H'), ('E', 'I'), ('F', 'K'), ('F', 'L'), ('F', 'S'), ('G', 'H'),
                ('G', 'I'), ('G', 'J'), ('H', 'I'), ('I', 'M'), ('I', 'N'), ('I', 'O'), ('J', 'K'), ('J', 'M'),
                ('J', 'N'), ('J', 'Q'), ('K', 'L'), ('K', 'Q'), ('L', 'M'), ('L', 'O'), ('L', 'P'), ('L', 'Q'),
                ('M', 'P'), ('M', 'Q'), ('M', 'R'), ('N', 'O'), ('N', 'T'), ('O', 'J'), ('O', 'Q'), ('O', 'R'),
                ('O', 'T'), ('P', 'Q'), ('P', 'S'), ('Q', 'J'), ('Q', 'S'), ('R', 'S'), ('R', 'T'), ('S', 'T')]
    # se crean todas las aristas
    G.add_edges_from(aristas_G)# se le asignan dichas aristas al grafo
    ubica = {'A': (2, 1), 'B': (19, 1), 'C': (5, 2), 'D': (11, 3), 'E': (18, 5), 'F': (4, 6), 'G': (12, 7), 'H': (20, 8),
             'I': (16, 10), 'J': (10, 10), 'K': (7, 11), 'L': (5, 13), 'M': (11, 13), 'N': (19, 14), 'O': (16, 16),
             'P': (4, 17), 'Q': (9, 17), 'R': (11, 19), 'S': (1, 20), 'T': (20, 20)}
    #se crea un diccionario con los cada vertice y su ubicacion en el plano X Y
    puntoA = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
    puntoA.x = ubica['A'][0]
    puntoA.y = ubica['A'][1]
    puntoB = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
    puntoB.x = ubica['B'][0]
    puntoB.y = ubica['B'][1]
    puntoC = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
    puntoC.x = ubica['C'][0]
    puntoC.y = ubica['C'][1]
    puntoD = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
    puntoD.x = ubica['D'][0]
    puntoD.y = ubica['D'][1]
    puntoE = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
    puntoE.x = ubica['E'][0]
    puntoE.y = ubica['E'][1]
    puntoF = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
    puntoF.x = ubica['F'][0]
    puntoF.y = ubica['F'][1]
    puntoG = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
    puntoG.x = ubica['G'][0]
    puntoG.y = ubica['G'][1]
    puntoH = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
    puntoH.x = ubica['H'][0]
    puntoH.y = ubica['H'][1]
    puntoI = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
    puntoI.x = ubica['I'][0]
    puntoI.y = ubica['I'][1]
    puntoJ = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
    puntoJ.x = ubica['J'][0]
    puntoJ.y = ubica['J'][1]
    puntoK = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
    puntoK.x = ubica['K'][0]
    puntoK.y = ubica['K'][1]
    puntoL = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
    puntoL.x = ubica['L'][0]
    puntoL.y = ubica['L'][1]
    puntoM = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
    puntoM.x = ubica['M'][0]
    puntoM.y = ubica['M'][1]
    puntoN = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
    puntoN.x = ubica['N'][0]
    puntoN.y = ubica['N'][1]
    puntoO = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
    puntoO.x = ubica['O'][0]
    puntoO.y = ubica['O'][1]
    puntoP = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
    puntoP.x = ubica['P'][0]
    puntoP.y = ubica['P'][1]
    puntoQ = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
    puntoQ.x = ubica['Q'][0]
    puntoQ.y = ubica['Q'][1]
    puntoR = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
    puntoR.x = ubica['R'][0]
    puntoR.y = ubica['R'][1]
    puntoS = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
    puntoS.x = ubica['S'][0]
    puntoS.y = ubica['S'][1]
    puntoT = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
    puntoT.x = ubica['T'][0]
    puntoT.y = ubica['T'][1]
    Puntos = {'A': puntoA, 'B': puntoB, 'C': puntoC, 'D': puntoD, 'E': puntoE, 'F': puntoF, 'G': puntoG, 'H': puntoH,
              'I': puntoI, 'J': puntoJ, 'K': puntoK, 'L': puntoL, 'M': puntoM, 'N': puntoN, 'O': puntoO, 'P': puntoP,
              'Q': puntoQ, 'R': puntoR, 'S': puntoS, 'T': puntoT}
    #Se crea un diccionario de los puntos antes creados para tener un acceso mas simple
    # se crea un contador como iterador de el ciclo for
    cont: int = 0
    for i in aristas_G:
        Pa = Puntos[aristas_G[cont][0]]
        Pb = Puntos[aristas_G[cont][1]]
        G.edges[i]['distancia'] = CalcDis(Pa, Pb)*100
        # se calcula la distancia entre vertices y se multiplica por 100 ya que
        # cada unidad de nuestro plano vale 100 metros, luego se asigna como peso a cada arista
        print('La distancia entre ', aristas_G[cont], G.edges[i],'[METROS]')
        cont = cont + 1
    nx.draw(G, pos=ubica, node_color='gray', with_labels=True)
    # se dibuja el grafo
    plt.show()




#
#Funcion para abrir el manual de usuario en el apartado de ayuda
def open_Ayuda_manual():
    os.startfile(".\Desktop\grafos_python\ayuda\manual_usuario_graphac")

#Funcion para abrir mas sobre grafos en el apartado de ayuda
def open_Ayuda_Grafos():
    os.startfile("https://es.wikipedia.org/wiki/Grafo")


#Agregar nodo al mapa
def añadirnodo():
    ingreso = Toplevel()
    ingreso.title('Agregar Nodo')
    tnombre = Label(ingreso, text='Ingrese nombre del nodo:')
    px= Label(ingreso, text= "x: ")
    py= Label(ingreso, text= "y: ")
    tnombre.grid(row=0, column=0)
    px.grid(row=1, column=0)
    py.grid(row=2, column=0)
    nombrev = Entry(ingreso)
    x = Entry(ingreso)
    y = Entry(ingreso)
    nombrev.grid(row=0, column=1)
    x.grid(row=1, column=1)
    y.grid(row=2, column=1)
    agregar = Button(ingreso, text="Agregar", command=lambda: agregarv(x, y, nombrev.get(), ingreso))
    agregar.grid(row=3, columnspan=2)

def agregarv(x, y, nombre, ingreso):
    try:
        gradoa = float(100)
        if (gradoa < 1):
            ingreso.destroy()
        else:
            vtemp = vertice(nombre, x, y)
            g.agregarVertice(vtemp)
            ingreso.destroy()
            actualizar()
    except ValueError:
        ingreso.destroy()

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
    # relacionar3 = Button(vrelacion, text="No Dirigida", command=lambda: relacion_No_Dirijida(opciones1.get(opciones1.curselection()), 
                                                                            #   opciones2.get(opciones2.curselection()),nv3.get(), vrelacion))
    # relacionar3.pack()

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
        canvas3.create_oval(g.listav[i].x+5, g.listav[i].y+5, g.listav[i].x + ancho-5, g.listav[i].y + ancho-5, fill="#3498D8", activefill="#E67E22")

        draw.ellipse([g.listav[i].x-120, g.listav[i].y-120, g.listav[i].x-120 + ancho, g.listav[i].y-120 + ancho], fill="#3498D8", outline="green")
        draw2.ellipse([g.listav[i].x, g.listav[i].y, g.listav[i].x + ancho, g.listav[i].y + ancho], fill="#3498D8", outline="green" )
    
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

#Barra de menús
barraMenu=Menu(ventana)

# canvas3.bind("<Double-1", dobleclick)

#Menu y submenus para Archivo
menuArchivo=Menu(barraMenu)
    #Submenu del submenu nuevo grafo
submenu_nuevografo=Menu(menuArchivo, tearoff=False)
submenu_nuevografo.add_command(label="Personalizado")
submenu_nuevografo.add_command(label="Aleatorio", command=aleatorio)
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
submenu_nodo.add_command(label="Agregar", command=añadirnodo)
submenu_nodo.add_command(label="Editar")
submenu_nodo.add_command(label="Eliminar", command=clickeliminarv)
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


