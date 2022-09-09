class Persona:

    def __init__(self, nombre, apellido, email, edad): # A travez de iit inicializamos nuestra instancia. SELF incluye toda la informacion sobre el objeto individual

        set.nomnre = nombre
        set.apellido = apellido
        set.email = email
        set.edad = 30


    def cumpleaños(self): #self = elena
        self.edad += 1  
        #elena.edad = 31
        print("Muchas Felicidades!")

    def condificar(self, abc): 
        #self = elena, cantidad_lineas = 45
        self.lineas_codigo += abc        