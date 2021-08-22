def main():
    #escribe tu código abajo de esta línea
    x=int(input('Ingresa la medida del lado 1: '))
    y=int(input('Ingresa la medida del lado 2: '))
    z=int(input('Ingresa la medida del lado 3: '))
    
    if (x>0 and y>0 and z>0) and (x+y>z and x+z>y and z+y>x):
        if x==y and y==z:
            print('ES UN TRIANGULO EQUILATERO')
        elif x==y or x==z or z==y:
            print('ES UN TRIANGULO ISOSCELES')
        else:
            print('ES UN TRIANGULO ESCALENO')
    else:
        print('NO ES TRIANGULO')

if __name__=='__main__':
    main()
