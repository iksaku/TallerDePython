mandado = ['leche', 'limones', 'pan', 'tortillas']
mandado.append('refrescos')
'''print(mandado)

primerElemento = mandado.pop()
print(primerElemento)
print(mandado)

print(len(mandado))'''

'''
mandado.reverse()
for elemento in mandado:
    print(elemento)
'''

'''lista = ["Rojo", "Azul", "Verde", "Amarillo", "Naranja"]
print(lista[3] + lista[1])'''

'''personas = [
    ["Jorge", 19],
    ["Hiram", 20],
    ["David", 22]
]
for p in personas:
    print(p[0] + " tiene " + str(p[1]))'''

personas = {
    1838276: "Hiram",
    1523527: "David",
    1808932: "Liliana",
    1889169: "Jorge"
}

for matricula, nombre in personas.items():
    print(str(matricula) + " pertenece a " + nombre)

for matricula in personas.keys():
    print(matricula)

for nombre in personas.values():
    print(nombre)

#####
import operator
print(sorted(personas.items(), key=operator.itemgetter(1)))
