class Lista:
    def __init__(self):
        self.nums = []

    def pedirnum(self, cantidad):
        for _ in range(cantidad):
            numero = int(input("Ingrese un numero: "))
            self.nums.append(numero)

    def orden(self):
        self.nums.sort()

    def imprparimp(self):
        resultado = {'pares': [], 'impares': [], 'problemas': []}

        for num in self.nums:
            if num % 2 == 0:
                resultado['pares'].append(num)
            elif num % 2 != 0:
                resultado['impares'].append(num)
            else:
                resultado['problemas'].append(num)

        if resultado['pares']:
            print("Los numeros Pares son: ", resultado['pares'])
        else:
            print("No hay números pares.")

        if resultado['impares']:
            print("Los numeros Impares son: ", resultado['impares'])
        else:
            print("No hay números impares.")

        if resultado['problemas']:
            print(f"Problemas en los datos: {resultado['problemas']}")

    def mostrep(self):
        repetidos = {}
        for num in self.nums:
            if num in repetidos:
                repetidos[num] += 1
            else:
                repetidos[num] = 1

        repetidos_filtrados = {num: c for num, c in repetidos.items() if c > 1}

        if repetidos_filtrados:
            print("Los Números repetidos son:")
            for num, c in repetidos_filtrados.items():
                print(f"Se repite el numero {num} -> {c} veces")
        else:
            print("No hay números repetidos.")

def main():
    cantnums = int(input("Cuantos numeros desea agregar a la lista: "))
    obj = Lista()
    obj.pedirnum(cantnums)
    obj.orden()
    print("\nLos numeros en Orden son:")
    print(obj.nums)
    obj.imprparimp()
    obj.mostrep()

if __name__ == "__main__":
    main()