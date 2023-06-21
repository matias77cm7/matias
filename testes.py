import tkinter
import os
from tkinter import *
import random
import pandas as pd
from datetime import date
resultado = False
legendas = []
legendaerrado = ''
# Imagens
pastaApp=os.path.dirname(__file__)

# cores ---------------------------------------
co0 = "#FFFFFF"  # branca / white
co1 = "#333333"  # preta pesado / dark black
co2 = "#fcc058"  # laranja / orange
co3 = "#38576b"  # valor / value
co4 = "#3297a8"   # azul / blue
co5 = "#fff873"   # amarela / yellow
co6 = "#fcc058"  # laranja / orange
co7 = "#e85151"   # vermelha / red
co8 = co4   # + verde
co10 ="#fcfbf7"
fundo = "#3b3b3b" # preta / black

# criando janela principal
janela = Tk()
janela.title('')
janela.geometry('1200x850')
janela.configure(bg=fundo)
#janela em 1 frames ---------------------------------------

frame_baixo = Frame(janela, width=1500, height=1000, bg=fundo, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NW)

#bandeiras-------------------------------------------------------------------------------------- primeiro codigo desenvolvido por mim 
'''
#1
if op_bandeiras[0] == 1:
    imgband1=PhotoImage(file=pastaApp+'\imagens/ale manha.png')
if op_bandeiras[0] == 2:
    imgband1=PhotoImage(file=pastaApp+'\imagens/argentina.png')
if op_bandeiras[0] == 3:
    imgband1=PhotoImage(file=pastaApp+'\imagens/belgica.png')
if op_bandeiras[0] == 4:
    imgband1=PhotoImage(file=pastaApp+'\imagens/brasil.png')
if op_bandeiras[0] == 5:
    imgband1=PhotoImage(file=pastaApp+'\imagens/espanha.png')
if op_bandeiras[0] == 6:
    imgband1=PhotoImage(file=pastaApp+'\imagens/franca.png')
if op_bandeiras[0] == 7:                                                                                                                                                                                                
    imgband1=PhotoImage(file=pastaApp+'\imagens/inglaterra.png')
if op_bandeiras[0] == 8:
    imgband1=PhotoImage(file=pastaApp+'\imagens/italia.png')
if op_bandeiras[0] == 9:
    imgband1=PhotoImage(file=pastaApp+'\imagens/portugal.png')
if op_bandeiras[0] == 10:
    imgband1=PhotoImage(file=pastaApp+'\imagens/uruguai.png')

l_band1=Label(janela,image=imgband1,width=200,height=200)
l_band1.place(x=0,y=151)
l_band1.configure(bg=('#3b3b3b'))
#2
if op_bandeiras[1] == 1:
    imgband2=PhotoImage(file=pastaApp+'\imagens/alemanha.png')
if op_bandeiras[1] == 2:
    imgband2=PhotoImage(file=pastaApp+'\imagens/argentina.png')
if op_bandeiras[1] == 3:
    imgband2=PhotoImage(file=pastaApp+'\imagens/belgica.png')
if op_bandeiras[1] == 4:
    imgband2=PhotoImage(file=pastaApp+'\imagens/brasil.png')
if op_bandeiras[1] == 5:
    imgband2=PhotoImage(file=pastaApp+'\imagens/espanha.png')
if op_bandeiras[1] == 6:
    imgband2=PhotoImage(file=pastaApp+'\imagens/franca.png')
if op_bandeiras[1] == 7:
    imgband2=PhotoImage(file=pastaApp+'\imagens/inglaterra.png')
if op_bandeiras[1] == 8:
    imgband2=PhotoImage(file=pastaApp+'\imagens/italia.png')
if op_bandeiras[1] == 9:
    imgband2=PhotoImage(file=pastaApp+'\imagens/portugal.png')
if op_bandeiras[1] == 10:
    imgband2=PhotoImage(file=pastaApp+'\imagens/uruguai.png')
l_band2=Label(janela,image=imgband2,width=200,height=200)
l_band2.place(x=0,y=361)
l_band2.configure(bg=('#3b3b3b'))
#3
if op_bandeiras[2] == 1:
    imgband3=PhotoImage(file=pastaApp+'\imagens/alemanha.png')
if op_bandeiras[2] == 2:
    imgband3=PhotoImage(file=pastaApp+'\imagens/argentina.png')
if op_bandeiras[2] == 3:
    imgband3=PhotoImage(file=pastaApp+'\imagens/belgica.png')
if op_bandeiras[2] == 4:
    imgband3=PhotoImage(file=pastaApp+'\imagens/brasil.png')
if op_bandeiras[2] == 5:
    imgband3=PhotoImage(file=pastaApp+'\imagens/espanha.png')
if op_bandeiras[2] == 6:
    imgband3=PhotoImage(file=pastaApp+'\imagens/franca.png')
if op_bandeiras[2] == 7:
    imgband3=PhotoImage(file=pastaApp+'\imagens/inglaterra.png')
if op_bandeiras[2] == 8:
    imgband3=PhotoImage(file=pastaApp+'\imagens/italia.png')
if op_bandeiras[2] == 9:
    imgband3=PhotoImage(file=pastaApp+'\imagens/portugal.png')
if op_bandeiras[2] == 10:
    imgband3=PhotoImage(file=pastaApp+'\imagens/uruguai.png')
l_band3=Label(janela,image=imgband3,width=200,height=200)
l_band3.place(x=0,y=571)
l_band3.configure(bg=('#3b3b3b'))
'''
#ajudinha do chatgpt
bandeiras = {
    1: 'alemanha.png',
    2: 'argentina.png',
    3: 'belgica.png',
    4: 'brasil.png',
    5: 'espanha.png',
    6: 'franca.png',
    7: 'inglaterra.png',
    8: 'italia.png',
    9: 'portugal.png',
    10: 'uruguai.png'
}
l_bandeiras = []
img_bandeiras = []
paises_escolhidos = []
op_bandeiras = random.sample(range(1,11), 3)
for i, op_bandeira in enumerate(op_bandeiras):
    paises_escolhidos.append(bandeiras[op_bandeira])
    img_bandeira = PhotoImage(file=pastaApp + '/imagens/' + bandeiras[op_bandeira]) # as imagens tavam se a perder so mostrava a ultima
    img_bandeiras.append(img_bandeira)
    l_bandeira = Label(janela, image=img_bandeira, width=170, height=200)
    l_bandeira.place(x=0, y=170 + (i * 210))
    l_bandeira.configure(bg='#3b3b3b')
    l_bandeiras.append(l_bandeira)
