"Ejemplo de manejo de excepciones"
try:
	numero1 = input("Ingrese un numero 1: \n")
	numero1=int(numero1)
	numero2= input("Ingrese un numero 2: \n")
	numero2= int(numero2)
	operacion = numero1/numero2
	print("El valor de la operacion es %d" %(operacion))
	edad= input("Ingrese su edad: \n")
	edad= int(edad)
	print("Su edad es %d"%(edad))
except NameError:
	print("Existe un error : %s" %e)
except ValueError as e:
	print("Existe un error (%s): %s" %(e.__class__.e))
	except ZeroDivionError as e:
	print("Existe un error (%s): %s" %(e.__class__.e))
except Exception as e:
	print("Existe un error (%s): %s" %(e.__class__.e))
