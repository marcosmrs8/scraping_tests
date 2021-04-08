
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
response = requests.get("https://www.zillow.com/homes/San-Francisco,-CA_rb/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.55177535009766%2C%22east%22%3A-122.31488264990234%2C%22south%22%3A37.69926912019228%2C%22north%22%3A37.851235694487485%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D", headers=header)


data = response.text
soup = BeautifulSoup(data, "html.parser")


# get the price
price_list = soup.select(".list-card-price")
all_prices = [price.get_text().split("+")[0][:6] for price in price_list if "$" in price.text]

# get the adress
adress_list = soup.select(".list-card-addr")
all_adress = [adress.get_text().split('|')[-1] for adress in adress_list]

# get the links
all_links = []
all_elements_links = soup.select(".list-card-top a")
for element in all_elements_links:
    links = element['href']
    if 'zillow' not in links:
        all_links.append('www.zillow.com{}'.format(links))
    else:
        all_links.append(links)

driver = webdriver.Chrome(executable_path="A:\development\chromedriver.exe")

for item in range(len(all_links)):
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSeAM99ApSUPC-NMAUby3AAtbd7Scki7T5FM8eiTllAQHJypkg/viewform?usp=sf_link')

    time.sleep(2)
    adress = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')

    links = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')

    adress.send_keys(all_adress[item])
    price.send_keys(all_prices[item])
    links.send_keys(all_links[item])
    submit.click()