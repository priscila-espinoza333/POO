from Persona import Persona
from Estudiante import Estudiante

#Instancia de persona
elena = Persona("Elena", "De Troya", "elena@codingdojo.com", 30, "Bootcamp Python")
juana = Persona("Juana", "De Arco", "juana@codingdojo.com", 17, "Bootcamp Java")

print(elena.nombre)
print(juana.nombre)

elena.cumpleaños()

print(elena.edad)
print(juana.edad)

print(elena.lineas_codigo)
print(juana.lineas_codigo)

elena.codificar(45)
print(elena.lineas_codigo)
elena.codificar(10)
print(elena.lineas_codigo)
print(juana.lineas_codigo)

print(elena.pais)
print(juana.pais)

Persona.pais = "México"
print(elena.pais)

Persona.imprime_lista()

pablo = Persona("Pablo", "Picasso", "pablo@codingdojo.com", 50, "Bootcamp MERN")

Persona.imprime_lista()

juana.cumpleaños()

print(juana.edad)

juana.tomar_cerveza()

pablo.codificar(101)

elena.clase.agrega_calificacion(9)
elena.clase.agrega_calificacion(7)

print(elena.clase.calificaciones)

pedro = Estudiante("Pedro", "Páramo", "pedro@codingdojo.com", 30, "Bootcamp Python", 1234)

print(pedro.id)

pedro.codificar(100)

print(pedro.lineas_codigo)

pedro.cumpleaños()

Persona.imprime_lista()

Estudiante.imprime_lista()

#elena.que_haces()
pedro.que_haces()

pedro.estudiar()
