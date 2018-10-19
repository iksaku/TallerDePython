def contar(numero, fin):
    if numero >= fin:
        return
    
    print(numero)
    contar(numero + 1, fin)

contar(0, 10)


# Esto es un comentario
'''
Esto también
es
un
Comentario
'''

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(0, 10):
    print(fibonacci(i))