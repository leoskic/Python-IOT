from alumno import Alumno
from listaObjetos import ListaObjetos


class Grupo(ListaObjetos):
    def __init__(self, grado=None, seccion=None, alumnos=None):
        if grado is None and seccion is None and alumnos is None:
            
            self.grupos = ListaObjetos()
            
        else:
            self.grado = grado
            self.seccion = seccion
            self.alumnos = alumnos
    
    def __str__(self):
        if hasattr(self, 'grupos'):
            self.grupos.__str__()
        else: 
            return f"{self.grado}, {self.seccion}, {self.alumnos.__str__()}"

    def get_gpo(self):
        return f"Grado: {self.grado}, Seccion: {self.seccion}, Alumno:"
        
        
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
    
    grupo2 = Grupo("1", "a", alumnolista2)
    
    grupolista = Grupo()
    
    grupolista.grupos.agregar_objeto(grup1)
    grupolista.grupos.agregar_objeto(grupo2)
    
    
    print(grup1)
    #print(grupolista.grupos.__str__())



