from grupo import Grupo
from alumno import Alumno
from listaObjetos import ListaObjetos

class Carrera(ListaObjetos):
    def __init__(self, nombre=None, clave=None, grupos=None):
        if nombre is None and clave is None and grupos is None:
            self.carreras = ListaObjetos()
        else:
            self.nombre = nombre
            self.clave = clave
            self.grupos = grupos
        
    def __str__(self):
        if hasattr(self, 'carreras'):
            return self.carreras.__str__()
        else:
            return f"{self.nombre}, {self.clave}, {self.grupos.__str__()}"
  
if __name__ == "__main__":

    alumno1 = Alumno("Javier", "Armando", "Garcia", "CURP001", "001")
    alumno2 = Alumno("Roberto", "Cedillo", "Marquez", "CURP002", "002")
    alumno3 = Alumno("Octavi", "Paz", "Olive", "CURP003", "003")
    
    alumnolista = Alumno()
    alumnolista2 = Alumno()
    
    alumnolista.alumnos.agregar_objeto(alumno1)
    alumnolista.alumnos.agregar_objeto(alumno2)
    alumnolista2.alumnos.agregar_objeto(alumno3)
    
    grup1 = Grupo("5", "c", alumnolista)
    grupox = Grupo("8", "c", alumnolista)
    grupo2 = Grupo("1", "a", alumnolista2)
    
    grupolista = Grupo()
    
    grupolista.grupos.agregar_objeto(alumnolista)
    grupolista.grupos.agregar_objeto(alumnolista2)
    
    carrera1 = ("Ciencias", "001", grupolista)
    
    carreralista = Carrera()
    
    carreralista.carreras.agregar_objeto(carrera1)
    
    print(carrera1)
    #print(carreralista.carreras.__str__())
    
    
    
    
    