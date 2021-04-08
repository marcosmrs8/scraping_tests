
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

#http://myhttpheader.com (link to get language and user-agent)

header = {
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
}

#get the link to check
response = requests.get("https://www.quintoandar.com.br/alugar/imovel/sao-paulo-sp-brasil/4-3-2-1-quartos/de-500-a-3000-aluguel", headers=header)


data = response.text
soup = BeautifulSoup(data, "html.parser")

price_list = soup.find_all("p", class_="m82tat-3 kVYbKp sc-bdVaJa iTBXOV")

all_prices = []
for i in price_list:
    price = i.text[8:-1].replace(u'\xa0', u' ')
    if len(price) > 5:
        all_prices.append(price)

# print(all_prices)

address_list = soup.find_all("div", class_="hhh4j4-3 cJuvGy")
all_adresses = [item.text for item in address_list if item.text != '']

link_list = soup.find_all("a", class_="sc-15oj7uq-0 hLbavN")
all_links =[]
for element in link_list:

    try:
        links = 'https://www.quintoandar.com.br' + element['href']
        all_links.append(links)
        print(all_links)
    except Exception:
        links = 'https://www.quintoandar.com.br' + element['href']
        print(links)

driver = webdriver.Chrome(executable_path="A:\development\chromedriver.exe")
for item in range(len(all_links)):
    print(len(all_links))
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdizckdxD4zsos2eWZlubJDVoo1D3H0ii7tmUTHSLT-F2V1lg/viewform?usp=sf_link')
    time.sleep(2)
    
    
    address = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    links = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div/span/span')
    
    
    address.send_keys(all_adresses[item])
    price.send_keys(all_prices[item])
    links.send_keys(all_links[item])
    submit.click()

















