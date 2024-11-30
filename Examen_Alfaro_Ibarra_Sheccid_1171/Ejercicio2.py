print("")
print("Alfaro_Ibarra_Sheccid_3w_1171_Examen")
print("")
class Persona:
    def __init__(self, nombre, edad ):
        self.nombre = nombre
        self.edad = edad

#Definir un metodo que imprima los datos de la persona
def imprimir_datos(self):
    print(f"Nombre: {self.nombre}, Edad: {self.edad}")

#Definir un metodo que nos diga si la persona es mayor o menor de edad
def edad_mn( edad):
    if edad >=18:
        print("Es mayor de edad")
    else:
        print("Es menor de edad")

#Utilizar clase
persona1 = Persona("Sheccid", 16)
imprimir_datos(persona1)
saber_edad= edad_mn(persona1.edad)
