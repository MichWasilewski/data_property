from utillies import find_page


find_page.find("https://www.gumtree.pl/s-mieszkania-i-domy-sprzedam-i-kupie/v1c9073p1", '(?<=class="pag-box pag-box-last" href="/s-mieszkania-i-domy-sprzedam-i-kupie/page-)(.*)(?=\/v1c9073p50">)')


# print("\nGumtree\n")
# for i in range (100):
#     url = "https://www.gumtree.pl/a-mieszkania-i-domy-do-wynajecia/krakow/lokal-biuro-mieszkanie-80m2-3pokoje-ul-syrokomli/1008182916760912555995109"
#     response = requests.get(url)
#     print(response)
# print(response.content)
# url = "https://www.gumtree.pl/s-mieszkania-i-domy-sprzedam-i-kupie/v1c9073p1"
# response = requests.get(url)
# last_page_gumt = re.findall('(?<=class="pag-box pag-box-last" href="/s-mieszkania-i-domy-sprzedam-i-kupie/page-)(.*)(?=\/v1c9073p50">)',
#                             str(response.content))


find_page.find("https://www.gumtree.pl/s-mieszkania-i-domy-sprzedam-i-kupie/v1c9073p1", '(?<=class="pag-box pag-box-last" href="/s-mieszkania-i-domy-sprzedam-i-kupie/page-)(.*)(?=\/v1c9073p50">)')



# print("\nolx\n")
# url2 = "https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/"
# response = requests.get(url2)
# print(response.content.decode('utf-8'))
# last_page_olx = re.findall('(?<=data-cy="page-link-last">\n\t\t\t<span>)(.*)(?=<\/span>)', str(response.content.decode('utf-8')))
# print(last_page_olx)
# for i in range(int(last_page_olx[0])+1):
#     print(url2 + "?page=" + str(i))



# print("\nOtodom\n")
# url3 = "https://www.otodom.pl/sprzedaz/mieszkanie/?nrAdsPerPage=72#"
# response = requests.get(url3)
# # print(response)
# # print(response.content)
# last_page_otd = re.findall('(?<=placeholder=")(.*)(?=" class="input)', str(response.content))
# print(last_page_otd)
# for i in range(int(last_page_otd[0])+1):
#     print(url3 + "&page=" + str(i))