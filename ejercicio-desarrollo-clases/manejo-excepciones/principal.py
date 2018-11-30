"Ejemplo de manejo de excepciones"
try:
	edad= input("Ingrese su edad: \n")
	edad= int(edad)
	print("Su edad es %d"%(edad))
except NameError:
	print("Existe un error: %s")
