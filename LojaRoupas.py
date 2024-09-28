#O usuário informa o valor total da compra, a forma de pagamento e o numero de parcelas.
#Ao final o programa mostra o valor final.

# Definindo descontos e juros
forma_pagamento = "a vista":
valor_compra > 1000:
desconto = 0.20
elif valor_compra > 500:
desconto = 0.15
else:
desconto = 0.10
valor_final = valor_compra * (1
desconto)
elif forma_pagamento = "a prazo":
numero_parcelas <= 5:
valor_final = valor_compra
elif valor_compra < 800:
return "Parcelas acima de 5x apenas para compras acima de R$ 800."

# Aplicando juros para parcelamento acima de 10x
numero_parcelas > 10:
juros = {
11: 0.05,
12: 0.065,
13: 0.07,
14: 0.09,
15: 0.095,
16: 0.10,
17: 0.113,
18: 0.12
}
numero_parcelas in juros:
valor_final = valor_compra * (1 + juros[numero_parcelas]) ** numero_parcelas
else:
return "Número de parcelas não suportado."
else:
valor_final = valor_compra
else:
return "Forma de pagamento inválida."
return valor_final

# Solicitando informações ao usuário
valor_compra = float(input("Informe o valor total da compra: R$ "))
forma_pagamento = input("Informe a forma de pagamento (a vista ou a prazo): ").strip().lower()
numero_parcelas = int(input("Informe o número de parcelas (1 a 18): "))

# Calculando o valor final
valor_final = calcular_valor_final(valor_compra, forma_pagamento, numero_parcelas)

# Exibindo o resultado
isinstance(valor_final, str):
print(valor_final) # Mensagem de erro
else:
print(f"O valor final da venda é: R$ {valor_final:.2f}"