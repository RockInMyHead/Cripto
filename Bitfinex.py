a = [1,2,3]
# encoding=utf8
import pickle
import time
import urllib

import chromedriver_binary
import selenium
##
from selenium import webdriver
from selenium.common.exceptions import (ElementClickInterceptedException,
                                NoSuchElementException,
                                WebDriverException)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

print ('st.')

#site = "https://invest.yandex.ru/catalog/fund/fxwo/"

#chrome_options = Options()
#chrome_options.add_argument("--headless")

#driver = webdriver.Chrome(options=chrome_options)
#driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome()
#driver.get(site)

#one_prise = driver.find_element_by_id("root")

import requests
from bs4 import BeautifulSoup

#def big_broker(price):
#price2 = price
prise_list = [0]
old_price = 0
prise1 = 0
buy = True
sell = False
site = "https://www.okx.com/ru/trade-spot/1inch-usdt"

#chrome_options = Options()
#chrome_options.add_argument("--headless")

#driver = webdriver.Chrome()
#driver.get(site)
        #picklein.dump(driver.get_cookies(), open ("session","wb"))
chromedriver = 'C:/broker/chromedriver'
#options = webdriver.ChromeOptions()

options = webdriver.ChromeOptions()


driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
driver.get(site)
def sell():
    print ('/////////////////sell')
    time.sleep(4)
    element_one =driver.find_element_by_xpath("/html/body/div[3]/main/div/section/div[3]/div[2]/div/div[1]/div/div[9]/div/div[1]/div[2]/div[5]/div/div[2]/div[2]/button")
    #                                           /html/body/div[2]/div[1]/div/div/div/div/div[1]/div/div/div/div[5]/div[2]
    element_one.click()
    #time.sleep(3)
    #sell = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/form/div[4]/div[1]/div[1]/div/input").send_keys(0)
    #enter = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div/div[3]/div[2]/label[1]/label/input").send_keys(u'\ue007')
    #time.sleep(4)
    #button_2 = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/form/div[3]/div").click()
def buy():
    time.sleep(4)
    element_one =driver.find_element_by_xpath("/html/body/div[3]/main/div/section/div[3]/div[2]/div/div[1]/div/div[9]/div/div[1]/div[2]/div[5]/div/div[1]/div[2]/button")
    element_one.click()
    #time.sleep(4)
    #buy = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/form/div[4]/div[1]/div[1]/div/input").send_keys("\r3")
    #enter = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div[3]/div[2]/label[1]/label/input").send_keys(u'\ue007')
    #button_1 = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/form/div[3]/div").click()
    #time.sleep(1)
    #button_2 = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/form/button").click()
    #time.sleep(7)
    #button_2 = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div[3]/button").click()

def register_on_site():
    #reg_path = "/html/body/div[1]/header/div[2]/div[1]/span[1]" #"/html/body/div[2]/div[1]/header/div/span[2]/a[1]"
    #element = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/header/div/span[2]/a[1]")))
    #register = driver.find_element_by_xpath("/html/body/div[1]/header/div[2]/div[1]/span[1]").click()
    yandex_id = "/html/body/div/div[2]/div/div/form/div/div/div/div[1]/label/span"
    password = "/html/body/div[2]/div/div/main/div/div/div/div/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[2]/input"
    register_id = driver.find_element_by_xpath(yandex_id).send_keys("+79186222038")
    time.sleep(10)
    register_button_1 =driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[3]/button").click()
    #/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[3]/button
    time.sleep(4)
    #cookie = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/table/tbody/tr/td[2]/table/tbody/tr/td[2]/button").click()
    register_password = driver.find_element_by_xpath(password).send_keys("135797531AaA")
    time.sleep(40)
    #/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/form/div[3]/button
    #register_button_2 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/form/div[3]/button").click()
    time.sleep(10)
    buy()
    print ("Вызываю buy")

ind = 0
h = 0
index = 0
#register_on_site()
time.sleep(120)
def check():
    driver.get("https://www.okx.com/ru/trade-spot/1inch-usdt")
    rehtml = driver.page_source
    #url = 'https://invest.yandex.ru/catalog/fund/fxwo/'
    #response = requests.get(site)
    soup = BeautifulSoup(rehtml, 'html5lib')
    quotes = soup.find('div', class_='src-containers-Animated-styles-default-1BbLJ')
    #print (quotes)
    time.sleep(10)
    prise_tin = driver.find_element_by_xpath("/html/body/div[3]/header/div/div/div[2]/div/div/div[1]/div/div[3]/div")
    print (prise_tin.text)
    try:
        for i in quotes:
            quotes = i
            quotes = quotes.replace('₽','')
            quotes = quotes.replace(' ','') # чистим цифры

            newquotes = ""
            b = 0
            for i in quotes:
                b +=1
                if b < 7 and i != ',': # убираем запятую
                    newquotes += i
                    quotes = newquotes # 2 0000
            prise2 = int(newquotes) #2
        #print ("Цена"+ str(prise2))
        price2 = prise2
        #print (price2)
        return price2
        #prise_list.append(int(price2)) # [2]
        #print (prise2) #2
        #print (prise_list) #[2]
    except TypeError:
        print ("Ошибка TypeError")
        pass
