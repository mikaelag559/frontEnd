from collections import Counter

# Ruta del archivo original
archivo_entrada = "/home/mikaela/Desktop/my_spotify_data/Spotify Account Data/YourLibrary.json"
# Ruta del archivo de salida sin duplicados
archivo_salida = "/home/mikaela/Desktop/frontEnd/Desktop.txt"

# Leer todas las líneas
with open(archivo_entrada, "r", encoding="utf-8") as f:
    lineas = [line.strip() for line in f if line.strip()]

# Contar ocurrencias
conteo = Counter(lineas)

# Filtrar las que NO están repetidas exactamente 2 veces
lineas_filtradas = [linea for linea in lineas if conteo[linea] != 2]

# Escribir resultado
with open(archivo_salida, "w", encoding="utf-8") as f:
    for linea in lineas_filtradas:
        print("Escribiendo línea:", linea)
        f.write("spotify:track:" + linea + "\n")

print("Líneas duplicadas exactamente dos veces han sido eliminadas.")
