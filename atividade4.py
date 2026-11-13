#4- Faça um programa em Py que alimente um vetor, com um número de posições definidas pelo usuário. 
# Este vetor deverá armazenar um conjunto de nomes em diferentes posições. Crie um mecanismo para 
# alimentar elementos no vetor e pesquisar por um valor existente.
# ======== MENU ======== 
#1) Cadastrar nome 
#2) Pesquisar nome 
#3) Listar todos os nome 
#0) Sair do programa 
#——————– 
#Digite sua escolha:

nom = []

while True: 
    entrada = input("Qual nome deseja registrar?(x para mostrar a tabela): ")
    
    if entrada == "x":
        break  
        
    nom.append(entrada)

print("========= MENU =========")
print("   1) Pesquisar nome")
print("2) Listar todos os nomes")

esc = int(input("Digite sua escolha: "))

if esc == 1:
    pes = input("Qual nome deseja pesquisar: ")

    if pes in nom:
        posicao = nom.index(pes)
        print("Nome registrado, está na posição", posicao + 1, ":", nom[posicao])
    else:
        print("Nome não encontrado na lista.")

elif esc == 2:
    print("Lista de nomes:", nom)
    

elif esc == 2:
    print("Aqui estão todos os nomes registrados",nom)
        

