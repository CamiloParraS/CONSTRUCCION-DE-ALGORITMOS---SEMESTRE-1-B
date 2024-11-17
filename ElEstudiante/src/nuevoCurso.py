import array as arr
from Departamento import Departamento

class Curso:
    
    # -----------------------------------------------------------------
    # Constantes
    # -----------------------------------------------------------------
    MINIMA = 1.5  # Nota mínima
    MAXIMA = 5.0  # Nota máxima
    
    # -----------------------------------------------------------------
    # Constructor
    # -----------------------------------------------------------------
    def __init__(self, codigo: str, nombre: str, creditos: int, departamento: Departamento):
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos
        self.departamento = departamento
        self.notas = [1, 2, 3, 4]
        self.nota = 0.0  # Initialize self.nota

    # -----------------------------------------------------------------
    # Métodos
    # -----------------------------------------------------------------
    def dar_codigo(self) -> str:
        return self.codigo

    def dar_nombre(self) -> str:
        return self.nombre
    
    def dar_creditos(self) -> int:
        return self.creditos

    def dar_nota(self) -> float:
        return self.nota

    def dar_departamento(self) -> Departamento:
        return self.departamento

    def asignar_nota(self, nueva_nota: float):
        if self.MINIMA <= nueva_nota <= self.MAXIMA:
            self.nota = nueva_nota
        else:
            raise ValueError(f'La nota debe estar entre {self.MINIMA} y {self.MAXIMA}.')

    def esta_calificado(self) -> bool:
        return self.nota != 0.0
    
    def calcular_promedio(self) -> float:
        if not self.notas:  # Handle empty list
            return 0.0
        suma = sum(self.notas)
        return suma / len(self.notas)
    
    def numero_aprobados(self) -> int:
        return sum(1 for nota in self.notas if nota >= self.MINIMA)
    
    def mayorPromedio(self) -> int:
        promedio = self.calcular_promedio()
        return sum(1 for nota in self.notas if nota > promedio)
    
    def menorPromedio(self) -> int:
        promedio = self.calcular_promedio()
        return sum(1 for nota in self.notas if nota < promedio)

    def notaMaxima(self) -> float:
        return max(self.notas) if self.notas else 0.0  # Handle empty list
    
    def notaMinima(self) -> float:
        return min(self.notas) if self.notas else 0.0  # Handle empty list
    
    def haceCurva(self):
        porcentaje = 0.05  # 5%
        return [nota + (nota * porcentaje) for nota in self.notas]
    
    def haceCurvaAlterna(self):
        for i in range(len(self.notas)):
            if self.notas[i] <= 2.0:
                self.notas[i] *= 1.1

    def cambiarNotas(self):
        for i in range(len(self.notas)):
            if self.notas[i] >= 4:
                self.notas[i] -= 0.5
            elif self.notas[i] <= 2:
                self.notas[i] += 0.5
    
    def darMenorNota(self) -> float:
        return min(self.notas) if self.notas else 0.0  # Handle empty list
    
    def darRangoConMasNotas(self) -> int:
        rango1 = rango2 = rango3 = 0
        for nota in self.notas:
            if 0.0 <= nota <= 1.99:
                rango1 += 1
            elif 2.0 <= nota <= 3.49:
                rango2 += 1
            elif 3.5 <= nota <= 5.0:
                rango3 += 1
        
        # Determine which range has the most notes
        if rango1 >= rango2 and rango1 >= rango3:
            return 1
        elif rango2 >= rango1 and rango2 >= rango3:
            return 2
        else:
            return 3
        

#-------------------------------------------------------------------------------------------------------------------------
# Test script
def main():
    # Create a Departamento instance
    departamento = Departamento("Matemáticas")

    # Create a Curso instance
    curso = Curso(codigo="MAT101", nombre="Matemáticas Básicas", creditos=3, departamento=departamento)

    # Assign some grades
    curso.notas = [4.0, 3.5, 2.0, 1.5, 5.0, 4.2, 3.0, 2.5]

    # Test the methods
    print("Código del curso:", curso.dar_codigo())
    print("Nombre del curso:", curso.dar_nombre())
    print("Créditos del curso:", curso.dar_creditos())
    print("Departamento del curso:", curso.dar_departamento().nombre)

    # Assign a new grade
    curso.asignar_nota(4.5)
    print("Nota asignada:", curso.dar_nota())

    # Check if the course is graded
    print("¿Está calificado?", curso.esta_calificado())

    # Calculate average
    print("Promedio de notas:", curso.calcular_promedio())

    # Number of approved grades
    print("Número de aprobados:", curso.numero_aprobados())

    # Number of students above average
    print("Estudiantes con nota mayor al promedio:", curso.mayorPromedio())

    # Number of students below average
    print("Estudiantes con nota menor al promedio:", curso.menorPromedio())

    # Maximum and minimum grades
    print("Nota máxima:", curso.notaMaxima())
    print("Nota mínima:", curso.notaMinima())

    # Apply curve
    notas_curvadas = curso.haceCurva()
    print("Notas después de aplicar curva:", notas_curvadas)

    # Apply alternate curve
    curso.haceCurvaAlterna()
    print("Notas después de aplicar curva alterna:", curso.notas)

    # Change grades
    curso.cambiarNotas()
    print("Notas después de cambiar:", curso.notas)

    # Get the lowest grade
    print("Menor nota:", curso.darMenorNota())

    # Get the range with the most notes
    print("Rango con más notas:", curso.darRangoConMasNotas())

if __name__ == "__main__":
    main()