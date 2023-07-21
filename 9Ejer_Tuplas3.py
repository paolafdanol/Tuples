import string

# Definimos la función para contar las frecuencias de las letras
def contar_letras(texto):
    # Convertimos el texto a minúsculas
    texto = texto.lower()
    # Creamos una lista de caracteres permitidos (sólo las letras a-z)
    letras_permitidas = set(string.ascii_lowercase)
    # Creamos un diccionario para almacenar las frecuencias
    frecuencias = {}
    # Contamos las frecuencias de las letras permitidas
    for letra in texto:
        if letra in letras_permitidas:
            if letra in frecuencias:
                frecuencias[letra] += 1
            else:
                frecuencias[letra] = 1
    # Convertimos el diccionario en una lista de tuplas y la devolvemos
    lista_frecuencias = [(letra, frecuencia) for letra, frecuencia in frecuencias.items()]
    return lista_frecuencias

# Pedimos al usuario el nombre del archivo a analizar
nombre_archivo = input("Ingresa el nombre del archivo a analizar: ")

# Leemos el archivo
with open(nombre_archivo, 'r') as archivo:
    texto = archivo.read()

# Contamos las frecuencias de las letras
frecuencias = contar_letras(texto)

# Creamos un diccionario de frecuencias
dic_frecuencias = {}
for letra, frecuencia in frecuencias:
    dic_frecuencias[letra] = frecuencia

# Ordenamos las frecuencias en orden decreciente y las imprimimos
frecuencias_ordenadas = sorted(dic_frecuencias.items(), key=lambda x: x[1], reverse=True)
for letra, frecuencia in frecuencias_ordenadas:
    print(letra, frecuencia)
