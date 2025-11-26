import csv
import pathlib, json

def read_csv_login(file_path):
    """
    Lee un archivo CSV y devuelve una lista de tuplas
    para usar en parametrización de pytest
    """
    data = []
    path = pathlib.Path(file_path) # convierte la ruta desde la raiz, aunque fuciona igual sin hacer esto
    
    with open(path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file) # Devuelve un diccionario/json/obj
        # reader = csv.reader(file) # Devuelve un string
        
        for row in reader:
            # Convertir string 'True'/'False' a booleano
            must_work = row['must_work'].lower() == 'true'
            data.append((row['username'], row['password'], must_work, row['error_text']))
    
    return data
