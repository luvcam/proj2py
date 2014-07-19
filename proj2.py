j = open("jogos.txt", "r")
jogos = j.readlines()
j.close()
a = open("apostas.txt", "r")
apostas = a.readlines()
a.close()

qtdJog = len(jogos) + 1
a = []
somaPontos = 0
for i in range(0, len(apostas), len(apostas)/qtdJog + 1):
    temp = []
    temp.append(apostas(i))
    

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
