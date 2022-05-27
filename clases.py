from msilib.schema import Class
import tkinter
import sys

class grafo():
    
    def __init__(self):
        self.listav = []
        self.listaA = []
    
    def __str__(self):
        return str(self.listav)

    def agregarVertice(self, v):
        self.listav.append(v)

    def agregarArista(self, a):
        self.listaA.append(a)

    def profundidad(self, inicio, lprofundidad=[]):
        if (inicio in lprofundidad):
            return
        lprofundidad.append(inicio)
        for vecino in inicio.la:
            self.profundidad(vecino,lprofundidad)
        return lprofundidad
    
    # def dijkstra(self, inicio):
    #     listadistancias=[]
    #     listavisitados=[]
    #     listaprevios=[]

    #     #inicio de las listas
    #     for i in range (len(self.listasv)):
    #         listadistancias.append(self.listav[i].distancia)
    #         listavisitados.append(self.listav[i].visitado)
    #         listaprevios.append(self.listav[i].predecesor)
    #         if inicio.nombre == self.listav[i].nombre:
    #             listadistancias[i] = 0
    #             listavisitados[i] = True
    #             listaprevios[i] = None
    #     #Calcular distancias de la lista de adyacencia del vertice de inicio
    #     for i in self.listaA:
    #         for j in inicio.la:
    #             if(inicio.nombre==i.frm.nombre and j.nombre==i.to.nombre):
    #                 distancia=i.distancia
    #                 listadistancias[self.listav.index(i.to)]=distancia
    #                 listaprevios[self.listav.index(i.to)]=inicio
        
    #     #Busca el menor de la lista no visitado
    #     for bol in listavisitados:
    #         for bol2 in listavisitados:
    #             nmin = sys.maxsize
    #             if bol2 == False:
    #                 for nm in range (len(listagrados)):
    #                     if listagrados[nm]<nmin and listavisitados[nm]==False:
    #                         nmin =listagrados[nm]

    #                 temp = nmin
    #                 indice = listagrados.index(temp)
    #         listavisitados[indice] = True

class vertice():
    def __init__(self, nombre, x, y):
        self.la = []
        self.ld = []
        self.nombre = nombre
        self.x = x
        self.y = y
        self.distancia = sys.maxsize
        # self.visitado = False
        # self.predecesor = None


    def __str__(self):
        return str(self.la)

    def vecino(self, ver_ad):
        self.la.append(ver_ad)

class arista():
    def __init__(self, frm, to, distancia, x1, y1, x2, y2):
        self.ld = []
        self.frm = frm
        self.to = to
        self.distancia = distancia
        self.var = tkinter.IntVar()
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2





