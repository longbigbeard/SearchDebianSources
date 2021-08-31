from bs4 import BeautifulSoup
from utils import get_request_info, search_from_db, save_to_db


def get_source_name(search_name, code_name):
    data_dict = search_from_db(code_name)
    result = data_dict.get(search_name)
    if result:
        print(result)
        return

    base_url = 'https://packages.debian.org/'
    response = get_request_info(base_url + code_name + '/' + search_name)
    if response.status_code != 200:
        print('获取失败，错误代码：', response.status_code)
        print(response.text)

    soup = BeautifulSoup(response.text, 'html.parser')
    source_name = soup.select('#psource a')
    dsc_link = soup.select_one('#pmoreinfo > ul:nth-child(6) > li:nth-child(1) > a')

    if len(source_name) > 0:
        if len(dsc_link.get_attribute_list('href')) > 0:
            dsc_link = dsc_link.get_attribute_list('href')[0]
        else:
            dsc_link = ''
        result = source_name[0].get_text() + '  ||  ' + dsc_link
        print(result)
        data_dict[search_name] = result
        save_to_db(code_name, data_dict)
    else:
        print('查无')
