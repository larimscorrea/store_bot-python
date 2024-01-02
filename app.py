from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl
import selenium


#acessar o site
driver = webdriver.Chrome()
driver.get('https://www.amazon.com.br/s?k=vade+mecum+2024&crid=1LUGSROR2J2MZ&sprefix=vade+me%2Caps%2C182&ref=nb_sb_ss_ts-doa-p_2_7')

#extrair todos os títulos
    # tag[@atributo='valor]
    # h2[@class='nome-produto']

titles = driver.find_elements(By.XPATH, "//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']")

# para encontrar todos os títulos
# for title in titles: 
#     print(titles.text)

#extrair todos os preços

prices = driver.find_elements(By.XPATH, "//a[@class='a-link-normal s-no-hover s-underline-text s-underline-link-text s-link-style a-text-normal']")

# Cria a planilha
workbook = openpyxl.Workbook()

# Cria a página produtos
workbook.create_sheet('products')

# Seleciona a página produtos
sheet_products = workbook['products']

sheet_products['A1'].value = 'Product'
sheet_products['B1'].value = 'Price'
workbook.save('products.xlsx')

#inserir os títulos e preços na planilha

for title, price in zip(titles, prices):
    sheet_products.append([title.text, price.text])

workbook.save('products.xlsx')
