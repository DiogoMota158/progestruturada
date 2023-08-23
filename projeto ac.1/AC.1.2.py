ano = int(input("Ano: "))

Resultado = (ano % 4 == 0 and ano % 100 !=0) or (ano %400 == 0)

print(Resultado)