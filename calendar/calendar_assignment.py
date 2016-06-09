# My old calendar program converted to Python 3
# Formatting adjusted for IDLE

def semana(d,m,a):
    res = (d + int(m*30.6) + int((a*1461)/4) + 5) % 7
    return res

def ajuste(mes,b,ano):
    if (mes < 3):
        m = mes + 13
        a = ano - 1
    else:
        m = mes + 1
        a = ano
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        ld = 31
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        ld = 30
    else:
        ld = 28 + b
    return (ld, m, a)

def calendario(mes,ano,b):
    nomemes = ("Jan ","Fev ","Mar ","Abr ","Mai ","Jun ","Jul ","Ago ","Set ","Out ","Nov ","Dez ")
    calend = [["   " for x in range(7)] for y in range(7)]
    ld, m, a = ajuste(mes,b,ano)
    print(nomemes[mes-1]," de ", ano)
    print("dom seg ter qua qui sex sab")
    k = 0
    for i in range(1,ld+1):
        semtemp = semana(i,m,a)
        if i < 10:
            calend[k][semtemp] = "  " + str(i)
        else:
            calend[k][semtemp] = " " + str(i)
        if semtemp == 6 or i == ld:
            for j in range(7):
                print(calend[k][j], end=" ")
            k = k + 1
            print("\n")
    print("----------------------------")

print("""CALENDARIO 1900-2099
Este programa exibe o dia da semana referente a uma data
especificada entre os anos 1900 e 2099. E tambem oferece
a opcao de visualizar o calendario mensal ou anual.""")

ano = int(input("Para comecar, digite o ano que deseja (formato: yyyy): "))
while True:
    if int(ano) < 1900 or int(ano) > 2099:
        ano = int(input("""Erro. So e permitido anos entre 1900 e 2099.
Digite novamente: """))
    else:
        break

if (ano % 400 == 0) or (ano % 100 != 0 and ano % 4 == 0):
    biss = 1
else:
    biss = 0

mes = int(input("\nAgora, digite o mes que deseja (formato: mm): "))
while True:
    if mes < 1 or mes > 12:
        mes = int(input("""Erro. Espera-se um valor entre 1 e 12.
Digite novamente: """))
    else:
        break

ld, mestemp, anotemp = ajuste(mes,biss,ano)

dia = int(input("\nDigite o dia que deseja (formato: dd): "))
while True:
    if dia < 1 or dia > ld:
        print("Erro. Para o mes ",mes," espera-se um valor entre 1 e ",ld,".")
        dia = int(input("Digite novamente: "))
    else:
        break

semtemp = semana(dia,mestemp,anotemp)
diadasemana = ("domingo","segunda","terca  ","quarta ","quinta ","sexta  ","sabado ")
print("\n",dia,"/",mes,"/",ano,", dia da semana: ", diadasemana[semtemp])
print("O ano ", ano, " tem ", (365+biss), " dias.")

print("Para visualizar o calendario do mes e ano especificados, digite 1;")
print("Para visualizar o calendario completo do ano especificado, digite 2;")
print("Digite qualquer outra tecla para encerrar o programa.")
op = int(input("Digita a sua opcao: "))
if op == 1:
    print("CALENDARIO MENSAL")
    calendario(mes,ano,biss)
elif op == 2:
    print("CALENDARIO MENSAL")
    for i in range(12):
        calendario(i+1,ano,biss)
else:
    print("Encerrando programa...")

