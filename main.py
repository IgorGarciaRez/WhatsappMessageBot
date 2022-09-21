import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib

contatos_df = pd.read_excel('Contatos.xlsx')
print(contatos_df)

option = webdriver.ChromeOptions()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chromedriver_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"

navegador = webdriver.Chrome(executable_path=chromedriver_path, options=option)
navegador.get("https://web.whatsapp.com/")

while len(navegador.find_elements_by_id("side")) < 1:
    time.sleep(1)

for i, nome in enumerate(contatos_df['Nome']):
    numero = contatos_df.loc[i, "Telefone"]
    mensagem = f"Ola {nome}!"
    texto = urllib.parse.quote(mensagem)
    link = f"https://web.whatsapp.com/send?phone={numero}&text={mensagem}"
    navegador.get(link)
    while len(navegador.find_elements_by_id("side")) < 1:
        time.sleep(1)
    navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p/span').send_keys(Keys.ENTER)
    time.sleep(10)
