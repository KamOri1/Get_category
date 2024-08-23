from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import URLSearchParams as ss
import pandas as pd
lista = [
         'garden-furniture/outdoor-furniture/lounge-sets/?Material=Fabric',
         ]
list_dict = {
'1' : 'garden-furniture/outdoor-furniture/all+products/?Material=Rattan,Wood',
# '2' : 'garden-furniture/outdoor-furniture/lounge-sets/?Material=Metal',
# '3' : 'garden-furniture/outdoor-furniture/lounge-sets/?Material=Rattan',
# '4' : 'garden-furniture/outdoor-furniture/lounge-sets/?Material=Wood',
}
countres = ['at', 'co.uk']


def het_category_filtr():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome()
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
            #
            # if ',' in src.getAll()[0].split('=')[1]:
            #     nowe = src.getAll()[0].split('=')[1].split(',')
            #     for kazdy in nowe:
            #         b = {
            #                 'slug': countre,
            #                  sas.getAll()[0].split('=')[1] : kazdy
            #
            #             }
            #         if category == '1':
            #
            #             filter_values1.append(b)
            #         elif category == '2':
            #
            #             filter_values2.append(b)
            #         elif category == '3':
            #
            #             filter_values3.append(b)
            #         elif category == '4':
            #
            #             filter_values4.append(b)
            # else:
            b = {
                'slug': countre,
                sas.getAll()[0].split('=')[1]: src.getAll()[1].split('=')[1]

            }

            # if a not in filter_names:
            #     filter_names.append(a)
            # if b not in filter_names:
            #     filter_values.append(b)
            if category == '1':
                cat1[countre] = current_url
                # filter_values1.append(b)
            elif category == '2':
                cat2[countre] = current_url
                # filter_values2.append(b)
            elif category == '3':
                cat3[countre] = current_url
                # filter_values3.append(b)
            elif category == '4':
                cat4[countre] = current_url
                # filter_values4.append(b)

    print('==================================================')
    print(cat1)
    print(cat2)
    print(cat3)
    print(cat4)
    print('==================================================')
    # print(filter_names)
    # print(filter_values1)
    # print(filter_values2)
    # print(filter_values3)
    # print(filter_values4)
    # print('==================================================')
    # df = pd.DataFrame(filter_values1)
    #
    # print(df.to_csv(index=False))
het_category_filtr()


