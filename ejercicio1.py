velocidades=[0,0,0,0,0]
vuelta=0


while vuelta < 5:
    velocidades=int(input("ingrese velocidades en Km: "))
    vuelta+=1

print([velocidades])



if velocidades > 140:
    print("peligro")
if velocidades < 20:
    print("peligro")