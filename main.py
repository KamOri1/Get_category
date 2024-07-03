from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import URLSearchParams as ss
import pandas as pd
lista = [
         'garden-furniture/outdoor-furniture/lounge-sets/?Material=Fabric',
         'garden-furniture/outdoor-furniture/lounge-sets/?Material=Metal',
         'garden-furniture/outdoor-furniture/lounge-sets/?Material=Rattan',
         'garden-furniture/outdoor-furniture/lounge-sets/?Material=Wood']
list_dict = {
'1' : 'garden-furniture/outdoor-furniture/lounge-sets/?Material=Fabric',
# '2' : 'garden-furniture/outdoor-furniture/lounge-sets/?Material=Metal',
# '3' : 'garden-furniture/outdoor-furniture/lounge-sets/?Material=Rattan',
# '4' : 'garden-furniture/outdoor-furniture/lounge-sets/?Material=Wood',
}
countres = ['at', 'hu', 'pt', 'se', 'co.uk', 'dk']


def het_category_filtr():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    cat1={}
    cat2={}
    cat3={}
    cat4={}
    filter_names = []
    filter_values = []
    filter_values1 = []
    filter_values2 = []
    filter_values3 = []
    filter_values4 = []
    for countre in countres:
        for category, link in list_dict.items():
            driver.get(f'https://www.beliani.{countre}\\{link}')
            element = driver.find_element(By.XPATH, '//*[@id="cookie_warning"]/div[2]/div[1]/div[3]/input[2]')

            if element.is_displayed():

                element.click()


            element = driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div[1]/div[9]/p')
            element.click()

            element = driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div[1]/div[9]/ul/li[1]/a')
            element.click()
            time.sleep(1)
            current_url = driver.current_url
            src = ss.URLSearchParams(current_url)
            sas = ss.URLSearchParams(link)
            print(sas.getAll())
            print(src.getAll())
            print(src.getAll()[0].split('='))
            a = {
                    'slug': countre,
                    sas.getAll()[0].split('=')[0] : src.getAll()[0].split('=')[0]
                }
            b = {
                    'slug': countre,
                     sas.getAll()[0].split('=')[1] : src.getAll()[0].split('=')[1]
                }
            if a not in filter_names:
                filter_names.append(a)
            if b not in filter_names:
                filter_values.append(b)
            if category == '1':
                cat1[countre] = current_url
            elif category == '2':
                cat2[countre] = current_url
            elif category == '3':
                cat3[countre] = current_url
            elif category == '4':
                cat4[countre] = current_url

            if category == '1':
                filter_values1.append(b)
            elif category == '2':
                filter_values2.append(b)
            elif category == '3':
                filter_values3.append(b)
            elif category == '4':
                filter_values4.append(b)

            #print(current_url)
    print(cat1)
    print(cat2)
    print(cat3)
    print(cat4)
    # print(filter_names)
    # print(filter_values)
    print(filter_names)
    print(filter_values1)
    print(filter_values2)
    print(filter_values3)
    print(filter_values4)
    print('==================================================')
    df = pd.DataFrame(filter_values1)

    print(df.to_csv(index=False))
het_category_filtr()

# filter names
# list = [
#     {
#         'slug':'countre',
#         "Material":src.getAll()[0].split('=')[0]
#     },
#
# ]
#
# filter values
a = [
    {'slug': 'at', 'Material': 'Stoff'},
     {'slug': 'at', 'Material': 'Metall'},
     {'slug': 'at', 'Material': 'Rattan'},
     {'slug': 'at', 'Material': 'Massivholz'},
     {'slug': 'hu', 'Material': 'Anyag'},
     {'slug': 'hu', 'Material': 'Fem'},
     {'slug': 'hu', 'Material': 'Rattan'},
     {'slug': 'hu', 'Material': 'Kemenyfa'}
]