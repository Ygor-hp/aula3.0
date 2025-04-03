print("Bem vindo ao posto ipiranga.\n")
l=float(input("Quantos litros você abasteceu:  "))
q=input("Qual foi o tipo de combustivel,"
        "se foi Etanol digite etanol se foi Gasolina digite gasolina: ")

E=4.90
G=5.80

if q == "etanol":
    v=E*l
    print(f"o valor do etanol deu {v}")
elif q == "gasolina":
    s =G*l
    print(f"o valor da gasolina deu {s}")



