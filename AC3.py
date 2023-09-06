#Exercício1
def exercicio_1(salario):
    if salario <= 280:
        percentual = 20
    elif salario <= 700:
        percentual = 15
    elif salario <= 1500:
        percentual = 10
    else:
        percentual = 5
    aumento = (salario * percentual) / 100

    print(salario)
    print(percentual)
    print(aumento)
    print(salario + aumento)

#Exercício2


def exercicio_2(dia):
    match dia:
        case 1:
            print("Domingo")
        case 2:
            print("Segunda-Feira")
        case 3:
            print("Terça-Feira")
        case 4:
            print("Quarta-Feira")
        case 5:
            print("Quinta-Feira")
        case 6:
            print("Sexta-Feira")
        case 7:
            print("Sábado")
        case _:
            print("Valor inválido")

#Exercício3


def exercicio_3(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    result_1 = (-b + (delta ** 0.5)) / (2 * a)
    result_2 = (-b - (delta ** 0.5)) / (2 * a)

    if a == 0:
        print("não é de segundo grau")
    elif delta < 0:
        print("não possui raizes reais")
    elif delta == 0:
        print(f"possui apenas uma raiz: {result_1}")
    else:
        print(f"possui duas raizes: {result_1} ; {result_2}")


