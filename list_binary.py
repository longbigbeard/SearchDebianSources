from bs4 import BeautifulSoup
from utils import get_request_info

def get_list_binary(search_name, code_name):
    base_url = 'https://packages.debian.org/source/'

    response = get_request_info(base_url + code_name + '/' + search_name)
    if response.status_code != 200:
        print('获取失败，错误代码：', response.status_code)
        print(response.text)

    soup = BeautifulSoup(response.text, 'html.parser')
    a = soup.select('#pbinaries > dl > dt > a')
    for b in a:
        print(b.get_text(), end=' ')

    dsc_link = soup.select_one('#pdownload > table > tr:nth-child(2) > td:nth-child(1) > a')
    if dsc_link:
        print('|', dsc_link.get_attribute_list('href')[0]) if len(dsc_link.get_attribute_list('href')) > 0 else print('|')
    else:
        print("查无")