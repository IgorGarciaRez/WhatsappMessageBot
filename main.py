import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib

contatos_df = pd.read_excel('Contatos.xlsx')
print(contatos_df)

option = webdriver.ChromeOptions()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
PATH = "chromedriver.exe"

navegador = webdriver.Chrome(PATH)
navegador.maximize_window()
navegador.get("https://web.whatsapp.com/")

element = WebDriverWait(navegador, 60).until(
        EC.presence_of_element_located((By.ID, "side"))
)

for i, nome in enumerate(contatos_df['Nome']):
    numero = contatos_df.loc[i, "Numero"]
    mensagem = f"Ola {nome}!"
    texto = urllib.parse.quote(mensagem)
    link = f"https://web.whatsapp.com/send?phone={numero}&text={mensagem}"
    navegador.get(link)
    element = WebDriverWait(navegador, 60).until(
        EC.presence_of_element_located((By.ID, "side"))
    )
    element = WebDriverWait(navegador, 60).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p/span'))
    )
    navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p/span').send_keys(Keys.ENTER)
    time.sleep(10)
