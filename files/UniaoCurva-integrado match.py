# coding=utf-8
import datetime
import os

dia = datetime.date.today()

info = {'f1': {'dia': None, 'hora': '0'}, 'f2': {'dia': None, 'hora': '0'}}

file1 = None
file2 = None
data = ''
menu = ''

# Teste de path alternativo
from tkinter import filedialog, Tk

root = Tk()
root.withdraw()
PATH = filedialog.askdirectory(title="INDIQUE O DIRETÓRIO CONTENDO AS PASTAS ANUAIS", initialdir="C:/")
root.update()


def segue(data):
    pd = data[0:2]
    pm = data[2:4]
    pa = data[4:6]

    pd = str(int(pd) + 1)
    if len(pd) < 2:
        pd = "0" + pd
    if int(pd) > 31:
        pd = "01"
        pm = str(int(pm) + 1)
        if len(pm) < 2:
            pm = "0" + pm
        if int(pm) > 12:
            pm = "01"
            pa = str(int(pa) + 1)
    print(pd, pm, pa)

    return pd + pm + pa


def CoAng(ax, ay, bx, by):
    a = (ay - by) / (ax - bx)
    b = ay - (a * ax)
    return a, b


def YCorr(x, ax, ay, bx, by):
    a, b = CoAng(ax, ay, bx, by)
    y = a * x + b
    return y


def match(v1, v2):
    i = 0
    j = 0
    r = []
    aux = []



    if abs(v1[0][0] - v1[1][0]) < abs(v2[0][0] - v2[1][0]):
        v1, v2 = v2, v1

    while j < len(v2) and i < len(v1) - 1:
        if v2[j][0] < v1[i + 1][0]:
            aux.append(v2[j][0])
            aux.append(((YCorr(v2[j][0], v1[i][0], v1[i][1], v1[i + 1][0], v1[i + 1][1])) + v2[j][1]) / 2)
            j += 1
            r.append(aux)
            aux = []
        else:
            i += 1

    i = 0
    j = 0
    aux = []
    while i < len(v1) and j < len(v2) - 1:
        if v1[i][0] < v2[j + 1][0]:
            aux.append(v1[i][0])
            aux.append(((YCorr(v1[i][0], v2[j][0], v2[j][1], v2[j + 1][0], v2[j + 1][1])) + v1[i][1]) / 2)
            i += 1
            r.append(aux)
            aux = []

        else:
            j += 1

        r.sort()
    return r


def corte(v1, v2):
    #TALVEZ SEJA NECESSÁRIO NÂO APAGAR
    #if abs(v1[0][0] - v1[1][0]) > abs(v2[0][0] - v2[1][0]):
    #    v1, v2 = v2, v1

    for i in range(len(v1)):
        if i == 0 and v1[0][0] == v2[0][0]:
            break
        if v1[i][0] >= v2[0][0]:
            v1 = v1[i:]
            break
    # é preciso definir qual lista tem o menor maximo


    if i == len(v2) and v1[-1][0] == v2[-1][0]:
        return v1, v2

    if v1[-1][0] > v2[-1][0]:
        i = len(v1)
        while i > 0:
            i -= 1  # logo no inicio ja temos v1 decrementação, pois o tamanho da lista conta o indice 0
            if v1[i - 1][0] <= v2[-1][0]:
                v1 = v1[:i]
                break

    else:
        i = len(v2)
        while i > 0:
            i -= 1  # logo no inicio ja temos v1 decrementação, pois o tamanho da lista conta o indice 0
            if v2[i - 1][0] <= v1[-1][0]:
                v2 = v2[:i + 1]
                break
    return v1, v2


