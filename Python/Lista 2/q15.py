qto_hora = float(input("Quanto você ganha por hora: "))
horas_mes = float(input("Quantas horas você trabalhou por mês? "))
bruto = round(qto_hora * horas_mes, 2);

print("Salário Bruto : R$ ", bruto)

#calculo do INSS 8%
inss = bruto * (8/100);

#calculo do sindicato 5%
sindicato = bruto * (5/100);

#calculo do IR 11%
ir = bruto * (11/100);

#descontos totais
descontos = sindicato + ir + inss
liquido = bruto - descontos

print("IR (11%%) : R$ ", round(ir, 2))
print("INSS (8%%) : R$ ", round(inss, 2))
print("Sindicato (5%%) : R$", round(sindicato, 2))
print("Salário Liquido: R$ ", round(liquido, 2))
