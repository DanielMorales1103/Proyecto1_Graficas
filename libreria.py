from math import isclose
import math

def barycentricCoords(A, B, C, P):
    # Se saca el �rea de los subtri�ngulos y del tri�ngulo
    # mayor usando el Shoelace Theorem, una f�rmula que permite
    # sacar el �rea de un pol�gono de cualquier cantidad de v�rtices.

    areaPCB = abs((P[0]*C[1] + C[0]*B[1] + B[0]*P[1]) - 
                  (P[1]*C[0] + C[1]*B[0] + B[1]*P[0]))

    areaACP = abs((A[0]*C[1] + C[0]*P[1] + P[0]*A[1]) - 
                  (A[1]*C[0] + C[1]*P[0] + P[1]*A[0]))

    areaABP = abs((A[0]*B[1] + B[0]*P[1] + P[0]*A[1]) - 
                  (A[1]*B[0] + B[1]*P[0] + P[1]*A[0]))

    areaABC = abs((A[0]*B[1] + B[0]*C[1] + C[0]*A[1]) - 
                  (A[1]*B[0] + B[1]*C[0] + C[1]*A[0]))

    # Si el �rea del tri�ngulo es 0, retornar nada para
    # prevenir divisi�n por 0.
    if areaABC == 0:
        return None

    # Determinar las coordenadas baric�ntricas dividiendo el 
    # �rea de cada subtri�ngulo por el �rea del tri�ngulo mayor.
    u = areaPCB / areaABC
    v = areaACP / areaABC
    w = areaABP / areaABC

    # Si cada coordenada est� entre 0 a 1 y la suma de las tres
    # es igual a 1, entonces son v�lidas.
    if 0<=u<=1 and 0<=v<=1 and 0<=w<=1 and isclose(u+v+w, 1.0):
        return (u, v, w)
    else:
        return None

def multi4x4matrix(matrix1, matrix2):
    resultado = [
        [0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0]]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                resultado[i][j] += matrix1[i][k] * matrix2[k][j]
    return resultado

def multimatrixvec(matrix, vect):
    resultado = [0.0, 0.0, 0.0, 0.0]

    for i in range(4):
        for j in range(4):
            resultado[i] += matrix[i][j] * vect[j]

    return resultado

def cross_product(vector_a, vector_b):
    if len(vector_a) != 3 or len(vector_b) != 3:
        raise ValueError("Both vectors must be three-dimensional.")
    
    result = [0, 0, 0]
    
    result[0] = vector_a[1] * vector_b[2] - vector_a[2] * vector_b[1]
    result[1] = vector_a[2] * vector_b[0] - vector_a[0] * vector_b[2]
    result[2] = vector_a[0] * vector_b[1] - vector_a[1] * vector_b[0]
    
    return result

def dot_product(vector_a, vector_b):
    if len(vector_a) != len(vector_b):
        raise ValueError("Both vectors must have the same dimension.")
    
    result = 0
    for i in range(len(vector_a)):
        result += vector_a[i] * vector_b[i]
    
    return result

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    
    return transposed

def matrix_minor(matrix, row, col):
    return [row[:col] + row[col+1:] for row in (matrix[:row] + matrix[row+1:])]

def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    
    det = 0
    for col in range(len(matrix)):
        det += ((-1) ** col) * matrix[0][col] * determinant(matrix_minor(matrix, 0, col))
    
    return det

def matrix_inverse(matrix):
    det = determinant(matrix)
    if det == 0:
        raise ValueError("Matrix is singular, cannot compute inverse.")
    
    rows = len(matrix)
    cols = len(matrix[0])
    adjugate = [[0 for _ in range(rows)] for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            minor = matrix_minor(matrix, i, j)
            cofactor = ((-1) ** (i + j)) * determinant(minor)
            adjugate[j][i] = cofactor / det
    
    return adjugate

def vector_magnitude(vector):
    return sum(component ** 2 for component in vector) ** 0.5

def normalize_vector(vector):
    magnitude = vector_magnitude(vector)
    normalized = [component / magnitude for component in vector]
    return normalized

def vector_subtraction(vector_a, vector_b):
    if len(vector_a) != len(vector_b):
        raise ValueError("Both vectors must have the same dimension.")
    
    result = [a - b for a, b in zip(vector_a, vector_b)]
    return result

def angle_between_vectors(vector1, vector2):
    dot_prod = dot_product(vector1, vector2)
    magnitude1 = vector_magnitude(vector1)
    magnitude2 = vector_magnitude(vector2)
    
    # Manejar casos especiales para evitar divisiones por cero
    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0
    
    cos_theta = dot_prod / (magnitude1 * magnitude2)
    
    # Asegurarse de que el coseno del ángulo esté en el rango [-1, 1]
    cos_theta = max(-1.0, min(1.0, cos_theta))
    
    # Calcular el ángulo en radianes
    angle_radians = math.acos(cos_theta)
    
    # Convertir el ángulo a grados
    angle_degrees = math.degrees(angle_radians)
    
    return angle_degrees