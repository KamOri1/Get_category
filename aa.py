import time
import datetime

timestamp = 1722859276.2271252
timestamp2 = 1722859761.3080454

# Konwersja timestamp na obiekt datetime
dt_object = datetime.datetime.fromtimestamp(timestamp)
dt_object1 = datetime.datetime.fromtimestamp(timestamp2)
# Formatowanie daty i czasu
print(dt_object.strftime("%H:%M:%S"))
print(dt_object1.strftime("H:%M:%S"))
print(datetime.datetime.now().strftime("%H:%M:%S"))


a = {
    'cat1': {
             'at': 'https://www.beliani.at/gartenmobel/lounge-mobel/',
             'co.uk': 'https://www.beliani.co.uk/outdoor-furniture/lounge-sets/?sort=default',
             'de': 'https://www.beliani.de/gartenmobel/lounge-mobel/?sort=default',
             'pl': 'https://www.beliani.pl/meble-ogrodowe/zestawy-wypoczynkowe/?sort=default',
             'fr': 'https://www.beliani.fr/mobilier-de-jardin/salons-de-jardin/?sort=default',
             'es': 'https://www.beliani.es/muebles-de-exterior/conjuntos-de-jardin/?sort=default',
             'hu': 'https://www.beliani.hu/kulter/lounge-butorok/?sort=default',
             'it': 'https://www.beliani.it/arredo-giardino/salotti-da-giardino/?sort=default',
             'se': 'https://www.beliani.se/utemobler/loungemobler/?sort=default',
             'pt': 'https://www.beliani.pt/mobiliario-de-jardim/conjuntos-de-jardim/?sort=default',
             'dk': 'https://www.beliani.dk/havemoebler/loungemobler/?sort=default',
             'cz': 'https://www.beliani.cz/venkovni-nabytek/zahradni-soupravy/?sort=default',
             'fi': 'https://www.beliani.fi/ulkokalusteet/ulkosohvaryhmat/?sort=default',
             'nl': 'https://www.beliani.nl/tuinmeubels/loungemeubels/?sort=default',
             'no': 'https://www.beliani.no/hagemobler/loungemobler/?sort=default',
             'sk': 'https://www.beliani.sk/zahradny-nabytok/zahradne-supravy/?sort=default'
             },
    'cat2': {
             'at': 'https://www.beliani.at/gartenmobel/gartenmobel-sets/?sort=default',
             'co.uk': 'https://www.beliani.co.uk/outdoor-furniture/garden-dining-sets/?sort=default',
             'de': 'https://www.beliani.de/gartenmobel/gartenmobel-sets/?sort=default',
             'pl': 'https://www.beliani.pl/meble-ogrodowe/zestawy-stol-z-krzeslami/looks/?sort=default',
             'fr': 'https://www.beliani.fr/mobilier-de-jardin/sets-de-jardin/?sort=default',
             'es': 'https://www.beliani.es/muebles-de-exterior/comedores-de-exterior/?sort=default',
             'hu': 'https://www.beliani.hu/kulter/kerti-butor-szett/?sort=default',
             'it': 'https://www.beliani.it/arredo-giardino/set-da-giardino/?sort=default',
             'se': 'https://www.beliani.se/utemobler/utemobelgrupper/?sort=default',
             'pt': 'https://www.beliani.pt/mobiliario-de-jardim/mesa-e-cadeiras-de-jardim/?sort=default',
             'dk': 'https://www.beliani.dk/havemoebler/haveset/?sort=default',
             'cz': 'https://www.beliani.cz/venkovni-nabytek/zahradni-jidelni-sady/?sort=default',
             'fi': 'https://www.beliani.fi/ulkokalusteet/puutarhakalustesetit/?sort=default',
             'nl': 'https://www.beliani.nl/tuinmeubels/tuinmeubelsets/?sort=default',
             'no': 'https://www.beliani.no/hagemobler/utendoers-spisegrupper/?sort=default',
             'sk': 'https://www.beliani.sk/zahradny-nabytok/zahradne-jedalenske-sady/?sort=default'
            },
    'cat3': {
             'at': 'https://www.beliani.at/gartenmobel/balkonmoebel/?sort=default',
             'co.uk': 'https://www.beliani.co.uk/outdoor-furniture/balcony-furniture/?sort=default',
             'de': 'https://www.beliani.de/gartenmobel/balkonmoebel/?sort=default',
             'pl': 'https://www.beliani.pl/meble-ogrodowe/meble-balkonowe/?sort=default',
             'fr': 'https://www.beliani.fr/mobilier-de-jardin/set-de-terrasse/?sort=default',
             'es': 'https://www.beliani.es/muebles-de-exterior/muebles-de-patio/?sort=default',
             'hu': 'https://www.beliani.hu/kulter/terasz-es-erkely-butorok/?sort=default',
             'it': 'https://www.beliani.it/arredo-giardino/patio-e-terrazzo/?sort=default',
             'se': 'https://www.beliani.se/utemobler/balkongmobler/?sort=default',
             'pt': 'https://www.beliani.pt/mobiliario-de-jardim/patio-e-terraco/?sort=default',
             'dk': 'https://www.beliani.dk/havemoebler/altanmobler/?sort=default',
             'cz': 'https://www.beliani.cz/venkovni-nabytek/balkonovy-nabytek/?sort=default',
             'fi': 'https://www.beliani.fi/ulkokalusteet/parvekekalusteet/?sort=default',
             'nl': 'https://www.beliani.nl/tuinmeubels/balkon-en-terrasmeubels/?sort=default',
             'no': 'https://www.beliani.no/hagemobler/balkongmoebler/?sort=default&Pris=1549.00-21759.00',
             'sk': 'https://www.beliani.sk/zahradny-nabytok/balkonovy-nabytok/?sort=default'
            },
    'cat4': {
             'at': 'https://www.beliani.at/sonnenschutz/',
             'co.uk': 'https://www.beliani.co.uk/parasols/', 
             'de': 'https://www.beliani.de/sonnenschutz/',
             'pl': 'https://www.beliani.pl/parasole/',
             'fr': 'https://www.beliani.fr/protections-solaires/',
             'es': 'https://www.beliani.es/sombrillas-y-toldos-vela/',
             'hu': 'https://www.beliani.hu/kulteri-arnyekolok/',
             'it': 'https://www.beliani.it/ombrelloni-e-parasoli-solari/',
             'se': 'https://www.beliani.se/solskydd/',
             'pt': 'https://www.beliani.pt/guarda-sois-e-acessorios/',
             'dk': 'https://www.beliani.dk/solbeskyttelse/',
             'cz': 'https://www.beliani.cz/slunecniky-a-rolety/',
             'fi': 'https://www.beliani.fi/aurinkovarjot-ja-jalustat/',
             'nl': 'https://www.beliani.nl/zonbescherming-en-accessoires/',
             'no': 'https://www.beliani.no/solskjerming/',
             'sk': 'https://www.beliani.sk/slnecniky-a-tienidla/'
            }
}