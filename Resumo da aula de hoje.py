from selectors import SelectSelector

print("Diario do Aluno")
id=input("Digite o id do aluno para entrar:")
senha=input("Digite a senha do aluno para entrar:")

if id == "Elgordo.09":
    if senha =="ygor.2006":

        print("\nBEM VINDO! ALUNO\n")

        print("experiencias de primeiro momento. primeira experiencia 01\n")

        nome = str(input("Digite seu nome :"))
        idade = int(input("Digite sua idade :"))
        salario = float(input("Digite seu salario:"))
        p = float(input("o percentual de seu salario é :"))
        s = salario * p / 100
        aumemto = salario + s
        print(f"Ola {nome}.\n Sua idade é {idade} anos.\n seu salario é de {salario}.\n"
              f"seu aumento de salario foi de {s}.\nseu novo salario é {aumemto}")

        print("\nsegunda experiencia do segundo momento.segunda experiencia 02\n")
        n1 = float(input("Digite qualquer numero: "))
        n2 = float(input("Digite qualquer numero: "))

        soma = n1 + n2
        sub = n1 - n2
        mul = n1 * n2
        div = n1 / n2

        print(f"sua soma foi {soma}.\n sua subtração foi de {sub}.\n sua multiplicação foi de {mul}.\n"
              f"sua divisão foi de {div}.")

        print("\nterceira experiencia do terceiro momento. terceira experiencia 03\n")

        a = 5
        b = 10

        print(f"A:{a} e B:{b}")

        c = a
        a = b
        b = c

        print(f"A:{a} e B:{b}")

        print("\nquarta experiencia do quarto momento. quarta experiencia 04\n")

        n1 = int(input("primeiro numero:"))

        n2 = int(input("primeiro nummero:"))

        if n1 > n2:
            print(n2, n1)

        else:
            print(n1, n2)

        print("quinta experiencia do quinto momento.quinta experiencia.")

        n1 = float(input("digite a primeira nota:"))
        n2 = float(input("digite a segunda nota:"))
        n3 = float(input("digite a segunda nota:"))

        media = (n1 + n2 + n3) / 3

        print(f"sua nota foi de {media}")

        if media >= 7:
            print("você foi aprovado.")


        else:
            print("você foi reprovado.")

        print("\nsexta experiencia do sexto momemento.sexta experiencia 06\n")

        n1 = float(input("digite a primeira nota:"))
        n2 = float(input("digite a segunda nota:"))
        n3 = float(input("digite a segunda nota:"))

        media = (n1 + n2 + n3) / 3

        print(f"sua nota foi de {media}")

        if media >= 7:
            print("você foi aprovado.")

        elif media <= 4:
            print("você esta de recuperação")

        else:
            print("você foi reprovado.")

        print("\nultima atividade.\n")

        primeiro = input("primeiro time:")
        segundo = input("segundo time:")
        s1 = int(input(f"saldo de gols do {primeiro} time:"))
        s2 = int(input(f"saldo de gols do {segundo} time:"))

        print(f"o {primeiro} fez {s1}, já o {segundo} fez {s2}")

        if s1 == s2:
            print("ouve um empate dos times.")
        else:
            if s1 > s2:
                print(f"o {primeiro} ganhou do {segundo} por {s1} a {s2}.")
            else:
                print(f"o {segundo} ganhou do {primeiro} por {s2} a {s1}.")








    else:
        print("senha está errada .")





else:
 print("erro no seu id")











