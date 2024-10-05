print("Vamos descobri sua nota:\n")
nota = int(input("inserira uma nota de 0 a 100:"))

if nota <= 60:
    print("NOTA F")
elif nota <= 69:
    print("NOTA D")
elif nota <= 79:
    print("NOTA C")
elif nota <= 89:
    print("NOTA B")
elif nota <= 100:
    print("NOTA A")
else:
    print("nota inválida")