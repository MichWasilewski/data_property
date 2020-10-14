import requests
#
# for i in range (100):
#     url = "https://www.gumtree.pl/a-mieszkania-i-domy-do-wynajecia/krakow/lokal-biuro-mieszkanie-80m2-3pokoje-ul-syrokomli/1008182916760912555995109"
#     response = requests.get(url)
#     print(response)
# print(response.content)
#
# for i in range (100):
#     url = "https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/q-mieszkania/"
#     response = requests.get(url)
#     print(response)
# print(response.content)

for i in range (100):
    url = "https://www.otodom.pl/sprzedaz/mieszkanie/"
    response = requests.get(url)
    print(response)
print(response.content)


