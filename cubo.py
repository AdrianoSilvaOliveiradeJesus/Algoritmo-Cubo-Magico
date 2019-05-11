# Importando  biblioteca do sistema
import sys
#Importando Objeto 'Algoritmos' que contém todas as OLL's e PLL's
from algoritmos import Algoritmos

#Função que deixa o algorimo ao contrário
def reverso(alg):
    #alg é o argumento com o algoritmo ainda normal
    #separa o algoritmo por espaço
    alg_reverse = alg.split(" ")
    #retorna uma lista com os movimentos ja invertidos
    return alg_reverse

#variavel com uma lista dos argumento do sistema
argumentos = sys.argv

#instânciando objeto Algoritmos
algoritmos = Algoritmos()

if(argumentos[1] == "OLL"):
    try:
        if(argumentos[2] == "-R"):
            print("Algoritmo Reverso")
    except Exception as e:
        print("OLL")

elif(argumentos[1] == "PLL"):
    try:
        if(argumentos[2] == "-R"):
            print("Algoritmo Reverso")
    except Exception as e:
        print(algoritmos.PLL[argumentos[2]])


saida = reverso("Adriano")

for move in saida:
    print(move)
