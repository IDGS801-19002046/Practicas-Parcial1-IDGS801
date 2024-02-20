from io import open

class Diccionario: 
    def __init__(self,esp=None,ing=None,idioma=None,buscar=None):
        self.esp=esp
        self.ing=ing
        self.idioma=idioma
        self.buscar=buscar
    def agregar(self,esp,ing):
         archivo1 = open('archivo.txt','a')
         archivo1.write(esp)
         archivo1.write(ing)
         archivo1.close() 
    
    def traducir(self,idioma,buscar):
         archivo1 = open('archivo.txt','r')
         l=[]
         for leer in archivo1.readlines():
             l.append(leer.rstrip().strip())
         i=l.index(buscar)
         if idioma=='Ingles':
             return l[i-1]
         else:
             return l[i+1]
