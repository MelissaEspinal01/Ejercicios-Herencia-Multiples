#Cree el siguiente ejercicio utilizando POO . En este ejercicio debe de simular el registro de
#notas de estudiantes universitarios de la carrera de Ing. En desarrollo de software. Para
#iniciar el ejercicio tenemos que definir 3 clases (Estudiantes, materias y notas).
#El ejercicio en la clase Notas debe de agregarle las notas de laboratorio y parcial a un
#estudiante de una materia en específico. El mensaje para mostrar queda a su discreción.

class Estudiantes:
    def __init__(self, Carrera, Estudiante1, Edad1, Estudiante2, Edad2, Estudiante3, Edad3):
        self.Carrera = Carrera
        self.Estudiante1 = Estudiante1
        self.Estudiante2 = Estudiante2
        self.Estudiante3 = Estudiante3
        self.Edad1 = Edad1
        self.Edad2 = Edad2
        self.Edad3 = Edad3

    def DatosEstudiantes(self):
        return "Datos de los estudiantes universitarios de la carrera {}, Estudiante 1: {}, Su edad es: {}, Estudiante 2: {}, su edad es: {}, Estudiante 3: {}, Su edad es: {} ".format(self.Carrera, self.Estudiante1, self.Edad1, self.Estudiante2, self.Edad2, self.Estudiante3, self.Edad3)

EstudianteSoftware = Estudiantes("Ingenieria en Desarrollo de software", "Andrea", 18, "Kevin", 18, "Abigail", 19)
print(EstudianteSoftware.DatosEstudiantes())


    