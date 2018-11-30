from paquete_principal.miarchivo import *
from paquete_principal.Ejercicio import Alumno

m = MiArchivo()
lista = m.obtener_informacion()
#Cada una de las lineas se le hace un split
lista = [l.split("|") for l in lista]

o = MiArchivoEscribir()

lista = lista[1:]

for d in lista:
	p = Alumno()
	p.agregar_nombre(d[0])
	p.agregar_nota1(d[1])
	p.agregar_nota2(d[2])
	p.agregar_nota3(d[3])
	p.calcular_promedio()
	o.agregar_informacion(p)
	
m.cerrar_archivo()
o.cerrar_archivo()
