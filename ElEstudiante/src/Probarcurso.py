from Curso import Curso
from Departamento import Departamento  # Asegúrate de tener esta clase definida

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