# numeroUm = float(input("digite um numero: "))
# numeroDois = float(input("digite outro numero: "))

# soma = numeroUm + numeroDois

# print("-"*20)
# print("Resultado")
# print(f"{soma}")

lista = []

for i in range(5):
    numero = int(input("Digite cinco numeros: "))
    lista.append(numero)

soma = 0
for i in range(len(lista)):
    soma = soma + lista[i]
print(soma)

