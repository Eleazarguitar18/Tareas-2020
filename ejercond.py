"""
n=int(input())
if(n>0):
    if(n%2==0):
        print("el numero es par positivo")
    else:
        print("el numero es impar positivo")
elif(n<0):
    if(n%2==0):
        print("el numero es par negativo")
    else:
        print("el numero es impar negativo")
"""
"""
print("que desea calcualar")
print("1.- area del rectangulo")
print("2.- area del triangulo")
print("3.- area de ambos ")
a=int(input())
if(a==1):
    h=9
    b=6
    area=h*b
    print(area)
elif(a==2):
    h=9
    b=6
    area2=(h*b)/2
    print(area2)
elif(a==3):
    h=9
    b=6
    area=h*b
    h=9
    b=6
    area2=(h*b)/2
    print(area2)
    print(area)
"""
print("introduzca los datos para calcualar")
print("introduzca la altura por favor")
h=int(input())
print("introduzca la base por favor")
b=int(input())
print("¿que desea calcular? eliga una opcion porfavor: ")
print("1.- area del rectangulo")
print("2.- area del triangulo")
print("3.- area de ambos ")
a=int(input())
if(a==1):
    area=h*b
    print("el area del rectangulo es ", area)
elif(a==2):
    area2=(h*b)/2
    print("el area del triangulo es", area2)
elif(a==3):
    area=h*b
    area2=(h*b)/2
    print("el area del rectangulo es", area)
    print("el area del triangulo es", area2)
else:
    print("la opcion que elegiste no es correcta, revisa tu escritura porfavor puede que hayas insertado algo fuera de las opciones ")