def mesclar(v, v2):
    res = []  # Lista para receber, as outras mescladas

    i = 0

    conf = []
    aux = []

    # laço que espera que a lista final seja preenchida
    while True:

        # Verifica se uma lista ja terminou

        if len(v) == 0:
            for e in v2: print(e)
            res.extend(v2)
            v2.pop(0)
            break
        if len(v2) == 0:
            res.extend(v)
            for e in v: print(e)
            v.pop(0)
            break

        # Compara os dois primeiros termos e adiciona o menor na lista res
        if (v[0][0] >= 900 and v[0][0] <= 950) and v2[0][0] > v[0][0]:  # and(v[0][0]<(v[0][0]+1))
            # ZONA DE CONFLITO
            aux.append(v[0][0])
            aux.append(((YCorr(v[0][0], v2[0][0], v2[0][1], v2[1][0], v2[1][1])) + v[0][1]) / 2)  # equação da reta

            v.pop(0)

            conf.append(aux)
            res.append(conf)

            conf = []
            aux = []

        else:
            if v[0][0] == v2[0][0]:
                print("CONFLITO#################################################")
                # input("Confito entre %s %s" %(v[0][0],v2[0][0]))
            if v[0][0] <= v2[0][0]:
                res.append(v[0])
                v.pop(0)
            else:
                res.append(v2[0])
                v2.pop(0)
            print(res[i])
            i += 1
    return res


########################
###INICIO DA EXECUÇÂO###
########################


# dicionário de meses
m = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
mon = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro",
       "dezembro"]

print("""Escolha um procedimento:

0 - Utilizar a data de hoje
1 - Unir todas as curvas a partir de uma data
2 - Informar data específica

""")

while menu not in ["0", "1", "2"]:
    menu = input("->")
    if menu == "0":
        if len(str(dia.day)) < 2:
            data += "0"  # corrige a falta de casa decimal
        data += str(dia.day)

        if len(str(dia.month)) < 2:
            data += "0"
        data += str(dia.month) + str(dia.year)[2::]

        pa = str(dia.year)
        pm = (mon[m.index(data[2:4])])
        pd = data[0:2]


    elif menu == "2" or menu == "1":

        varre = False
        if menu == "1":
            print("Serão realizadas leituras a partir de uma data especifica.")
            varre = True
        print("Informe a data desejada:")

        while True:

            # ANO
            e = input("ano -> (aaaa)")
            if len(e) != 4:
                print("ano inválido!\n")
                continue
            pa = e

            # MES
            e = int(input("mes -> (mm)"))
            if e not in range(1, 13):
                print("mês inválido!\n")
                continue
            e = str(e)
            if len(e) < 2:
                e = "0" + e
            # transforma pm em de numero em texto correspondente
            pm = (mon[m.index(e)])

            # DIA
            e = int(input("dia -> (dd)"))
            if e not in range(1, 32):
                print("dia inválido!\n")
                continue
            e = str(e)
            if len(e) < 2:
                e = "0" + e
            pd = e

            # retornando o pm (path-mes) para numeral para usar a data como padrão ddmmaa
            data = pd + (m[mon.index(pm)]) + pa[2:]

            break

path = PATH + "/" + pa + "/" + pm + "/" + pd
try:
    folder = os.listdir(path)
except Exception as msg:
    print("Erro ao encontrar o caminho especificado")
    print(msg)
    exit(1)

