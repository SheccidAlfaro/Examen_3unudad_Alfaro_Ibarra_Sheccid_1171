print("")
print("Alfaro_Ibarra_Sheccid_3w_1171_Examen")
print("")
#Definir una clase Llamado triangulo, con los atributos para saber si es equilatero, isosceles o escaleno
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

#Definir un metodo para saber si el triangulo es equilatero, isosceles o escaleno
def tipo_de_triangulo(triangulo):
    if triangulo.lado1 == triangulo.lado2 == triangulo.lado3:
        return "Equilatero"
    elif triangulo.lado1 == triangulo.lado2 or triangulo.lado1 == triangulo.lado3 or triangulo.lado2 == triangulo.lado3:
        return "Isosceles"
    else :
        return "Escaleno"

#Crear el objeto de la clse triangulo preguntando los lados al usuario
lado1 = float (input("Ingrese el primer lado del triangulo: "))
lado2 = float (input("Ingrese el segundo lado del triangulo: "))
lado3 = float (input("Ingrese el tercer lado del triangulo: "))
#Crear el objeto de la clase triangulo
triangulo = Triangulo(lado1, lado2, lado3)
#Llamar al metodo tipo de triangulo y mostrar el resultado
print("El tipo de triangulo es: ", tipo_de_triangulo(triangulo))