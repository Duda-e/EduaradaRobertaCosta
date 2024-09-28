#Lista de reserva de Voos

nomes = []
destinos = []
continua = "sim"

while continua == "sim":

    nome = input("Digite um nome: ")
    nomes.append(nome) 

    destino = input("Digite o seu destino:")
    destinos.append(destino)

    continua = input("Deseja continuar? (sim/não): ")
   
for nome in nomes:
    print ("-"*30)
    print (f"Lista de reserva de Voos")
    print (f"Nome: {nome}")
    print (f"Destino: {destino}")
    
