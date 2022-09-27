import time
import pandas as pd
import requests
import json
import xlsxwriter

workbook = xlsxwriter.Workbook('emails.xlsx')
worksheet = workbook.add_worksheet()
row = 0
column = 0

cnpj_df = pd.read_excel('Cnpjs teste.xlsx')
print(cnpj_df)

def consulta_cnpj(cnpj):
    url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"
    querystring = {"token": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX", "cnpj": "06990590000123", "plugin": "RF"}
    response = requests.request("GET", url, params=querystring)
    resp = json.loads(response.text)
    return resp['email']


for i in cnpj_df['cnpj']:
    item = consulta_cnpj(i)
    worksheet.write(row, column, item)
    row += 1
    time.sleep(20)

workbook.close()