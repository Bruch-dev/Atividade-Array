#2- Faça um programa em Py que leia um vetor de seis elementos numéricos inteiros, calcule e mostre: 
#a) A quantidade de números pares 
#b) Quais os números pares 
#c) A quantidade de números ímpares 
#d) Quais os números ímpares

nPares = []
qntP = 0
qntI = 0
nImpares = []

for i in range(6):

    num = (int(input("Digite um número inteiro: ")))

    if num % 2 == 0:
        nPares.append(num)
        qntP += 1

    else:
        nImpares.append(num)
        qntI += 1

print("A quantidade de números par(es) é de", qntP)
print("Os número(s) é(são)", nPares)
print("A quantidade de números par(es) é de", qntI)
print("Os número(s) é(são)", nImpares)