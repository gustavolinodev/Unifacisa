from multiprocessing.connection import wait
import time


n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

print("Realizando a troca de numeros...")
time.sleep(3.0)
aux = n1;
n1 = n2;
n2 = aux;

print("O valor da primeira variável agora é: %d, e da segunda agora é: %d" %(n1,n2))
