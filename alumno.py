from listaObjetos import ListaObjetos

class Alumno(ListaObjetos) :
    def __init__(self, nombre=None, apat=None, amat=None, curp=None, matricula=None):
        if nombre is None and apat is None and amat is None and curp is None and matricula is None:
            
            self.alumnos = ListaObjetos()
            
        else:
            self.nombre = nombre
            self.apat = apat
            self.amat = amat
            self.curp = curp
            self.matricula = matricula
                

    def __str__(self):
        if hasattr(self, 'alumnos'):
            return self.alumnos.__str__()
        else:
            return f"{self.nombre}, {self.apat}, {self.matricula}"

if __name__ == "__main__":

    alumno = Alumno("Javier", "Armando", "Garcia", "CURP001", "001")
    alumno2 = Alumno("Roberto", "Cedillo", "Marquez", "CURP002", "002")

    #print(alumno1)

    AlumnoLista = Alumno()

    AlumnoLista.alumnos.agregar_objeto(alumno)
    AlumnoLista.alumnos.agregar_objeto(alumno2)

    print(AlumnoLista.alumnos.listar_objetos())