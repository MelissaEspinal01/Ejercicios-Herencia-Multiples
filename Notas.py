from Estudiantes import Estudiantes
from Materias import Materias

class Notas:
    def __init__(self, estudiante, materia):
        self.estudiante = estudiante
        self.materia = materia
    
    def NotaLaboratorio(self, nota_laboratorio, nota_parcial):
        return "La nota del laboratorio del alumn@ {} de la materia {} es: {}, y su nota de parcial es: {}".format(self.estudiante, self.materia.Materia1, nota_laboratorio, nota_parcial)

estudiantes_carrera = Estudiantes("Ingenieria en Desarrollo de software", "Andrea", 18, "Kevin", 18, "Abigail", 19)
materias_cursadas = Materias()

estudiante1 = estudiantes_carrera.Estudiante1

notas_estudiante1 = Notas(estudiante1, materias_cursadas)
print(notas_estudiante1.NotaLaboratorio(80, 90))

