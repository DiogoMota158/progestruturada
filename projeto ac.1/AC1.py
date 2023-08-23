a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))

delta = b**2 - (4*a*c)
resultado1 = (-b + (delta)**0.5)/(2*a)
resultado2 = (-b - (delta)**0.5)/(2*a)

print("resultado1", resultado1)
print("resultado2", resultado2)
