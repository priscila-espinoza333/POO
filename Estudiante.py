from Persona import Persona

class Estudiante(Persona): #Estamos diciendo que la clase a heredar es Persona

    lista_estudiantes = []

    #Estudiante
    def __init__(self, nombre, apellido, email, edad, nombre_curso, id):
        super().__init__(nombre, apellido, email, edad, nombre_curso) #Comenzamos con el de Persona
        self.id = id
        Estudiante.lista_estudiantes.append(self)

    
    @classmethod
    def imprime_lista(cls):
        print("Total de estudiantes:", len(cls.lista_estudiantes))
        for estudiante in cls.lista_estudiantes:
            print(estudiante.nombre)

    
    def cumpleaños(self):
        super().cumpleaños() #Referencia a la función de mi superior
        print("A seguir estudiando ;)")

    def que_haces(self):
        print("Estoy estudiando en Coding Dojo y aprendiendo muchísimo!")

    def estudiar(self):
        print("Hoy estamos estudiando python")
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
