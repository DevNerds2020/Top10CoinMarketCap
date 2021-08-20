import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

path = 'chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get('https://coinmarketcap.com/')
names = []
prices = []
content = driver.page_source
soup = BeautifulSoup(content)
driver.quit()
for a in soup.findAll(attrs='sc-16r8icm-0 sc-1teo54s-1 dNOTPP'):
    name = a.find('p') # html <p>
    if name not in names:
        names.append(name.text)

print(names)
# now lets get the prices
for b in soup.findAll(attrs='sc-131di3y-0 cLgOOr'):
    price = b.find('a') # html <p>
    if price not in prices:
        prices.append(price.text)

print(prices)
# now lets put them in a csv file

df = pd.DataFrame({'Names': names, 'prices': prices})
df.to_csv('coinmarketcap.csv', index=False, encoding='utf-8')
# i will put the code on my github
# please dont forget to like and subscribe to my channel tnx guys