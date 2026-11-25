import json
with open('docs_practica/cap31/api_ejemplo.json', encoding='utf-8') as f:
    data = json.load(f)
print('Nombre:', data.get('name', 'N/A'))
print('Rama:', data.get('default_branch', 'N/A'))
print('Visibilidad:', data.get('visibility', 'N/A'))
print('Licencia opcional:', data.get('license', 'No especificada'))
