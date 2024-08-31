"""buclen for"""


def promedio_notas(alumnos_notas):
   
    if not alumnos_notas:
        return 0
    
    suma_notas = 0
    cantidad_alumnos = 0

    for nota in alumnos_notas.values():
        suma_notas += nota
        cantidad_alumnos += 1

    promedio = suma_notas / cantidad_alumnos
    return promedio

def alumno_con_mejor_nota(alumnos_notas):
    
    if not alumnos_notas:
        return None
    
    mejor_alumno = None
    mejor_nota = float('-inf')

    for alumno, nota in alumnos_notas.items():
        if nota > mejor_nota:
            mejor_nota = nota
            mejor_alumno = alumno

    return mejor_alumno

# Datos de ejemplo
alumnos_notas = {
    "Ana": 8.5,
    "Luis": 9.0,
    "Carlos": 7.5,
    "Maria": 9.5
}

# Imprimir resultados
print("Promedio de las notas:", promedio_notas(alumnos_notas))
print("Alumno con la mejor nota:", alumno_con_mejor_nota(alumnos_notas))
