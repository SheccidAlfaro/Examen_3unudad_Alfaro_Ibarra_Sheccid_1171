print("")
print("Alfaro_Ibarra_Sheccid_3w_1171_Examen")
print("")
#Definir una clase llamada Agenda 
class Agenda:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

#Definir un método llamado agregar_contacto para agregar contactos a la agenda
def agregar_contacto(agenda, nombre, telefono, correo):
    agenda.append(Agenda(nombre, telefono, correo))
 #Definir un menu para interactuar con la agenda
def menu():
    print("Añadir contacto")
    print ("Lista de contactos")
    print ("Buscar contacto")
    print ("Editar contacto")
    print ("Cerrar agenda")
    