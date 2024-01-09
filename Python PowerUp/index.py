# Passo a passo do projeto 

''' Passo 1 - Entrar no sistema da empresa = https://dlp.hashtagtreinamentos.com/python/intensivao/login'''

# pip install pyautogui
import pyautogui
import time
# clicar -> pyautogui.click
# escrever -> pyautogui.write
# apertar uma tecla -> pyautogui.press
# apertar atalho -> pyautogui.hotkey
# rolar -> pyautogui.scroll
pyautogui.PAUSE = 1 # a cada comando, irá pausar 1 segundo
pyautogui.press("win")
pyautogui.write("Google Chrome")
time.sleep(2)
pyautogui.press("enter")
pyautogui.click(x=1297, y=414)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
time.sleep(2)
pyautogui.press("enter")

''' Passo 2 - Fazer login'''

time.sleep(7)
pyautogui.press("tab")
email = "diegohgoto@hotmail.com"
senha = "Di180304!"
pyautogui.write(email)
pyautogui.press("tab")
pyautogui.write(senha)
pyautogui.press("enter")
time.sleep(2)

''' Passo 3 - Importar a base de dados'''

# pip install pandas numpy openpyxl
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

''' Passo 4 - Cadastrar os produtos'''

time.sleep(4)
for linha in tabela.index:

    pyautogui.click(x=297, y=329)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)
