salario = float(input("Digite o seu salário atual: "))

if(salario < 280.0):
    percentual = "20"
    aumento = salario * (20/100)
elif(salario >= 280.0 and salario < 700.0):
    percentual = "15"
    aumento = salario * (15/100)
elif(salario >= 700 and salario < 1500):
    percentual = "10"
    aumento = salario * (10/100)
else:
    percentual = "5"
    aumento = salario * (5/100)

novoSalario = salario + aumento

print("Seu salário atual é: ", salario)
print("Você se encaixa no percentual de %s%% de aumento" % percentual)
print("Seu valor de aumento seguindo esse percentual é de: %.2f" %aumento)
print("Seu novo salário vai ser: %.2f" %(novoSalario))