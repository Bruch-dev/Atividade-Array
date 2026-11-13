#3- Em uma cidade do interior, sabe-se que de janeiro a abril de 1976 (121 dias) não ocorreu 
# temperatura inferior a 15o C e nem superior a 40o C. Fazer um programa JS que determine: 
#a) A menor temperatura ocorrida 
#b) A maior temperatura ocorrida 
#c) A temperatura média do período  

dias = 0
maiorT = 0
menorT = 460
tempT = 0

while dias < 10:
    dias += 1

    temp = float(input("Digite a temperatura de hoje: "))
    tempT += temp

    if temp < 150 or temp > 400:
        dias -= 1
        continue

        

    if temp > maiorT:
        maiorT = temp

    if dias == 1:
        menorT = temp

    elif temp < menorT:
        menorT = temp

tempM = tempT / dias

print("A maior temperatura registrada é de", maiorT, "graus celcius")
print("A menor temperatura registrada é de", menorT, "graus celcius")
print("A temperatura média é de", tempM, "graus celcius")