my_paper=[]
#price1 = 0#0
i2 = True
n = 0
prise_2 = 0
list_prise = []
flag_buy = 0
stop = 0
stop_list = []
nl = 0
all_money = 0
while i2 == True:
    time.sleep(2)
    n +=1
    print (n)
    try:
        prise_tin3 = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[1]/div[2]/div[3]/span[1]").text
        print ("Цена: " + str(prise_tin3))
        prise_tin3_3 = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/div/input").send_keys(Keys.CONTROL + "a")
        prise_tin3_1 = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/div/input").send_keys(Keys.DELETE)
        prise_tin3_1 = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/div/input").send_keys(prise_tin3)
        #time.sleep(1)
        #чистим колличество
        prise_tin3_3 = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/div/div/input").send_keys(Keys.CONTROL + "a")
        prise_tin3_1 = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/div/div/input").send_keys(Keys.DELETE)
        const_buy= driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/div/div/input").send_keys("0.100000")

        prise_tin3_3_1 = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/div/div/input").send_keys(Keys.CONTROL + "a")
        time.sleep(1)
        prise_tin3_1_1 = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/div/div/input").send_keys(Keys.DELETE)
        prise_tin3_1_1 = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/div/div/input").send_keys(prise_tin3)

        #чистим колличество
        prise_tin3_3 = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div/input").send_keys(Keys.CONTROL + "a")
        prise_tin3_1 = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div/input").send_keys(Keys.DELETE)

        const_sell= driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div/input").send_keys("0.100000")

        #close = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[5]/div[2]/div[3]/div[1]/div[2]").click()
        prise_tin3 = str(prise_tin3)
        prise_tin3_3 = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/div").click()
        prise_tin3_3_p = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div[3]/div[2]/div/div/input").get_attribute("value")
        buy_my_prise = prise_tin3_3_p
        print ("Цена за 0.1 : " + str(prise_tin3))
    except:
        try:
            close_error2 = driver.find_element_by_xpath("/html/body/div[10]/div/div[4]/div/button[1]").click()
        except :
            print ("Ошибка")
    #ost_buy = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[3]/div[2]/div[1]/div/div[3]/div/div[2]/div/div/div[3]/div[1]").text
    #ost_sell = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[3]/div[2]/div[1]/div/div[3]/div/div[2]/div/div/div[3]/div[1]").text
    #ost_buy = ost_buy.replace("Доступно","")
    #ost_sell = ost_sell.replace("Доступно","")
    ost_buy = 1
    ost_sell = 1
    print (ost_buy)
    print (ost_sell)
    try:
        quotes = prise_tin3_3_p
        quotes = quotes.replace('USD','')
        quotes = quotes.replace(' ','') # чистим цифры # 6400
        quotes = quotes.replace(',','')
        quotes = quotes.replace('.','')
        if len(quotes) < 5:
            quotes = quotes + "0"
        prise_1 = int(quotes)
        print (prise_1)
    except :
        print ("Ошибка")
        time.sleep(2)
        pass
    nl += 1
    kommission = prise_1 * 0.01
    kommission = kommission * 0.0018
    kommission = kommission + kommission
    print ("Комиссия состовляет : " + str(kommission))
    for i in list_prise:
        if prise_1 > (i+10):
            try:
                ps = prise_1
                ps2 = format(ps, ',d')
                time.sleep(1)
                prise_tin3_3_1 = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/div/div/input").send_keys(Keys.CONTROL + "a")
                time.sleep(1)
                prise_tin3_1_1 = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/div/div/input").send_keys(Keys.DELETE)
                prise_tin3_1_1 = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/div/div/input").send_keys(prise_tin3)
                sell = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div[8]/div/button").click()
                print ("Старая цена: " + str(i) + "  Новая цена: " + str(prise_1) + "  Выставляю на продажу за +  10: " + str(prise_1))
                #len_1 = len(list_prise)
                #one_prise = 0,009994
                const_sell= driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div/input").send_keys("0.1")
                list_prise.remove(i)
                all_money = (all_money + ((prise_1 - i) + 10))
                print ("Общая прибыль : " + all_money)
            except :
                try:
                    close_error = driver.find_element_by_xpath("/htmыl/body/div[10]/div/div[4]/div/button[1]").click()
                    list_prise.append(int(i))
                except :
                    try:
                        prise_tin3_3_1 = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/div/div/input").send_keys(Keys.CONTROL + "a")
                        time.sleep(1)
                        prise_tin3_1_1 = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/div/div/input").send_keys(Keys.DELETE)
                        prise_tin3_1_1 = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/div/div/input").send_keys(prise_tin3)
                        sell = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div[8]/div/button").click()
                        print ("Старая цена: " + str(i) + "  Новая цена: " + str(prise_1) + " Выставляю на продажу за + 10 : " + str(prise_1))
                    except:
                        print ("Ошибка при продажи")
                        pass

    flag_buy += 1
    try:
        buy_call = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[4]/div[1]/div/span[2]").text
        buy_call = buy_call.replace(' USDT','')
        buy_call = buy_call.replace(' ','')
        buy_call = float(buy_call)
        if flag_buy % 1 == 0 and buy_call > 0.1:
            if prise_1 < prise_2  and prise_2 != 0:
                #prise_button_1 = driver.find_element_by_xpath("/html/body/div[1]/main/div/section/div[3]/div[2]/div/div[1]/div/div[9]/div/div[1]/div[2]/div[4]/div/div[1]/div/div/div[2]/div/div[1]/div/div/div[1]/div/input").send_keys(buy_prise)
                try:
                    ps_2 = float(buy_my_prise) - 0.0020
                    ps_2 = str(ps_2)
                    prise_tin3_3_1 = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/div/div/input").send_keys(Keys.CONTROL + "a")
                    time.sleep(1)
                    prise_tin3_1_1 = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/div/div/input").send_keys(Keys.DELETE)
                    prise_tin3_1_1 = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/div/div/input").send_keys(ps_2)
                    buy = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[8]/div/button").click()
                    print ("Старая цена: " + str(prise_2) + "  Новая цена: " + str(prise_1) + "Выставляю на покупку за: " + str(ps_2))
                    time.sleep(1)
                    const_buy= driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/div/div/input").send_keys("0.1")
                    list_prise.append(int(prise_1))
                except:
                    print ("Ошибка при покупки")
    except:
        print ("Ошибка при подсчете возможных покупок!!!")
        pass

    prise_2 = prise_1
    print (list_prise)
    time.sleep(1)
