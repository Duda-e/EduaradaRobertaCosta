print("vamos calcular")

numeroUm = float(input("insira um número:\n"))
numeroDois = float(input("insira outro número:\n"))
operacao = (input("insira a operação desejada (+ ,- ,* ,/ ):"))

if operacao == "+":
    print(numeroUm + numeroDois)
elif operacao == "-":
    print(numeroUm - numeroDois)
elif operacao == "*":
    print(numeroUm * numeroDois)
elif operacao == "/":
    if numeroDois == 0:
        print("Não é possível dividir por zero!")
    print(numeroUm / numeroDois)