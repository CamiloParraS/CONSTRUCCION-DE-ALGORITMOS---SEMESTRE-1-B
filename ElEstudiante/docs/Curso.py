# aun no se cual usar, por eso hay 2 cursos

import array as arr
from docs.Departamento import Departamento

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
        self.notas = [1, 2, 3, 4,]

    # -----------------------------------------------------------------
    # Métodos
    # -----------------------------------------------------------------
    # Retorna el codigo del curso
    def dar_codigo(self) -> str:
        return self.codigo

    # Retorna el nombre del curso
    def dar_nombre(self) -> str:
        return self.nombre
    
    # Retorna el numero de creditosde curso
    def dar_creditos(self) -> int:
        return self.creditos

    #  Retorna el departamento del curso
    def dar_nota(self) -> float:
        return self.notas

    #  Retorna el departamento del curso
    def dar_departamento(self) -> Departamento:
        return self.departamento

    # Asigna la nota dada por el parametro
    # :param nueva_nota: Nueva nota del curso. Debe estar entre 1.5 y 5.0.
    def asignar_nota(self, nueva_nota: float):
        if self.MINIMA <= nueva_nota <= self.MAXIMA:
            self.nota = nueva_nota
        else:
            raise ValueError(f'La nota debe estar entre {self.MINIMA} y {self.MAXIMA}.')

    # Indica si el curso ya ha sido calificado 
    def esta_calificado(self) -> bool:
        return self.nota != 0.0
    
#-------------------------------------------------------------------------------------------------------
# Tarea 
#-----------------------------------------------------------------------------------------------------

# Calcular el promedio de el curso 
    def  calcular_promedio(self) -> float:
        suma = 0.0
        indice =0 
        while indice < len(self.notas):
            suma += self.notas[indice]
            indice += 1
        return  suma / len(self.notas)
    
# Numero Aprobados
    def numero_aprobados(self) -> int:
        aprobados = 0
        indice = 0
        while indice < len(self.notas):
            aprobados += (self.notas[indice] >= self.MINIMA)
            indice += 1  
        return aprobados  
    
# Estudiantes enciam de el Promedio
    def mayorPromedio(self):
        promedio = self.calcular_promedio()
        Mayor = 0
        indice = 0
        while indice < len(self.notas):
            if self.notas[indice] > promedio:
                Mayor += 1
            indice += 1
        return Mayor
    
# Estudiantes Menor que el promedio
    def mayorPromedio(self):
        promedio = self.calcular_promedio()
        Menor = 0
        indice = 0
        while indice < len(self.notas):
            if self.notas[indice] < promedio:
                Menor += 1
            indice += 1
        return Menor

# Nota Maxima 
    def  notaMaxima(self) -> float:
        max_nota = self.notas[0]  
        indice = 1 
        while indice < len(self.notas):  
            if self.notas[indice] > max_nota:  
                max_nota = self.notas[indice]  
        indice += 1  

# Nota Minimia 
    def  notaMinima(self) -> float:
        notaMinima = self.notas[0]  
        indice = 1  
    
        while indice < len(self.notas):  
            if self.notas[indice] < notaMinima: 
                notaMinima = self.notas[indice]  
        indice += 1  
        return notaMinima
    
# Hacer Curva 
    def haceCurva(self):
        notas_aumentadas = [] 
        index = 0  
        porcentaje = 5 # 5%
        
        while index < len(self.notas):  
            aumento = self.notas[index] * (porcentaje / 100)  
            nueva_nota = self.notas[index] + aumento 
            notas_aumentadas.append(nueva_nota)  
            index += 1  

        return notas_aumentadas
    

#def jaaaa(self):
#    for nota in self.notas:
#        print(f'7 x [i] = 7 * i')

def evenjaaa(self):
    range = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    for i in range(0, 11 , 2):
        print (f'7 * {i} = {7 * i}')
        if (i * 7) % 2 == 0:
            print (f"{i} es par ")

evenjaaa()