import requests
import re

def find (url, my_reg):
    response = requests.get(url)
    last_page = re.findall(my_reg, str(response.content.decode('utf-8')))
    for i in range(int(last_page[0])+1):
        print(url + "" + str(i))