for i in range(0,3):
    paises_escolhidos[i] = paises_escolhidos[i].replace('.png','')
#----------------------------------------------------------------------------------------------
#clubes----------------------------------------------------------------------------------------
clubes = {
    1: 'ajax.png',
    2: 'arsenal.png',\
    3: 'atletico.png',
    4: 'barca.png',
    5: 'bayern.png',
    6: 'benfica.png',
    7: 'borussia.png',
    8: 'chelsea.png',
    9: 'city.png',
    10: 'juventos.png',
    11: 'liverpool.png',
    12: 'milan.png',
    13: 'porto.png',
    14: 'psg.png',
    15: 'real.png',
    16: 'sporting.png',
    17: 'unt.png'
}
l_clubes = []
img_clubes = []
clubes_escolhidos = []
op_clubes = random.sample(range(1,18), 3)
for i,op_clube in enumerate(op_clubes):
    clubes_escolhidos.append(clubes[op_clube])
    img_clube = PhotoImage(file=pastaApp + '/imagens/clubes/'+clubes[op_clube])
    img_clubes.append(img_clube)
    l_clube = Label(janela, image=img_clube, width=170, height=170)
    l_clube.place(x=220 + (i*210), y=-10)
    l_clube.configure(bg='#3b3b3b')
    l_clubes.append(l_clube)

#----------------------------------------------------------------------------------------------
#base de dados --------------------------------------------------------------------------------
def bandeira(linha, bandeira):
    if 'alemanha' in bandeira[linha-1]:
        return 'Germany'
    if 'argentina' in bandeira[linha-1]:
        return 'Argentina'
    if 'portugal' in bandeira[linha-1]:
        return 'Portugal'
    if 'portugal' in bandeira[linha-1]:
        return 'Belgium'
    if 'brasil' in bandeira[linha-1]:
        return 'Brazil'
    if 'espanha' in bandeira[linha-1]:
        return 'Spain'
    if 'franca' in bandeira[linha-1]:
        return 'France'
    if 'inglaterra' in bandeira[linha-1]:
        return 'England'
    if 'italia' in bandeira[linha-1]:
        return  'Italy'
    if 'uruguai' in bandeira[linha-1]:
        return 'Uruguay'

