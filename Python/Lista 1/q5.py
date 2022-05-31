valor = float(input("Digite o valor do produto: "))

dez = valor * (10/100);
vinte = valor * (20/100);
cinquenta = valor * (50/100);

print("O valor do seu produto com 10%% de desconto é: %.2f" %(valor -dez))
print("O valor do seu produto com 20%% de desconto é: %.2f" %(valor -vinte))
print("O valor do seu produto com 50%% de desconto é: %.2f" %(valor -cinquenta))