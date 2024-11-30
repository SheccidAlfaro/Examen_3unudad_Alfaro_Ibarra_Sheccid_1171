print("")
print("Alfaro_Ibarra_Sheccid_3w_1171_Examen")
print("")
#Definir una clase llamada Calculadora
class Calculadora:
#Definir metodo para sumar
 def sumar(self, a, b):
    return a + b

#Definir metodo para restar
 def restar(self, a, b):
    return a - b

#Definir metodo para multiplicar
 def multiplicar(self, a, b):
    return a * b

#Definir metodo para dividir
 def dividir(self, a, b):
    return a / b

# Llamar a los metodos de la clase Calculadora
calculadora = Calculadora()
print("Suma: ", calculadora.sumar(20, 5))
print("resta : ", calculadora.restar(20, 5))
print("Multiplicacion: ", calculadora.multiplicar(20, 5))
print ("Division: ", calculadora.dividir(20, 5))