def caminhos(linha,clubes):
    
    try:
        if 'ajax.png' in clubes[linha-1]:
            return 'Ajax Amsterdam'
        if 'sporting.png' in clubes[linha-1] or 'benfica.png' in clubes[linha-1] or 'porto.png' in clubes[linha-1]:
            if 'sporting.png' in clubes[linha-1]:
                return 'Sporting CP'
            if 'benfica.png' in clubes[linha-1]:
                return 'SL Benfica'
            if 'porto.png' in clubes[linha-1]:
                return 'FC Porto'
        if 'psg.png' in clubes[linha-1]:
            return 'Paris Saint-Germain'
        if 'unt.png' in clubes[linha-1] or 'liverpool.png' in clubes[linha-1] or 'city.png' in clubes[linha-1] or 'chelsea.png' in clubes[linha-1] or 'arsenal.png' in clubes[linha-1]:
            if 'unt.png' in clubes[linha-1]:
                return 'Manchester United'
            if 'liverpool.png' in clubes[linha-1]:
                return 'Liverpool FC'
            if 'city.png' in clubes[linha-1]:
                return 'Manchester City'
            if 'chelsea.png' in clubes[linha-1]:
                return 'Chelsea FC'
            if 'arsenal.png' in clubes[linha-1]:
                return 'Arsenal FC'
        if 'borussia.png' in clubes[linha-1] or 'bayern.png' in clubes[linha-1]:
            if 'borussia.png' in clubes[linha-1]:
                return 'Borussia Dortmund'
            if 'bayern.png' in clubes[linha-1]:
                return 'Bayern Munich'
        if 'atletico.png' in clubes[linha-1] or 'barca.png' in clubes[linha-1] or 'real.png' in clubes[linha-1]:
            if 'atletico.png' in clubes[linha-1]:
                return 'Atlético de Madrid'
            if 'barca.png' in clubes[linha-1]:
                return 'FC Barcelona'
            if 'real.png' in clubes[linha-1]:
                return 'Real Madrid'
        if 'milan.png' in clubes[linha-1] or 'juventos.png' in clubes[linha-1]:
            if 'milan.png' in clubes[linha-1]:
                return 'Milan AC'
            if 'juventos.png' in clubes[linha-1]:
                return 'Juventus FC'
    except UnicodeEncodeError:
        pass

#----------------------------------------------------------------------------------------------

imgLogo=PhotoImage(file=pastaApp+"\imagens/logo.png")
l_logo=Label(janela,image=imgLogo,width=100,height=167)
l_logo.place(x=0,y=0)
l_logo.configure(bg=('#3b3b3b'))

# Configurando o frame cima ---------------------------------------
app_x = Label(frame_baixo, text='X', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co7 )
app_x.place(x=925, y=10)
app_x = Label(frame_baixo, text='Jogador 1', height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=co1, fg=co0 )
app_x.place(x=917, y=70)
app_x_pontos = Label(frame_baixo, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0 )
app_x_pontos.place(x=980, y=20)

app_separador = Label(frame_baixo, text=':', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0 )
app_separador.place(x=1010, y=20)

app_o = Label(frame_baixo, text='O', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co4 )
app_o.place(x=1070, y=10)
app_o = Label(frame_baixo, text='Jogador 2', height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=co1, fg=co0 )
app_o.place(x=1065, y=70)
app_o_pontos = Label(frame_baixo, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0 )
app_o_pontos.place(x=1030, y=20)

# text box para escrever o nome dos jogadores ---------------------------------------
def verificar_resultado():
    global resultado
    with open('C:/Users/Professor/Desktop/trabalho/resultados.txt', 'r') as arquivo:
        resultado = arquivo.read().strip()

# Criando logica do app ---------------------------------------

jogador_1 = "X"
jogador_2 = "O"

score_1 = 0
score_2 = 0

tabela = [['1','2','3'] , ['4','5','6'] , ['7','8','9']]

jogando = 'X'
joga =''
contador = 0
contador_de_rodada = 0
def retornar_conteudo(nomej1):
    return nomej1.get()
def mostrar_na_tela_o_nome(a,b,conteudo):
    legenda = Label(text=conteudo)
    legenda.place(x=a, y=b)
    return legenda

