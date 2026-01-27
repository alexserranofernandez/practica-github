#Te piden realizar un programa en que gestionen la media y la mediana de varias de tres 
#asignaturas de legua: catalán, inglés y castellano. Una vez introducidos varios registros el 
#programa debe mostrar la media y mediana los todos los alumnos introducidos 
notas_ingles = []
notas_castellano = []
notas_catalan = []
continuar = "s"
while continuar == "s":
# Pido los datos del estudiante
    nombre = input("Introduce estudiante: ")
    ingles = float(input("Nota inglés: "))
    castellano = float(input("Nota castellano: "))
    catalan = float(input("Nota catalán: "))
# Pido las notas a las listas
    notas_ingles.append(ingles)
    notas_castellano.append(castellano)
    notas_catalan.append(catalan)
    
# Pregunto si desea introducir otro alumno
    continuar = input("Deseas introducir otro alumno s/n: ")

# Ordeno las listas para mostrarlas y calcular la mediana
notas_ingles.sort()
notas_castellano.sort()
notas_catalan.sort()

# Muestro las listas ordenadas
print(f"Inglés: {notas_ingles}")
print(f"Castellano: {notas_castellano}")
print(f"Catalán: {notas_catalan}")

# Calculo las medias
media_ingles = sum(notas_ingles) / len(notas_ingles)
media_castellano = sum(notas_castellano) / len(notas_castellano)
media_catalan = sum(notas_catalan) / len(notas_catalan)

# Muestro las medias
print(f"La media en inglés es: {round(media_ingles, 1)}")
print(f"La media en castellano es: {round(media_castellano, 1)}")
print(f"La media en catalán es: {round(media_catalan, 1)}")
# num_estudiantes es igual para todas las asignaturas
num_estudiantes = len(notas_ingles)

# Mediana de inglés
if num_estudiantes % 2 == 0:
    mediana_ingles = (notas_ingles[num_estudiantes // 2 - 1] + notas_ingles[num_estudiantes // 2]) / 2
else:
    mediana_ingles = notas_ingles[num_estudiantes // 2]

# Mediana de castellano
if num_estudiantes % 2 == 0:
    mediana_castellano = (notas_castellano[num_estudiantes // 2 - 1] + notas_castellano[num_estudiantes // 2]) / 2
else:
    mediana_castellano = notas_castellano[num_estudiantes // 2]

# Mediana de catalán
if num_estudiantes % 2 == 0:
    mediana_catalan = (notas_catalan[num_estudiantes // 2 - 1] + notas_catalan[num_estudiantes // 2]) / 2
else:
    mediana_catalan = notas_catalan[num_estudiantes // 2]

# Muestro las medianas
print(f"La mediana en inglés es: {mediana_ingles}")
print(f"La mediana en castellano es: {mediana_castellano}")
print(f"La mediana en catalán es: {mediana_catalan}")
