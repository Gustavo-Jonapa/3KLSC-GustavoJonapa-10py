def sumaRecursiva(Numero):
    if (Numero <= 9):
        return Numero
    else:
        return sumaRecursiva(Numero // 10) + Numero % 10

def sumaIterativa(Numero):
    suma = 0
    while Numero > 9:
        suma += Numero % 10
        Numero //= 10
    return Numero + suma

NumIng = int(input("Ingresar el numero: "))

print(f"\nResultado de la suma recursiva es: {sumaRecursiva(NumIng)}")
print(f"\nResultado de la suma iterativa es: {sumaIterativa(NumIng)}")
