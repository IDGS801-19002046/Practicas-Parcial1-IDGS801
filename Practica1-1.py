class piramide:
    num=0

    def impr(self, num):
        i = 1
        while i <= num:
            print('*' * i)
            i += 1

def main():
    obj = piramide()
    num = int(input("Ingresar un numero entero para la piramide: "))
    obj.impr(num)


if __name__ == "__main__":
    main()
    
    
    