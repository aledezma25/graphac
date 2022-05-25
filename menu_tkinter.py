import os
from tkinter import *
from tkinter import filedialog
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


