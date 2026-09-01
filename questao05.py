# mostre numeros positivos negativos zeros e faca uma soma entre 10 entradas disso
soma = 0
zero = 0
positivos = 0
negativos = 0
for etapa in range(1,9):
 numero = int(input("Digite um número: "))
 soma = soma + numero 
 if numero >= 1:
   positivos = positivos + 1
 elif numero <= -1:
    negativos = negativos + 1 
 else:
    zero = zero + 1
print("  você escreveu numeros positivos ",positivos," vezes")
print("  você escreveu numeros negativos ",negativos," vezes")
print(" você escreveu 0 ",zero," vezes")
print("soma dos numeros é: ", soma)

soma = 0
for etapa in range(1,9):
    numero = int(input("Digite um número: "))
    soma = soma + numero
print("soma dos numeros é: ", soma)