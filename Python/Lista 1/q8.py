nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

media = round((nota1 + nota2) / 2, 2);

if(media < 7):
    print("Você foi Reprovado")
elif(media >= 7 and media < 10):
    print("Você foi Aprovado")
else:
    print("Você foi aprovado com Distinção")