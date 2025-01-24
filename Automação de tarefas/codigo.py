# Projeto de automação "Hashtag da Programação".

# Importar as bibliotecas.
import pyautogui
import time
import pandas as pd

#Auterar a configuração.
pyautogui.PAUSE = 0.5

# Passo 1: Abrir o sistema para cadastro.
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

#entrar no link do site.
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep (3)

# Passo 2: Fazer login
pyautogui.click(x=1202, y=676)
pyautogui.write('cienciaetecnologia23@gmail.com')
pyautogui.press('tab')
pyautogui.write('minhaenha')
pyautogui.press('tab')
pyautogui.press('enter')

# Passo 3: Importar base de dados
tabela = pd.read_csv('produtos.csv')
print(tabela)
time.sleep(3)

#Passo 4: Cadastrar um produtos.
for linha in tabela.index:
    pyautogui.click(x=847, y=755) 
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]

    if obs != 'nan':
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")

# dar scroll de tudo pra cima
pyautogui.scroll(5000)








