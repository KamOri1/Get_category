import threading
import time
#działająca wersja do użytku

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import datetime
import URLSearchParams as ss

PATH_ACCEPT_COOKIE = '//*[@id="cookie_warning"]/div[2]/div[1]/div[3]/input[2]'
PATH_DROP_DOWN_LEANGUAGE_LIST = '//*[@id="header"]/div[2]/div[1]/div[9]/p'
PATH_CLICK_LEANGUAGE = '//*[@id="header"]/div[2]/div[1]/div[9]/ul/li[1]/a'
cat_all = {
            'cat1':{},
            'cat2':{},
            'cat3':{},
            'cat4':{},
        }
class CollectCategory:
    def __init__(self, cat_all, **kwargs):
        self.category_oryginal_links = kwargs
        self.countres = ['at', 'co.uk', 'de', 'pl', 'fr', 'es', 'hu','it', 'se', 'pt', 'dk', 'cz', 'fi', 'nl', 'no', 'sk']
        self.options = Options()
        self.options.add_argument("--headless")
        self.options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome(options=self.options)

        self.cat_all = cat_all



    def choiceCorrectLang(self, countre, link) -> None:
        self.driver.get(f'https://www.beliani.{countre}\\{link}')
        element = self.driver.find_element(By.XPATH, value=PATH_ACCEPT_COOKIE)
        if element.is_displayed():
            element.click()
        element = self.driver.find_element(By.XPATH, value=PATH_DROP_DOWN_LEANGUAGE_LIST)
        element.click()
        element = self.driver.find_element(By.XPATH, value=PATH_CLICK_LEANGUAGE)
        element.click()
        time.sleep(1)


    def saveAllCategory(self) -> dict :
        loop_count = 1

        for countre in self.countres:
            for category, link in self.category_oryginal_links.items():
                try:
                    self.choiceCorrectLang(countre, link)
                    current_url = self.driver.current_url

                    if category == 'Cat_1':
                        self.cat_all['cat1'][countre] = current_url
                    elif category == 'Cat_2':
                        self.cat_all['cat2'][countre] = current_url
                    elif category == 'Cat_3':
                        self.cat_all['cat3'][countre] = current_url
                    elif category == 'Cat_4':
                        self.cat_all['cat4'][countre] = current_url

                    print(f"{category} - {loop_count}: {countre} ✓")
                    loop_count += 1
                except Exception as e:
                    print(f"{category} : {countre} x")

        print(self.cat_all)
        return {}



# a = CollectCategory(
#                     first='/outdoor-furniture/lounge-sets/',
#                     sec='/outdoor-furniture/garden-dining-sets/',
#                     three='/outdoor-furniture/balcony-furniture/',
#                     four='/parasols/'
#                     ).saveAllCategory()


ae = {'cat1': {'at': 'https://www.beliani.at/gartenmobel/alle+produkte/?Material=Rattan,Massivholz&sort=default', 'co.uk': 'https://www.beliani.co.uk/outdoor-furniture/all+products/?Material=Rattan,Wood&sort=default'}, 'cat2': {'at': 'https://www.beliani.at/gartenmobel/alle+produkte/?Material=Rattan&sort=default', 'co.uk': 'https://www.beliani.co.uk/outdoor-furniture/all+products/?Material=Rattan&sort=default'}, 'cat3': {}, 'cat4': {}}
def zadanie_a():
    # Kod dla obiektu a
    print("Zaczęto zadanie A")
    a = CollectCategory(cat_all,
        Cat_1='/outdoor-furniture/lounge-sets/',

    ).saveAllCategory()


    print("Zakończono zadanie A")

def zadanie_b():
    # Kod dla obiektu b
    print("Zaczęto zadanie B")
    b = CollectCategory(cat_all,

        Cat_2='/outdoor-furniture/garden-dining-sets/',

    ).saveAllCategory()


    print("Zakończono zadanie B")

def zadanie_c():
    # Kod dla obiektu b
    print("Zaczęto zadanie C")
    c = CollectCategory(cat_all,

        Cat_3='/outdoor-furniture/balcony-furniture/',

    ).saveAllCategory()


    print("Zakończono zadanie C")

def zadanie_d():
    # Kod dla obiektu b
    print("Zaczęto zadanie D")
    d = CollectCategory(cat_all,

        Cat_4='/parasols/'
    ).saveAllCategory()
    print("Zakończono zadanie D")


task_a = threading.Thread(target=zadanie_a)
task_b = threading.Thread(target=zadanie_b)
task_c = threading.Thread(target=zadanie_c)
task_d = threading.Thread(target=zadanie_d)
A_time = datetime.datetime.now().strftime("%H:%M:%S")
task_a.start()
task_b.start()
task_c.start()
task_d.start()

task_a.join()

task_b.join()

task_c.join()

task_d.join()
print(cat_all)
print('start time', A_time)
print('end time ', datetime.datetime.now().strftime("%H:%M:%S"))