#diga quantos numeros o usuario digitou antes de digitar 0
tentativas = 0
numero = int(input("Digite um numero "))

while numero != 0:
  print("Numero invalido")
  numero = int(input("Digite novamente "))
  tentativas = tentativas + 1   
print(" você digitou ",tentativas," tentativas antes de digitar 0")
   