while i2 == True:
    try:
        k = 0
        #check()
        index +=1
        print (index)                                                                                             # Парсим цену
        price2 = check()
        #with open("C:/broker/log.txt", "a") as file:
        #    file.write(str(" " + str(price2)))
        print ("Старая цена : " + str(prise1))
        print ("Новая цена : " + str(price2))
        print (my_paper)
        try:
            button_exit = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div[3]/button").click()
            print ("Убрал нежелательный урон")
        except:
            print ("Нет нежелательного элемента")
        if price2 != prise1 and prise1 != 0 and len(str(price2)) == 5 :
            try:                                                                                                # Если цена изменилась и старая цена не равна 0 то:
                if price2 < prise1 : # покупаю                                                                  # Если новая цена меньше старой то:
                    difference = prise1 - price2
                    try:
                        if difference > 20:
                            print ("Разница : " +str(difference))
                            time.sleep(2)
                            bytton_fast_buy = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/form/button").click()                                                        # Покупаю
                            time.sleep(4)
                            button_3 = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div[2]/div/div/div/div").click()
                            time.sleep(4)
                            prise = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/ul[1]/li[1]/div[2]")
                            #global prise_2
                            prise_2 = prise.text
                            prise_2 = prise_2.replace(" ","")
                            prise_2 = prise_2.replace("₽","")
                            prise_2 = prise_2.replace(",","")
                            prise_2 = prise_2.replace("\u202f\u202f", "")
                            print(prise_2)
                            time.sleep(10)
                            button_exit = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div[3]/button").click()
                            my_paper.insert(0,prise_2)
                            buy()
                            with open("C:/broker/log.txt", "a", encoding="utf-8") as file:
                                file.write(" " + str(prise_2))
                            print ("/////////////////////Покупаю")
                            #with open("C:/broker/log.txt", "w") as file:
                            #    file.write(str(my_paper))                                                          # В список добавляется купленная акция
                            #print ("Комиссия : " + str(price2*0.025))
                        else:
                            print ('Маленькая цена для покупки :'+ str(difference))
                    except NoSuchElementException:
                        print ("Повторная покупка ошибка : NoSuchElementException")
                        print ("Не купил")
                        buy()
                        pass
                    except WebDriverException:
                        print ("Повторная покупка ошибка : WebDriverException")
                        print ("Не купил")
                        pass
                    except ElementClickInterceptedException:
                        print ("Повторная покупка ошибка : ElementClickInterceptedException")
                        print ("Не купил")
                        pass

            except TypeError:
                pass
            except NoSuchElementException:
                pass
    except:
        pass
    #else:
        #if prise1  == 0:                                                                            # Если старая цена равна 0 то:
            #prise1 = price2
    #prise1 = price2
