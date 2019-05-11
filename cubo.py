def reverso(alg):
    alg_reverse = alg.split(" ")
    return alg_reverse

algoritmo = str(input("Cole o Algoritmo: "));

saida = reverso(algoritmo)

for move in saida:
    print(move)
