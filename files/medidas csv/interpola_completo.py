from tkinter import filedialog
import tkinter as tk

def yCorr(x, ax, ay, bx, by):
    m = (ay - by) / (ax - bx)
    y = ((m * (x - ax)) + ay)
    return y

while True:

    a=input("""Qual a operação desejada?
    0 - Cancelar
    1 - Descobrir Calibração a partir de arquivo Real e Medida
    2 - Descobrir valor Real a partir de Calibração e Medida
    """)

    if(a=="0"):
        break;

    if(a=="1"):

        root=tk.Tk()
        root.withdraw()
        real = filedialog.askopenfile(mode="r",title="Arquivo de leitura REAL separado por tabulação (\\t), com decimal virgula")


        lista_real = real.read()
        lista_real=lista_real.replace(",",".")
        lista_real=lista_real.split("\n")
        for i in range(len(lista_real)):
            lista_real[i]=lista_real[i].split()
            if (len(lista_real[i]) <= 0):
                lista_real.pop(i)
                continue
            else:
                lista_real[i][0] = float(lista_real[i][0])
                lista_real[i][1] = float(lista_real[i][1])
        print(lista_real)

        real.close()


        med = filedialog.askopenfile(mode="r",title="Arquivo de medição(.csv) com decimal virgulae separador ponto e vírfula (;)")
        #med = open("1.5.csv",mode="r")

        lista_med = med.read()
        lista_med=lista_med.replace(",",".")
        lista_med=lista_med.split("\n")

        if (len(lista_med[-1]) <= 0):
            lista_med.pop(-1)

        for i in range(len(lista_med)):
            lista_med[i]=lista_med[i].split(";")
            if (len(lista_med[i]) <= 0):
                lista_med.pop(i)
                continue
            else:
                lista_med[i][0] = float(lista_med[i][0])
                lista_med[i][1] = float(lista_med[i][1])
        print(lista_med)

        med.close()

        menor=""
        while True:
            if (menor == "c") or (lista_real[0][0] <= lista_med[0][0]):
                menor = "c"
                if lista_real[1][0] < lista_med[0][0]:
                    lista_real.pop(0)
                else: break
            elif (menor == "m") or (lista_med[0][0] <= lista_real[0][0]):
                menor = "m"
                if lista_med[0][0] < lista_real[0][0]:
                    lista_med.pop(0)
                else: break


        maior=""
        while True:
            if (maior == "c") or (lista_real[-1][0] >= lista_med[-1][0]):
                maior = "c"
                if lista_real[-2][0] > lista_med[-1][0]:
                    lista_real.pop(-1)
                else: break
            elif (maior == "m") or (lista_med[-1][0] >= lista_real[-1][0]):
                maior = "m"
                if lista_med[-2][0] > lista_real[-1][0]:
                    lista_med.pop(-1)
                else: break





        i=0
        r=[]
        while i < len(lista_med):
            if lista_med[i][0]>=lista_real[1][0]:
                lista_real.pop(0)
            rx = lista_real[0][0]
            ry = lista_real[0][1]
            rx2 = lista_real[1][0]
            ry2 = lista_real[1][1]
            r.append([
                lista_med[i][0],
                yCorr(lista_med[i][0],rx,ry,rx2,ry2)/lista_med[i][1]
                    ])
            #print(str(r[i])+"\t inserido entre os valores correspondentes de \t",cx,cy,"e",cx2,cy2)
            i+=1

        out = filedialog.asksaveasfilename(defaultextension=".txt")
        out=open(out,mode="w")

        for i in r:
            out.writelines(str(i[0])+";"+str(i[1])+"\n")

        out.close()
        break

    ####################################################################################################################################################

    if a == "2":
        root = tk.Tk()
        root.withdraw()
        calib = filedialog.askopenfile(mode="r", title="Arquivo de calibração separado por ponto e vírgula com decimal ponto (padrão gerado)")

        lista_calib = calib.read()
        lista_calib = lista_calib.split("\n")

        if (len(lista_calib[-1]) <= 0):
            lista_calib.pop(-1)

        for i in range(len(lista_calib)):
            lista_calib[i]=lista_calib[i].split(";")
            if (len(lista_calib[i]) <= 0):
                lista_calib.pop(i)
                continue
            else:
                lista_calib[i][0] = float(lista_calib[i][0])
                lista_calib[i][1] = float(lista_calib[i][1])
        print(lista_calib)

        calib.close()



        med = filedialog.askopenfile(mode="r",title="Arquivo de medição(.csv) com decimal virgulae separador ponto e vírfula (;)")
        #med = open("1.5.csv",mode="r")

        lista_med = med.read()
        lista_med=lista_med.replace(",",".")
        lista_med=lista_med.split("\n")

        if (len(lista_med[-1]) <= 0):
            lista_med.pop(-1)

        for i in range(len(lista_med)):
            lista_med[i]=lista_med[i].split(";")
            if (len(lista_med[i]) <= 0):
                lista_med.pop(i)
                continue
            else:
                lista_med[i][0] = float(lista_med[i][0])
                lista_med[i][1] = float(lista_med[i][1])
        print(lista_med)

        med.close()

        input(str(len(lista_med))+"|:|"+str(len(lista_calib)))


        menor=""
        while True:
            if (menor == "c") or (lista_calib[0][0] <= lista_med[0][0]):
                menor = "c"
                if lista_calib[1][0] <= lista_med[0][0]:
                    lista_calib.pop(0)
                else: break
            elif (menor == "m") or (lista_med[0][0] <= lista_calib[0][0]):
                menor = "m"
                if lista_med[0][0] <= lista_calib[0][0]:
                    lista_med.pop(0)
                else: break


        maior=""
        while True:
            if (maior == "m") or (lista_med[-1][0] >= lista_calib[-1][0]):
                maior = "m"
                if lista_med[-2][0] >= lista_calib[-1][0]:
                    lista_med.pop(-1)
                else: break
            elif (maior == "c") or (lista_calib[-1][0] >= lista_med[-1][0]):
                maior = "c"
                if lista_calib[-2][0] >= lista_med[-1][0]:
                    lista_calib.pop(-1)
                else: break


        i=0
        r=[]
        while i < len(lista_med):
            if lista_med[i][0]>=lista_calib[1][0]:
                lista_med.pop(0)
            rx = lista_calib[0][0]
            ry = lista_calib[0][1]
            rx2 = lista_calib[1][0]
            ry2 = lista_calib[1][1]
            print(len(lista_med))
            print(lista_med[-1])
            print(lista_med[-2])
            print(len(lista_calib))
            print(lista_calib[-1])
            print(lista_calib[-2])
            r.append([lista_med[i][0],yCorr(lista_med[i][0],rx,ry,rx2,ry2)*lista_med[i][1]])
            i+=1

        out = filedialog.asksaveasfilename(defaultextension=".txt")
        out=open(out,mode="w")

        for i in r:
            out.writelines(str(i[0])+";"+str(i[1])+"\n")

        out.close()
        break

####################################################################################################################################################

    else:
        print("COMANDO INVÁLIDO")
        continue
exit()
