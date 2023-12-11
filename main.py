import json

try:
    with open('gramatas.json', 'r', encoding='utf8') as file:
        data = json.load(file)
except FileNotFoundError:
    print('files netika atrasts')
except json.JSONDecoder:
    print('files nav json formata')

print(f'Kopējais grāmatu skaits: {len(data)}')
autors = input('Nosauciet autora vārdu un uzvārdu: ')
gramatas_autors = [gramata for gramata in data if gramata['autors'] == autors]
if gramatas_autors:
    print('Autora izdotas grāmats nosaukums un izdošanas gads:')
    for gramata in gramatas_autors:
        print(gramata['nosaukums'], gramata['izdošanas_gads'])
else:
    print(f'{autors} grāmatas netika atrastas.')

print()

zanrs_skaits = {}
for gramata in data:
    zanrs = gramata['žanrs']
    zanrs_skaits[zanrs] = zanrs_skaits.get(zanrs, 0) + 1
print('Grāmatas žanrs un to skaits:')
for zanrs, skaits in zanrs_skaits.items():
    print(f'{zanrs}: {skaits} grāmatas')
