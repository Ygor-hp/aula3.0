primeiro=input("primeiro time:")
segundo=input("segundo time:")
s1=int(input(f"saldo de gols do {primeiro} time:"))
s2=int(input(f"saldo de gols do {segundo} time:"))

print(f"o {primeiro} fez {s1}, já o {segundo} fez {s2}")

if s1 == s2:
    print("ouve um empate dos times.")
else:
    if s1>s2:
        print(f"o {primeiro} ganhou do {segundo} por {s1} a {s2}.")
    else:
        print(f"o {segundo} ganhou do {primeiro} por {s2} a {s1}.")
