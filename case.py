#mediate un menu de seleccion de un usuario 
#eligira 1 suma 2 resta , 3multiplicacion , 4 divion de 2 numenros que elija el usuario
print("seleccione una opcion")
print("1.- suma")
print("2.- resata")
print("3.- multiplicacion")
print("4.- division")
o=int(input())
print("introduzca dos numeros: ")
a=int(input())
b=int(input())
if(o==1):
    r=a+b
elif(o==2):
    r=a-b 
elif(o==3):
    r=a*b 
elif(o==4):
    if(b==0):
        print("Nose puede hacer la division entre 0: ")
    else:
        r=a//b
print("el resulatado es", r)
