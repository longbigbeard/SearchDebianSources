import requests


def get_request_info(url):
    response = requests.get(url, proxies={'http':'10.2.3.45:8118'})

    return response

def get_file_info(file):
    with open(file) as f:
        infos = f.readlines()
        return [i.strip("\n") for i in infos]
