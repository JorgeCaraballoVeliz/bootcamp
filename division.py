def dividir(a, b):
    if b == 0:
        return "División inválida, por favor, ingrese otros parámetros"
    return a / b

if __name__ == "__main__":
    print(dividir(6, 3))