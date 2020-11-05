import requests
import re

portals = {'gumtree': {'url': 'https://www.gumtree.pl/s-mieszkania-i-domy-sprzedam-i-kupie/v1c9073p1', 'reg':'(?<=class="pag-box pag-box-last" href="/s-mieszkania-i-domy-sprzedam-i-kupie/page-)(.*)(?=\/v1c9073p50">)',
                     'szablon': 'https://www.gumtree.pl/s-mieszkania-i-domy-sprzedam-i-kupie/page-{page_number}/v1c9073p{page_number}'},
          'olx': {'url': 'https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/', 'reg':'(?<=data-cy="page-link-last">\n\t\t\t<span>)(.*)(?=<\/span>)',
                 'szablon': 'https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/?page={page_number}'},
          'otodom': {'url': 'https://www.otodom.pl/sprzedaz/mieszkanie/?nrAdsPerPage=72#', 'reg': '(?<=placeholder=")(.*)(?=" class="input)',
                    'szablon': 'https://www.otodom.pl/sprzedaz/mieszkanie/?nrAdsPerPage=72&page={page_number}'}}

# for i in range(1, 51):
#     print(portals['gumtree']['szablon'].format(page_number = i))


def find(url: str, reg: str, szablon: str):
    response = requests.get(url)
    last_page = re.findall(reg, str(response.content.decode('utf-8')))
    for i in range(int(last_page[0])+1):
        print(szablon.format(page_number=i))




def page():
    for k, v in portals.items():
        print(f"Przeszukuje portal {k}")
        find(url=v["url"], reg=v["reg"], szablon=v["szablon"])