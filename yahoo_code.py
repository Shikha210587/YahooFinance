from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests



yahoo_link = "https://finance.yahoo.com/"
driver= webdriver.Chrome(ChromeDriverManager().install())
driver.get(yahoo_link)
driver.maximize_window()
sleep(1)


scroll_button = driver.find_element(By.CLASS_NAME,'scroll-down-arrow')
scroll_button.click()

scroll_button = driver.find_element(By.NAME,'agree')
scroll_button.click()

sign_button = driver.find_element(By.ID,'login-container')
sign_button.click()
WebDriverWait(driver,5).until(EC.presence_of_element_located((By.ID,"login-landing")))

usermail = 'pspriyasharma931@gmail.com'
userpass = 'ericsson@SH22'
# usermail = input('enter mail id')
# userpass = input('password')

WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.NAME,"username"))).send_keys(usermail)
sleep(1)
next_button = driver.find_element(By.ID,'login-signin')
next_button.click()
sleep(1)

WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.NAME,"password"))).send_keys(userpass)
next_button = driver.find_element(By.ID,'login-signin')
next_button.click()
sleep(1)
driver.get("https://finance.yahoo.com/quote/CL%3DF")
sleep(3)
# driver.find("div",class = "llabel svelte-tx3nkj")
# s=driver.find_element_by_xpath((By.XPATH,"/html/body/div[1]/main/section/section/section/article/div[2]/ul/li[6]/span[1]"))

url = f"https://finance.yahoo.com/quote/CL%3DF"
page = requests.get(url)
soup = BeautifulSoup(page.text,"html.parser")
stock = soup.find(class_="container svelte-tx3nkj").find_all("span")
print(stock)

# stock= soup.find('ul')
ls =[]
res_dict={}
for li in stock:
    # print(li.text,)
    ls.append(li.text)
# print("--------list",ls)

for i in range(0, len(ls), 2):
    res_dict[ls[i]] = ls[i + 1]
print(res_dict)

print("Open value",res_dict.get("Open"))
print("Last value",res_dict.get("Last Price"))
diff= float(res_dict.get("Open") )- float(res_dict.get("Last Price"))
print("Difference is between open and last bid value",diff)