br = False
while True:

    if len(folder) == 0:
        print("Não foram encontrados arquivos em", path)
        br = True
    else:
        for file in folder:
            if file.startswith("S1"):
                if file1 is None and (file[3:9] == data and file[10:14] > info['f1']['hora']):
                    file1 = file
                    info['f1']['dia'] = file[3:9]
                    info['f1']['hora'] = (file[10:14])
                    continue
            elif file.startswith("S2"):
                if file2 is None and (file[3:9] == data and file[10:14] > info['f2']['hora']):
                    file2 = file
                    info['f2']['dia'] = file[3:9]
                    info['f2']['hora'] = (file[10:14])
                    break
            if file1 is None and file == folder[-1]:
                if varre:
                    br = True
                    break
                print("Execução completa em", path)
                exit(0)

    if varre and br:
        br = False
        data = segue(data)
        pd = data[0:2]
        pm = data[2:4]
        pa = "20" + data[4:6]
        pm = (mon[m.index(pm)])
        path = pa + "/" + pm + "/" + pd
        try:
            folder = os.listdir(path)
        except Exception as msg:
            print("Não foi encontrado o caminho:/", path, "/ O processo será terminado")
            exit(0)
        file1 = None
        file2 = None
        info = {'f1': {'dia': None, 'hora': '0'}, 'f2': {'dia': None, 'hora': '0'}}
        continue

    try:
        file1 = open(path + "/" + file1, "r")
        file2 = open(path + "/" + file2, "r")
        lista1 = file1.readlines()
        lista2 = file2.readlines()
    except Exception as msg:
        print("Tentativa de leitura entre:", file1, file2)
        print(msg)
        print("O processo será terminado!")
        exit(1)

    # separação de dat em lista


    ########################################
    ##Transforma file1 em resultados1#######
    ########################################

    dados = False
    for x in range(len(lista1)):
        lista1[x] = lista1[x].replace(',', '.')  # correção de sintaxe decimal
        lista1[x] = lista1[x].replace('\n', '')  # remoção de caracteres indesejados
        if len(lista1[x]) <= 0:
            continue
        if (dados == False) and (("HeaderEnd" in lista1[x]) or (lista1[x][0].isdigit())):  # verifica o fim do cabeçalho
            dados = True
            resultados1 = []  # criação da lista1 somente de valores
            y = 0
            continue
        if dados:  # Somente após o início dos dados
            # os valores são separados em dois
            # comprimento de onda
            # espectro do respectivo comprimento
            resultados1.append(lista1[x].split(";"))
            resultados1[y] = [float(resultados1[y][0]), float(resultados1[y][1])]
            if resultados1[y][0] > 950: break
            y += 1
    '''
    print("TABELA DE RESULTADOS 1\n")
    print("Cp onda | Espectro")
    for x in resultados1:
        print("%.1f\t|%e" % (x[0], x[1]))
    '''
    file1.close()  # não é mais necessária a leitura do arquivo

    # a=input("continua...")

    ################################
    ##Transforma file2 em res2######
    ################################

    dados = False
    for x in range(len(lista2)):
        lista2[x] = lista2[x].replace(',', '.')  # correção de sintaxe decimal
        lista2[x] = lista2[x].replace('\n', '')  # remoção de caracteres indesejados
        if len(lista2[x]) <= 0:
            continue
        if (dados == False) and (("HeaderEnd" in lista2[x]) or (lista2[x][0].isdigit())):  # verifica o fim do cabeçalho
            dados = True
            resultados2 = []  # criação da lista1 somente de valores
            y = 0
            continue
        if dados:  # Somente após o início dos dados
            # os valores são separados em dois
            # comprimento de onda
            # espectro do respectivo comprimento
            resultados2.append(lista2[x].split())  # no caso DESSE arquivo, a lista está separada em \t
            resultados2[y][0] = float(resultados2[y][0])
            resultados2[y][1] = float(resultados2[y][1])
            y = y + 1

    """
    print("TABELA DE RESULTADOS 2\n")
    print("Cp onda | Espectro")
    for x in resultados2:
        print("%.1f\t|%e" % (x[0], x[1]))
    """
    file2.close()  # não é mais necessária a leitura do arquivo

    # ----------------------------#
    # ----MESCLAGEM DE LISTAS-----#
    # ----------------------------#

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!ANTES DE FAZER A MESCLAGHEM!!!
    # !A LISTA DEVE ESTAR ORDENADA!!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # retornando o pm (path-mes) para numeral
    nome = "R_" + pd + (m[mon.index(pm)]) + pa[2:]
    cria = open(PATH + "/" + pa + "/" + pm + "/" + pd + "/" + nome + "_" + info['f1']['hora'] + ".txt", "w")

    fim = []
    for i in resultados1:
        if i[0] > 900:
            fim.extend(resultados1[:resultados1.index(i)])
            break
    for i in resultados2:
        if i[0] > 950:
            fim.extend(resultados2[resultados2.index(i):])
            break

    print(resultados1)
    print(resultados2)
    input("a")

    resultados1, resultados2 = corte(resultados1, resultados2)

    print(resultados1)
    print(resultados2)
    input("b")

    fim.extend(match(resultados1, resultados2))
    fim.sort()

    print(fim)
    input("c")

    # fim = mesclar(resultados1, resultados2)
    fim = "\n".join(str(elm) for elm in fim)  # adiciona as string separando por linha
    fim = fim.replace("[", "")
    fim = fim.replace("]", "")



    cria.write(str(fim))  # escreve
    cria.close()
    file1 = None
    file2 = None
    print("Fim da leitura do arquivo ->", data, info["f1"]["hora"])
print("Finalizado")
