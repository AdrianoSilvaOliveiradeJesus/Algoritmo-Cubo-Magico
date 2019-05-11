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

#Se o segundo argumento da lista é "OLL" ele cai nesse bloco
if(argumentos[1] == "OLL"):
    #argumentos[2] == referência da OLL
    #argumentos[3] == "Se o Algortimo é reverso ou não"
    try:
        #O argumento '-R' quer dizer para printar o algorimo invertido
        if(argumentos[2] == "-R"):
            print("Algoritmo Reverso")
    #Esse bloco printa na tela o algoritmo com a referência do mesmo
    except Exception as e:
        print("OLL")

#Se não,se ele for igual "PLL" Ele cai nesse bloco
elif(argumentos[1] == "PLL"):
    #argumentos[2] == referência da PLL
    #argumentos[3] == "Se o Algortimo é reverso ou não"
    try:
        #O argumento '-R' quer dizer para printar o algorimo invertido
        if(argumentos[3] == "-R"):
            saida = reverso(algoritmos.PLL[argumentos[2]])
            print(saida)
    #Esse bloco printa na tela o algoritmo com a referência do mesmo
    except Exception as e:
        saida = algoritmos.PLL[argumentos[2]]
        print(saida)
