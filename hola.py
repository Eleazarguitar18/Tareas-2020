"""
print("hola mundo")
import math
x=45.78456
n=math.ceil(x)
print(x)
print(n)
"""
x=2.5
y=2.3
r=round((x-y),2)
uso=r*2
print(uso)

#################
"""
recuperacion=0
casteado=math.ceil(recuperacion)
tiempotranscurrido=0
while casteado != a:
    r=round((x-y),2)
    apro=round(r,2)
    #print(r)
    recuperacion=round((recuperacion + apro),2) 
    tiempotranscurrido=tiempotranscurrido+1
    print(recuperacion)
    print(tiempotranscurrido)
"""
# alternativa del ejercicio de targerta inteligente
"""
import math
x=float(input("Pasaje sin targeta:  "))
y=float(input("Pasaje con targeta:  "))
a=float(input("inserta el precio de la targeta: "))
b=float(input("carga inicial de la targeta:  "))
if(x<=y):
    print("no se recupera")
else:
    recuperacion=0
    tiempotranscurrido=1
    r=0
    while recuperacion < a:
        diferencia=round((x-y),2)
        r=round((r+diferencia),2)
        print(diferencia)
        print(r)
        recuperacion=round((recuperacion+r),2)
        print("acumulo; ",recuperacion, "en el dia", tiempotranscurrido)
        tiempotranscurrido=tiempotranscurrido+1
    print(" se acumulo: ",recuperacion)
    print("en un tiempo de: ",tiempotranscurrido)

"""