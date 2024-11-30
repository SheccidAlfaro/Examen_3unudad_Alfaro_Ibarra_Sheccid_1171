print("")
print("Alfaro_Ibarra_Sheccid_3w_1171_Examen")
print("")
#Crear una clase
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

#Definir metodo que imprima los datos del alumno
def imprimir(alumno):
    print(f"Nombre: {alumno.nombre}")
    print(f"Calificacion : {alumno.nota}")

#Definir metodo que diga si el alumno aprobo o no
def calificacion_final (alumno):
    if alumno >= 60:
        print("Aprobado")
    else:
        print("Reprobado")

#utilizar la clase
alumno1 = Alumno("Sheccid", 80)
imprimir(alumno1)
calificacion= calificacion_final(alumno1.nota)
