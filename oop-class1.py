class Profesor:

    def __init__(self ,el_nombre, el_gmail):
        
        self.nombre = el_nombre

        self.gmail = el_gmail

    def dime_tu_nombre(self):

        return self.nombre
class Alumno:

    def __init__(self , el_seleccionado):

        self.nombre = el_seleccionado

        self.inasistencia = 0

        self.dieta = ""

        self.mentor = None

    def mentoria(self,profesor):

        self.mentor = profesor

    
    def falta(self):
        
        self.inasistencia += 1 
            

    def elegir_dieta(self ,la_dieta):

        self.dieta = la_dieta

    def es_vegetariano(self):

        self.dieta = "vegetariano"

    def esta_libre(self):

        if self.inasistencia >5:

            return "QUEDA LIBRE"
        
        else:
            return "ESTA BIEN"
        

profe_elio = Profesor("Elio", "elio@gmail.com")

profe_gabi = Profesor("Gabi", "gabi@gmail.com")

print(profe_elio.dime_tu_nombre())

print(profe_gabi.dime_tu_nombre())

alumno_martino = Alumno("Martino")

alumno_juampablo = Alumno("Juampablo")

alumno_martino.falta()

alumno_martino.falta()

alumno_martino.falta()

alumno_martino.falta()

alumno_martino.falta()

alumno_martino.falta()

print(alumno_martino.esta_libre())

alumno_juampablo.elegir_dieta("vegetariano")

print(alumno_juampablo.dieta)

alumno_martino.es_vegetariano

print(alumno_martino.dieta)

alumno_martino.mentoria(profe_elio)

print(alumno_martino.mentor)




import ipdb; ipdb.set_trace()
