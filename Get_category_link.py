#działająca wersja do użytku

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import URLSearchParams as ss

PATH_ACCEPT_COOKIE = '//*[@id="cookie_warning"]/div[2]/div[1]/div[3]/input[2]'
PATH_DROP_DOWN_LEANGUAGE_LIST = '//*[@id="header"]/div[2]/div[1]/div[9]/p'
PATH_CLICK_LEANGUAGE = '//*[@id="header"]/div[2]/div[1]/div[9]/ul/li[1]/a'

class CollectCategory:
    def __init__(self, **kwargs):
        self.category_oryginal_links = kwargs
        self.countres = ['at', 'co.uk', 'de', 'pl', 'fr', 'es', 'hu','it', 'se', 'pt', 'dk', 'cz', 'fi', 'nl', 'no', 'sk']
        self.options = Options()
        self.options.add_argument("--headless")
        self.driver = webdriver.Chrome()
        # self.cat1={}
        # self.cat2={}
        # self.cat3={}
        # self.cat4={}
        self.cat_all = {
            'cat1':{},
            'cat2':{},
            'cat3':{},
            'cat4':{},
        }



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

        for countre in self.countres:
            print(self.countres)
            for category, link in self.category_oryginal_links.items():
               self.choiceCorrectLang(countre, link)
               current_url = self.driver.current_url
               if category == 'first':
                   self.cat_all['cat1'][countre] = current_url
                   #self.cat1[countre] = current_url
               elif category == 'sec':
                    #self.cat2[countre] = current_url
                    self.cat_all['cat2'][countre] = current_url
               elif category == 'three':
                    #self.cat2[countre] = current_url
                    self.cat_all['cat3'][countre] = current_url
               elif category == 'four':
                    #self.cat2[countre] = current_url
                    self.cat_all['cat4'][countre] = current_url
        #print(self.cat1)
        #print(self.cat2)
        print(self.cat_all)
        return {}


a = CollectCategory(
                    first='/outdoor-furniture/lounge-sets/',
                    sec='/outdoor-furniture/garden-dining-sets/',
                    three='/outdoor-furniture/balcony-furniture/',
                    four='/parasols/'
                    ).saveAllCategory()


ae = {'cat1': {'at': 'https://www.beliani.at/gartenmobel/alle+produkte/?Material=Rattan,Massivholz&sort=default', 'co.uk': 'https://www.beliani.co.uk/outdoor-furniture/all+products/?Material=Rattan,Wood&sort=default'}, 'cat2': {'at': 'https://www.beliani.at/gartenmobel/alle+produkte/?Material=Rattan&sort=default', 'co.uk': 'https://www.beliani.co.uk/outdoor-furniture/all+products/?Material=Rattan&sort=default'}, 'cat3': {}, 'cat4': {}}