"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    min_max = {}
    with open("files/input/data.csv", "r") as data:
        for line in data:
            if line.strip():
                parts = line.split("\t")
                letter = parts[0]
                value = int(parts[1])
                if letter not in min_max:
                    min_max[letter] = (value, value)
                else:
                    current_min, current_max = min_max[letter]
                    min_max[letter] = (min(current_min, value), max(current_max, value))
    return sorted([(letter, max_val, min_val) for letter, (min_val, max_val) in min_max.items()])

print(pregunta_05())
