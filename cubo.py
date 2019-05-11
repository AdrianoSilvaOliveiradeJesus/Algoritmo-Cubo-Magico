from algoritmos import Algoritmos

def reverso(alg):
    alg_reverse = alg.split(" ")
    return alg_reverse

algoritmos = Algoritmos()
print(algoritmos.PLL)

saida = reverso("Adriano")

for move in saida:
    print(move)
