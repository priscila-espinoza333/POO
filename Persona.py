from Curso import Curso #aqui estoy importando la información curso
class Persona:

    pais = "Chile" #Atributo de toda la clase
    lista_personas = [] #Lista de todas las instancia de Persona
    total_lineas_codigo = 0 #Total de lineas de codigo de TODOS

    def __init__(self, nombre, apellido, email, edad, nombre_curso): #A través de init INICIALIZAMOS nuestra instancia. SELF incluye toda la información sobre el objeto individual
        #nombre = "Juana", apellido = "De Arco", email = "juana@codingdojo.com", edad = 20
        self.nombre = nombre # self se refiera a la instancia que estemos estableciendo en este caso elena
        self.apellido = apellido
        self.email = email
        self.edad = edad
        self.lineas_codigo = 0 # aqui estoy cuantificando las lienas de codigo que una persona hace    
        Persona.lista_personas.append(self)
        self.clase = Curso(nombre_curso) #Valor por defecto

    def cumpleaños(self): #self = juana
        self.edad += 1 #juana.edad = 18
        print("¡Muchas felicidades!")
        if Persona.mayoria_edad(self.edad): #TRUE
            print("Wujuuu, eres mayor de edad")

    def codificar(self, abc): #abc = 45
        #self = elena, cantidad_lineas = 45
        self.lineas_codigo += abc
        Persona.total_lineas_codigo += abc
        if Persona.experto(self.lineas_codigo):
            print("Eres toda una experta codificando", self.nombre)


    @classmethod
    def imprime_lista(cls): #clase = Persona
        print("Total de personas:", len(cls.lista_personas))
        for personita in cls.lista_personas:
            print(personita.nombre)

    @staticmethod
    def mayoria_edad(edad): #edad = 18
        if edad >= 18:
            return True
        else:
            return False

    @staticmethod
    def experto(lineas): #recibo un número
        if lineas > 100: #Si el número es mayor a 100, entonces es experto
            return True
        else: # si no, entonces NO es experto aún
            return False

    def tomar_cerveza(self):#self = juana
        if Persona.mayoria_edad(self.edad): #18
            print("Aquí está tu cerveza", self.nombre)
        else:
            print("Lo siento no puedes tomar", self.nombre)






















































        