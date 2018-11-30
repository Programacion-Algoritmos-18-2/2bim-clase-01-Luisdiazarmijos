class Alumno(object):

    def __init__(self):
        self.nombre=""
        self.nota1 = 0
        self.nota2 = 0
        self.nota3 = 0
        self.promedio=0
        #Declaramos los agregar

    def agregar_nombre(self,n):
        self.nombre = n
        pass

    def agregar_nota1(self, n1):
        self.nota1=float(n1)
        pass
    def agregar_nota2(self, n2):
        self.nota2 =float(n2)
        pass
    def agregar_nota3(self, n3):
        self.nota3 =float(n3)
        pass
    #Declaramos los obtener
    def obtener_nombre(self):
        return self.nombre
        pass
    def obtener_nota1(self):
        return self.nota1
        pass
    def obtener_nota2(self):
        return self.nota2
        pass
    def obtener_nota3(self):
        return self.nota3
        pass
        #Calculamos el priomedio
    def calcular_promedio(self):
        self.promedio = (self.nota1 + self.nota2 + self.nota3)/ 3
    
    def __str__(self):
        return "%f - %f - %f " %(self.nota1, self.nota2, self.nota3)
        