import csv
import json

# Función para eliminar el BOM de un archivo
def eliminar_bom(texto):
    if texto.startswith(u'\ufeff'):
        return texto[1:]
    else:
        return texto

# Abrir un archivo en modo escritura para JSONL
with open('prueba.jsonl', 'w', encoding='utf-8') as jsonlfile:

    # Leer el archivo CSV y eliminar el BOM
    with open('prueba.csv', 'r', newline='', encoding='utf-8') as csvfile:
        contenido = eliminar_bom(csvfile.read())
        csvreader = csv.DictReader(contenido.splitlines())
        
        for row in csvreader:
            prompt = row['prompt']
            completion = row['completion']
            
            # Crear un diccionario por cada par de prompt y completion
            data = {"prompt": prompt, "completion": completion}
            
            # Escribir el diccionario como una línea JSON en el archivo JSONL
            jsonlfile.write(json.dumps(data, ensure_ascii=False) + '\n')

print("Archivo JSONL 'prueba.jsonl' generado correctamente.")
