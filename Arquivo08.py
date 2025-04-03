print("Bem vindo ao posto ipiranga.\n")
litros=float(input("Quantos litros você abasteceu:  "))
combustivel=input("Digite g ou G para gasolina ou para etanol digite G ou g" )


valE=4.90
valG=5.80

if combustivel == "E" or combustivel== "e":
    v=valE*litros
    print(f"o valor do etanol deu {v}")
else:
    if combustivel == "G" or combustivel== "g":
        s =valG*litros
        print(f"o valor da gasolina deu {s}")



