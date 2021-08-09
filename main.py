import numpy as np
import random as rd

quantidade_população = 10
produto_volumes = {0:0.751, 1:0.0000899, 2:0.400, 3:0.29,
           4:0.200, 5:0.0035, 6:0.496, 7:0.0424,
           8:0.0544, 9:0.0319, 10:0.635, 11:0.87,
           12:0.498, 13:0.527}
produto_precos = {0:999.9, 1:2199.12, 2:4346.99, 3:3999.9,
          4:2999.9, 5:2499.9, 6:199.9, 7:308.66,
          8:429.9, 9:299.29, 10:849, 11:1199.89,
          12:1999.9, 13:3999 }

def cria_individuo():
    individuo = []
    for i in range(14):
        individuo.append(rd.randint(0,1))
    return individuo

def cria_populacao():
    populacao=[]
    for i in range(quantidade_população):
        individuo = cria_individuo()
        populacao.append(individuo)
    return populacao

p = []
p = cria_populacao()

def calcula_volume(indice):
    soma_vol = 0
    for j in range(len(p[indice])):
        if p[indice][j] == 1:
            soma_vol += produto_volumes[j]
    return soma_vol

def calcula_volumes():
    soma_vols = {}
    for i in range(len(p)):
        soma_vols[i] = calcula_volume(i)
    print("\n")
    return soma_vols

def calcula_preco(indice, populacao):
    soma_preco = 0
    for j in range(len(populacao[indice])):
        if populacao[indice][j] == 1:
            soma_preco += produto_precos[j]
    return soma_preco

def calcula_precos(populacao):
    soma_precos = {}
    for i in range(len(populacao)):
        soma_precos[i] = produto_precos(i, populacao)
    print("\n")
    return soma_precos

print(p)
print(calcula_volumes(p))
