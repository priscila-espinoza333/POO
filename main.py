from Persona import Persona

#Instancia de persona
elena = Persona("Elena, De Troya", "elena@codingdojo.com", 30)
juana = Persona("Juana", "De Arco", "juana@codingdojo.com", 20)

print(elena.nombre)
print(juana.nombre)

elena.cumpleaños()

print(elena.edad)
print(juana.edad)

print(elena.lineas_codigo)
print(juana.lineas_codigo)

elena.codigo(45)
print(elena.lineas_codigo)

elena.codificar(45)
print(elena.lineas_codigo)
elena.codificar(10)
print(elena.lineas_codigo)
print(juana.lineas_codigo)

