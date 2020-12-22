a=int(input())
b=int(input())
mod=a%b
print(mod)

num=int(input("ingrese un numero mayor que 2 :  "))
if(num>2):
    contador=0
    i=2
    while i<num and contador==0:
        resto=num%i
        if resto==0:
            contador+=1
        i+=1
    if contador==0:
        print("el numero ", num," es primo")
    else:
        print(("el numero ", num," no es primo"))