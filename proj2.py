j = open("jogos.txt", "r")
jogos = j.readlines()
j.close()
a = open("apostas.txt", "r")
apostas = a.readlines()
a.close()

import Pontos

j = []
for i in jogos[1:]:
    j.append([int(i.split()[1]), int(i.split()[2])])

qtdJog = len(jogos) + 1
a = []
##for i in range(0, len(apostas), len(apostas)/qtdJog + 1):
for x in range(0, len(apostas), qtdJog):
    somaPontos = 0
##    temp = []
    print apostas[x]
##    for j in range(i+1, i+qtdJog-1):
    for y in range(1, qtdJog-1):
        print y, apostas[y+x][:-1]
        somaPontos = somaPontos + Pontos.pontos(j[y-1],[int(apostas[y+x].split()[1]), int(apostas[y+x].split()[2])])
        print Pontos.pontos(j[y-1],[int(apostas[y+x].split()[1]), int(apostas[y+x].split()[2])])
    temp = [apostas[x][:-1], somaPontos]
    a.append(temp)
##        print [int(apostas[y+x].split()[1]), int(apostas[y+x].split()[2])]
##        somaPontos = somaPontos + Pontos.pontos(j[y],[apostas[y][1], [apostas[y][2]]])
##        somaPontos = somaPontos + pontos([
##j = []
##for i in jogos[1:]:
##    temp = []
##    temp.append(i[:-1].split()[1])
##    temp.append(i[:-1].split()[2])
##    j.append(temp)
##
##a = []
##qntdNom = apostas.count("--\n") + 1
####for i in range(len(apostas))[0:len(apostas):len(apostas)/qntdNom + 1]:
####    temp = []
####    temp.append(apostas[i][:-1])
####    a.append(temp)
##
##for x in range(0, len(apostas), len(apostas)/qntdNom + 1):
##    temp = []
##    temp.append(apostas[x][:-1])
##    for y in range(x+1, x+len(j)):
##        
####        temp.append(apostas[y][:-1].split()[1])
####        temp.append(apostas[y][:-1].split()[2])
####    a.append(temp)
####    print temp
