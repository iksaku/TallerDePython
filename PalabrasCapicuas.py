word = input("Ingrese una palabra: ")

'''
print(word)
print(word[0])
print(word[-1])
print(word[-2])

print(word[1:4])
'''

def es_capicua(palabra):
    longitud = int(len(palabra) / 2)
    for normal in range(0, longitud):
        espejo = (normal + 1) * -1
        if palabra[normal].lower() != palabra[espejo].lower():
            return False
    
    return True

if es_capicua(word):
    print("La palabra es Capicua :D")
else:
    print("La palabra NO es Capicua :(")