import selenium
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import time

opt=webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)

driver=webdriver.Chrome(options= opt)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

game=True
money=driver.find_element(By.ID,"money")

costs=[]

timeout=time.time()+8
min=time.time()+300


while game:
    price = driver.find_elements(By.CSS_SELECTOR, "#store b")
    money = driver.find_element(By.ID, "money")
    cookie = driver.find_element(By.ID, "cookie")
    time.sleep(0.1)
    cookie.click()

    costs=[]

    if time.time()>timeout:
        for i in price:
            j = i.text.split()
            if len(j) > 1:
                c = j[len(j) - 1]
                cost = int(c.replace(",", ""))
                costs.append(cost)
        for n in costs:
            k = costs.index(n)

            cursor = driver.find_element(By.ID, "buyCursor")
            grandma = driver.find_element(By.ID, "buyGrandma")
            factory = driver.find_element(By.ID, "buyFactory")
            mine = driver.find_element(By.ID, "buyMine")
            shipment = driver.find_element(By.ID, "buyShipment")
            alchemy = driver.find_element(By.ID, "buyAlchemy lab")
            portal = driver.find_element(By.ID, "buyPortal")
            timemachine = driver.find_element(By.ID, "buyTime machine")
            elderpledge = driver.find_element(By.ID, "buyElder Pledge")
            store = [cursor, grandma, factory, mine, shipment, alchemy, portal, timemachine, elderpledge]
            if n>int(money.text) and n>costs[0]:
                store[k-1].click()
            cookie.click()
        timeout+=10
    if time.time()>min:
        break