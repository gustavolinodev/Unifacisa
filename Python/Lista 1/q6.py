salario = float(input("Digite o seu salário: "));

reajuste = salario * (10/100);
novoSalario = salario + reajuste;

print("Seu novo salário após o reajuste da inflação é: R$ %.2f" %(novoSalario))