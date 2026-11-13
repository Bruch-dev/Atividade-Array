#1- Faça um programa em Py que receba o total das vendas de cada vendedor e armazenadas em um vetor. 
#Receba também o percentual de comissão de cada vendedor e armazene-os em outro vetor.
#Receba os nomes desses vendedores e armazene ­os em um terceiro vetor. Existem apenas dez vendedores. 
#Calcule e mostre: 
#a) Um relatório com os nomes dos vendedores e os valores a receber; 
#b) O total das vendas de todos os vendedores; 
#c) O maior valor a receber e quem o receberá; 
#d) O menor valor a receber e quem o receberá.

nomeV = []
totalV = []
porC = []
valT = 0
maiorV = 0
menorV = None  

for i in range(10):
    nomeV.append(input("Digite o nome do vendedor: "))
    
    totalV.append(float(input("Digite o total de vendas dele: ")))
    
    porC.append(float(input("Digite a porcentagem de comissão do vendedor: ")))
    

    comissao = totalV[i] * (porC[i] / 100)
    valT += totalV[i]


    if i == 0:
        maiorV = comissao
        menorV = comissao
    else:
        if comissao > maiorV:
            maiorV = comissao
        if comissao < menorV:
            menorV = comissao


for i in range(10):
    print("O vendedor", nomeV[i], "vendeu no total", totalV[i], "reais")

print("O total de vendas de todos os vendedores é de", valT, "reais")
print("O maior valor a receber é de", maiorV, "reais")
print("O menor valor a receber é de", menorV, "reais")
