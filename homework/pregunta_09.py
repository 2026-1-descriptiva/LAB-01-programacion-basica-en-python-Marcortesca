"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    with open('files/input/data.csv', 'r') as file:
        lines = file.readlines()

    key_counts = {}

    for line in lines:
        columns = line.strip().split('\t')
        dict_str = columns[4]
        pairs = dict_str.split(',')
        for pair in pairs:
            key, _ = pair.split(':')
            if key not in key_counts:
                key_counts[key] = 0
            key_counts[key] += 1

    return dict(sorted(key_counts.items()))

print(pregunta_09())
