
monto=int(input("ingrese el monto: "))



edad=int(input("ingrese su edad: "))
socio=input("si/no: ")

if monto >= 10000 and socio=="si" and edad<60:
    descuento=monto*0.15
    total=monto-descuento
    print("su monto final es de un" ,total, "con un descuento del 15%, siendo socio")

if monto >= 10000 and edad>=60 and socio=="no":
    descuento=monto*0.15
    total=monto-descuento
    print("su monto final es de un" ,total, "con un descuento del 15%, siendo mayor de edad")

if monto < 10000:
    print("no se aplicó nigun descuento especial, sumonto final es de",monto,)