mostrar_ultimas_jogadas = Label(janela, text="")
def iniciar_jogo():
    b_jogar.place(x=713213, y=434234)
    # pra controlar o jogo
    def ficheiro():
        with open('C:/Users/Professor/Desktop/trabalho/score.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
        ultimas_cinco_linhas = linhas[-5:]
        texto = "\n".join(ultimas_cinco_linhas)
        mostrar_ultimas_jogadas.place(x=895,y=200)
        mostrar_ultimas_jogadas.config(text=texto)
    botao_score = Button(janela, text='Mostrar/Atualizar score', command=ficheiro())
    botao_score.place(x=895,y=150)
    def controlar(i):
        global jogando
        global contador
        global jogar
        global legendaerrado
        def verificar():
            if contador>=3:
                botao.destroy()
                nomej1.destroy()
                # linhas
                if tabela[0][0]==tabela[0][1]==tabela[0][2]!="":
                    vencedor(jogando)
                elif tabela[1][0] == tabela[1][1]==tabela[1][2]!="":
                    vencedor(jogando)
                elif tabela[2][0] == tabela[2][1]==tabela[2][2]!="":
                    vencedor(jogando)
                # colunas
                if tabela[0][0] == tabela[1][0]==tabela[2][0]!="":
                    vencedor(jogando)
                elif tabela[0][1] == tabela[1][1]==tabela[2][1]!="":
                    vencedor(jogando)
                elif tabela[0][2] == tabela[1][2]==tabela[2][2]!="":
                    vencedor(jogando)
                # diagonais
                if tabela[0][0] == tabela[1][1]==tabela[2][2]!="":
                    vencedor(jogando)
                elif tabela[0][2] == tabela[1][1]==tabela[2][0]!="":
                    vencedor(jogando)
                # Empate 
                if contador>=9:
                    vencedor('Foi empate') 
        def comparar_dados(nome, bandeira, clube,op):
            global legendaerrado
            #bandeira = 'France'
            # Anthony Martial
            # Marcus Rashford
            # clube = 'Manchester United'
            # clube = 'Real Madrid'
            # Cristiano Ronaldo
            # bandeira = 'Portugal'
            #nome = 'Marcus Rashford'
            bandeira = 'England'
            clube = 'Manchester United'
            arq = pd.read_csv('C:/Users/Professor/Desktop/trabalho/csv/StrikerPerformance.csv')
            
            loc_nome = arq.loc[arq['name'] == nome]
            
            if not loc_nome.empty:
                linha_nome = loc_nome.iloc[0] 
                if linha_nome['nationality'] == bandeira:
                    if linha_nome['current club'] == clube:
                            resultado = True
                    else:
                        legendaerrado = Label(text='Errado')
                        legendaerrado.place(x=845,y=490)
                        resultado = False
                else:
                    legendaerrado = Label(text='Errado')
                    legendaerrado.place(x=845,y=500)
                    resultado = False
            else:
                legendaerrado = Label(text='Errado')
                legendaerrado.place(x=845,y=490)
                resultado = False
            with open('C:/Users/Professor/Desktop/trabalho/resultados.txt', 'w') as arquivo:
                arquivo.write(str(resultado))

            verificar_resultado()
            global legendas
            if op == 1:
                escrever1()
                if resultado == True:
                    legendas.append(mostrar_na_tela_o_nome(290,320,nome))
            elif op == 2:
                escrever2()
                if resultado == True:
                    legendas.append(mostrar_na_tela_o_nome(480,320,nome))
            elif op == 3:
                escrever3()
                if resultado == True:
                    legendas.append(mostrar_na_tela_o_nome(680,320,nome))
            elif op == 4:
                escrever4()
                if resultado == True:
                    legendas.append(mostrar_na_tela_o_nome(290,530,nome))
            elif op == 5:
                escrever5()
                if resultado == True:
                    legendas.append(mostrar_na_tela_o_nome(480,530,nome))
            elif op == 6:
                escrever6()
                if resultado == True:
                    legendas.append(mostrar_na_tela_o_nome(680,530,nome))          
            elif op == 7:
                escrever7()
                if resultado == True:
                    legendas.append(mostrar_na_tela_o_nome(290,730,nome))          
            elif op == 8:
                escrever8()
                if resultado == True:
                    legendas.append(mostrar_na_tela_o_nome(480,730,nome))           
            elif op == 9:
                escrever9()
                if resultado == True:
                    legendas.append(mostrar_na_tela_o_nome(680,730,nome))
        # comparando o valor recebido
        if i==str(1):
            try:
                legendaerrado.destroy()
            except AttributeError:
                pass
            # verificando se aquela posicao esta vazia ou nao
            if b_0['text']=='':
                # verificando quem esta jogar e assim definir a cor do smbolo
                if jogando =='X':
                    cor=co7
                if jogando =='O':
                    cor=co8
                clube= caminhos(1,clubes_escolhidos)
                nomej1 = Entry(janela)
                nomej1.place(x=845,y=450)
                botao = Button(janela, text='Aqui', command=lambda :comparar_dados(retornar_conteudo(nomej1),bandeira(1,paises_escolhidos),clube,1))
                
                botao.place(x=845,y=470)
                janela.update_idletasks()  # Atualizar a interface gráfica
                def escrever1():
                    global jogando
                    global contador
                    global jogar
                    global resultado
                    if resultado == 'True' or resultado == True:
                        b_0['fg'] = cor
                        b_0['text'] = jogando
                        tabela[0][0]= jogando
                        contador+=1
                    else:
                        pass
                    if jogando =='X':
                            jogando = 'O'
                            joga = 'Jogador 1'
                    else:
                            jogando = 'X'
                            joga = 'Jogador 2'
                    
                    botao.destroy()
                    nomej1.destroy()
                    verificar()
        if i==str(2):
            try:
                legendaerrado.destroy()
            except AttributeError:
                pass
            # verificando se aquela posicao esta vazia ou nao
            if b_1['text']=='':
                # varificando quem esta jogar e assim definir a cor do smbolo
                if jogando =='X':
                    cor=co7
                if jogando =='O':
                    cor=co8
                clube= caminhos(2,clubes_escolhidos)
                nomej1 = Entry(janela)
                nomej1.place(x=845,y=450)
                botao = Button(janela, text='Aqui', command=lambda :comparar_dados(retornar_conteudo(nomej1),bandeira(2,paises_escolhidos),clube,2))
                botao.place(x=845,y=470)
                janela.update_idletasks()  # Atualizar a interface gráfica
                def escrever2():
                    global jogando
                    global contador
                    global jogar
                    global resultado
                    if resultado == 'True' or resultado == True:
                        b_1['fg'] = cor
                        b_1['text'] = jogando
                        tabela[0][1]= jogando
                        contador+=1
                    else:
                        pass
                    if jogando =='X':
                            jogando = 'O'
                            joga = 'Jogador 1'
                    else:
                            jogando = 'X'
                            joga = 'Jogador 2'
                    
                    botao.destroy()
                    nomej1.destroy()
                    verificar()
        if i==str(3):
            try:
                legendaerrado.destroy()
            except AttributeError:
                pass
            if b_2['text']=='':
                if jogando =='X':
                    cor=co7
                if jogando =='O':
                    cor=co8
                clube= caminhos(3,clubes_escolhidos)
                nomej1 = Entry(janela)
                nomej1.place(x=845,y=450)
                botao = Button(janela, text='Aqui', command=lambda :comparar_dados(retornar_conteudo(nomej1),bandeira(3,paises_escolhidos),clube,3))
                botao.place(x=845,y=470)
                janela.update_idletasks()  # Atualizar a interface gráfica
                def escrever3():
                    global jogando
                    global contador
                    global jogar
                    global resultado
                    if resultado == 'True' or resultado == True:
                        b_2['fg'] = cor
                        b_2['text'] = jogando
                        tabela[0][2]= jogando
                        contador+=1
                    else:
                        pass
                    if jogando =='X':
                            jogando = 'O'
                            joga = 'Jogador 1'
                    else:
                            jogando = 'X'
                            joga = 'Jogador 2'
                    
                    botao.destroy()
                    nomej1.destroy()
                    verificar()
        if i==str(4):
            try:
                legendaerrado.destroy()
            except AttributeError:
                pass
            # verificando se aquela posicao esta vazia ou nao
            if b_3['text']=='':
                # varificando quem esta jogar e assim definir a cor do smbolo
                if jogando =='X':
                    cor=co7
                if jogando =='O':
                    cor=co8
                clube= caminhos(1,clubes_escolhidos)
                nomej1 = Entry(janela)
                nomej1.place(x=845,y=450)
                botao = Button(janela, text='Aqui', command=lambda :comparar_dados(retornar_conteudo(nomej1),bandeira(1,paises_escolhidos),clube,4))
                botao.place(x=845,y=470)
                janela.update_idletasks()  # Atualizar a interface gráfica
                def escrever4():
                    global jogando
                    global contador
                    global jogar
                    global resultado
                    if resultado == 'True' or resultado == True:
                        b_3['fg'] = cor
                        b_3['text'] = jogando
                        tabela[1][0]= jogando
                        contador+=1
                    else:
                        pass
                    if jogando =='X':
                            jogando = 'O'
                            joga = 'Jogador 1'
                    else:
                            jogando = 'X'
                            joga = 'Jogador 2'
                    
                    botao.destroy()
                    nomej1.destroy()
                    verificar()

        if i==str(5):
            try:
                legendaerrado.destroy()
            except AttributeError:
                pass
            # verificando se aquela posicao esta vazia ou nao
            if b_4['text']=='':
                # varificando quem esta jogar e assim definir a cor do smbolo
                if jogando =='X':
                    cor=co7
                if jogando =='O':
                    cor=co8
                clube= caminhos(2,clubes_escolhidos)
                nomej1 = Entry(janela)
                nomej1.place(x=845,y=450)
                botao = Button(janela, text='Aqui', command=lambda :comparar_dados(retornar_conteudo(nomej1),bandeira(2,paises_escolhidos),clube,5))
                botao.place(x=845,y=470)
                janela.update_idletasks()  # Atualizar a interface gráfica
                def escrever5():
                    global jogando
                    global contador
                    global jogar
                    global resultado
                    if resultado == 'True' or resultado == True:
                        b_4['fg'] = cor
                        b_4['text'] = jogando
                        tabela[1][1]= jogando
                        contador+=1
                    else:
                        pass
                    if jogando =='X':
                            jogando = 'O'
                            joga = 'Jogador 1'
                    else:
                            jogando = 'X'
                            joga = 'Jogador 2'
                   
                    botao.destroy()
                    nomej1.destroy()
                    verificar()

        if i==str(6):
            try:
                legendaerrado.destroy()
            except AttributeError:
                pass
            # verificando se aquela posicao esta vazia ou nao
            if b_5['text']=='':
                # varificando quem esta jogar e assim definir a cor do smbolo
                if jogando =='X':
                    cor=co7
                if jogando =='O':
                    cor=co8
                clube= caminhos(3,clubes_escolhidos)
                nomej1 = Entry(janela)
                nomej1.place(x=845,y=450)
                botao = Button(janela, text='Aqui', command=lambda :comparar_dados(retornar_conteudo(nomej1),bandeira(3,paises_escolhidos),clube,6))
                botao.place(x=845,y=470)
                janela.update_idletasks()  # Atualizar a interface gráfica
                def escrever6():
                    global jogando
                    global contador
                    global jogar
                    global resultado

                    if resultado == 'True' or resultado == True:
                        b_5['fg'] = cor
                        b_5['text'] = jogando
                        tabela[1][2]= jogando
                        contador+=1
                    else:
                        pass
                    if jogando =='X':
                            jogando = 'O'
                            joga = 'Jogador 1'
                    else:
                            jogando = 'X'
                            joga = 'Jogador 2'
                    
                    botao.destroy()
                    nomej1.destroy()
                    verificar()  

        if i==str(7):
            try:
                legendaerrado.destroy()
            except AttributeError:
                pass
            # verificando se aquela posicao esta vazia ou nao
            if b_6['text']=='':
                # varificando quem esta jogar e assim definir a cor do smbolo
                if jogando =='X':
                    cor=co7
                if jogando =='O':
                    cor=co8
                clube= caminhos(1,clubes_escolhidos)
                nomej1 = Entry(janela)
                nomej1.place(x=845,y=450)
                botao = Button(janela, text='Aqui', command=lambda :comparar_dados(retornar_conteudo(nomej1),bandeira(1,paises_escolhidos),clube,7))
                botao.place(x=845,y=470)
                janela.update_idletasks()  # Atualizar a interface gráfica
                def escrever7():
                    global jogando
                    global contador
                    global jogar
                    global resultado

                    if resultado == 'True' or resultado == True:
                        b_6['fg'] = cor
                        b_6['text'] = jogando
                        tabela[2][0]= jogando
                        contador+=1
                    else:
                        pass
                    if jogando =='X':
                            jogando = 'O'
                            joga = 'Jogador 1'
                    else:
                            jogando = 'X'
                            joga = 'Jogador 2'
                    contador+=1
                    botao.destroy()
                    nomej1.destroy()
                    verificar() 

        if i==str(8):
            try:
                legendaerrado.destroy()
            except AttributeError:
                pass
            # verificando se aquela posicao esta vazia ou nao
            if b_7['text']=='':
                # varificando quem esta jogar e assim definir a cor do smbolo
                if jogando =='X':
                    cor=co7
                if jogando =='O':
                    cor=co8
                clube= caminhos(2,clubes_escolhidos)
                nomej1 = Entry(janela)
                nomej1.place(x=845,y=450)
                botao = Button(janela, text='Aqui', command=lambda :comparar_dados(retornar_conteudo(nomej1),bandeira(2,paises_escolhidos),clube,8))
                botao.place(x=845,y=470)
                janela.update_idletasks()  # Atualizar a interface gráfica
                def escrever8():
                    global jogando
                    global contador
                    global jogar
                    global resultado
                    if resultado == 'True' or resultado == True:
                        b_7['fg'] = cor
                        b_7['text'] = jogando
                        tabela[2][1]= jogando
                        contador+=1
                    else:
                        pass
                    if jogando =='X':
                            jogando = 'O'
                            joga = 'Jogador 1'
                    else:
                            jogando = 'X'
                            joga = 'Jogador 2'
                    
                    botao.destroy()
                    nomej1.destroy()
                    verificar()      

        if i==str(9):
            try:
                legendaerrado.destroy()
            except AttributeError:
                pass
            # verificando se aquela posicao esta vazia ou nao
            if b_8['text']=='':
                # varificando quem esta jogar e assim definir a cor do smbolo
                if jogando =='X':
                    cor=co7
                if jogando =='O':
                    cor=co8
                clube= caminhos(3,clubes_escolhidos)
                nomej1 = Entry(janela)
                nomej1.place(x=845,y=450)
                botao = Button(janela, text='Aqui', command=lambda :comparar_dados(retornar_conteudo(nomej1),bandeira(3,paises_escolhidos),clube,9))
                botao.place(x=845,y=470)
                janela.update_idletasks()  # Atualizar a interface gráfica
                def escrever9():
                    global jogando
                    global contador
                    global jogar
                    global resultado
                    if resultado == 'True' or resultado == True:
                        b_8['fg'] = cor
                        b_8['text'] = jogando
                        tabela[2][2]= jogando
                        contador+=1
                    else:
                        pass
                    if jogando =='X':
                            jogando = 'O'
                            joga = 'Jogador 1'
                    else:
                            jogando = 'X'
                            joga = 'Jogador 2'
                    
                    botao.destroy()
                    nomej1.destroy()
                    verificar()

        # Apos o contador ser maior ou igual a 5, 
        # verifica se ouve algum vencedor de acordo 
        # com os padroes seguintes dentro da tabela



    # pra decidir o vencedor
    def vencedor(i):
        global tabela
        global score_1
        global score_2
        global contador_de_rodada
        global contador
        global legendas
        # bloqueando os botoes
        b_0['state']='disable'
        b_1['state']='disable'
        b_2['state']='disable'
        b_3['state']='disable'
        b_4['state']='disable'
        b_5['state']='disable'
        b_6['state']='disable'
        b_7['state']='disable'
        b_8['state']='disable'

        app_vencedor = Label(frame_baixo, text='', width=17, relief='flat', anchor='center', font=('Ivy 13 bold'), bg=co1, fg=co2 )
        app_vencedor.place(x=930, y=130)

        if i =='X':
            score_2+=1
            app_vencedor['text'] = 'Joagador 2 venceu'
            app_o_pontos['text'] =score_2

        if i =='O':
            score_1+=1
            app_vencedor['text'] = 'Joagador 1 venceu'
            app_x_pontos['text'] =score_1

        if i=='Foi empate':
            app_vencedor['text'] = 'Foi um empate'

        def start():
            # limpando os botoes
            b_0['text']=''
            b_1['text']=''
            b_2['text']=''
            b_3['text']=''
            b_4['text']=''
            b_5['text']=''
            b_6['text']=''
            b_7['text']=''
            b_8['text']=''

            b_0['state']='normal'
            b_1['state']='normal'
            b_2['state']='normal'
            b_3['state']='normal'
            b_4['state']='normal'
            b_5['state']='normal'
            b_6['state']='normal'
            b_7['state']='normal'
            b_8['state']='normal'

            app_vencedor.destroy()
            b_jogar.destroy()
            for legenda in legendas:
                legenda.destroy()
        # Botao jogar
        b_jogar = Button(frame_baixo, command=start, text='Proxima rodada', height=1,  font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0 )
        b_jogar.place(x=965, y=90)


        def jogo_acabou():
            b_jogar.destroy()
            app_vencedor.destroy()

            terminar()

        if contador_de_rodada>=5:
            jogo_acabou()
        else:
            contador_de_rodada+=1
            # reiniciando a tabela
            tabela = [['1','2','3'] , ['4','5','6'] , ['7','8','9']]
            contador = 0



    # pra terminar o jogo atual
    def terminar():
        global tabela
        global contador_de_rodada
        global score_1
        global score_2
        global contador
        today = date.today()
        today = str(today)
        print(today)
        with open('C:/Users/Professor/Desktop/trabalho/score.txt', 'a') as aq:
                aq.write(f'{today} X = {score_1}  O = {score_2}\n')
        tabela = [['1','2','3'] , ['4','5','6'] , ['7','8','9']]
        contador_de_rodada = 0
        score_1 = 0
        score_2 = 0
        contador = 0

        # bloqueando os botoes
        b_0['state']='disable'
        b_1['state']='disable'
        b_2['state']='disable'
        b_3['state']='disable'
        b_4['state']='disable'
        b_5['state']='disable'
        b_6['state']='disable'
        b_7['state']='disable'
        b_8['state']='disable'

        app_fim = Label(frame_baixo, text='Jogo Acabou', width=17, relief='flat', anchor='center', font=('Ivy 13 bold'), bg=co1, fg=co2 )
        app_fim.place(x=930, y=130)

        # jogar de novo

        def jogar_denovo():
            app_x_pontos['text'] = '0'
            app_o_pontos['text'] = '0'
            app_fim.destroy()
            b_jogar.destroy()

            # chamando a funcao iniciar o jogo
            iniciar_jogo()

        # Botao jogar denovo
        b_jogar = Button(frame_baixo, command=jogar_denovo, text='Jogar de novo', height=1,  font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0 )
        b_jogar.place(x=965, y=90)






    # linhas verticais 
    app_ = Label(frame_baixo, text='', height=82, relief='flat', pady=5, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7 )
    app_.place(x=420, y=175)
    app_ = Label(frame_baixo, text='', height=82, relief='flat', pady=5, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7 )
    app_.place(x=620, y=175)

    # linhas horizontais 
    app_ = Label(frame_baixo, text='', width=145, relief='flat', padx=2, pady=-1, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7 )
    app_.place(x=230, y=350)
    app_ = Label(frame_baixo, text='', width=145, relief='flat', padx=2, pady=-1, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7 )
    app_.place(x=230, y=560)
    
    #linhas finais
    app_ = Label(frame_baixo, text='', width=145, relief='flat', padx=2, pady=-1, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7 )
    app_.place(x=230, y=758)
    app_ = Label(frame_baixo, text='', width=145, relief='flat', padx=2, pady=-1, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7 )
    app_.place(x=230, y=167)
    #horizontal
    app_ = Label(frame_baixo, text='', height=84, relief='flat', pady=5, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7 )
    app_.place(x=813, y=167)
    app_ = Label(frame_baixo, text='', height=84, relief='flat', pady=5, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7 )
    app_.place(x=225, y=167)
    # linha 0
    b_0 = Button(frame_baixo,command=lambda:controlar('1'), text='', width=10, height=4,  font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7 )
    b_0.place(x=237, y=190)
    b_1 = Button(frame_baixo,command=lambda:controlar('2'), text='', width=10, height=4,  font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7 )
    b_1.place(x=433, y=190)
    b_2 = Button(frame_baixo,command=lambda:controlar('3'), text='', width=10, height=4,  font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7 )
    b_2.place(x=630, y=190)


    # linha 1
    b_3 = Button(frame_baixo,command=lambda:controlar('4'), text='', width=10, height=5,  font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7 )
    b_3.place(x=236, y=370)
    b_4 = Button(frame_baixo,command=lambda:controlar('5'), text='', width=10, height=5,  font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7 )
    b_4.place(x=433, y=370)
    b_5 = Button(frame_baixo,command=lambda:controlar('6'), text='', width=10, height=5,  font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7 )
    b_5.place(x=630, y=370)

    # linha 2
    b_6 = Button(frame_baixo,command=lambda:controlar('7'), text='', width=10, height=5,  font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7 )
    b_6.place(x=236, y=573)
    b_7 = Button(frame_baixo,command=lambda:controlar('8'), text='', width=10, height=5,  font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7 )
    b_7.place(x=433, y=573)
    b_8 = Button(frame_baixo,command=lambda:controlar('9'), text='', width=10, height=5,  font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7 )
    b_8.place(x=630, y=573)

# Botao jogar
b_jogar = Button(frame_baixo,command=iniciar_jogo, text='Jogar', width=10, height=1,  font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0 )
b_jogar.place(x=970, y=90)


janela.mainloop()