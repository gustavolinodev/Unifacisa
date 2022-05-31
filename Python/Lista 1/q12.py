nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

media = round((nota1 + nota2) / 2, 2);

if(media >= 9):
    conceito = "A"
elif(media >= 7.5 and media < 9):
    conceito ="B"
elif(media >= 6 and media < 7.5):
    conceito ="C"
elif(media >= 4 and media < 6):
    conceito = "D"
else:
    conceito ="E"

print("Sua média : %.2f e o seu conceito ficou: %s" %(media, conceito))