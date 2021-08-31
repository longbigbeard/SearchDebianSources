import json
import os
import requests


def get_request_info(url):
    response = requests.get(url, proxies={'http': '10.2.3.45:8118'})
    return response


def get_file_info(file):
    with open(file) as f:
        infos = f.readlines()
        return [i.strip("\n") for i in infos]


def search_from_db(file_name):
    if not os.path.isfile(file_name + '_db.json'):
        return {}
    with open(file_name + '_db.json') as f:
        if f.readlines():
            f.seek(0)
            return json.loads(f.read())
        else:
            return {}


def save_to_db(file_name, data_dict):
    with open(file_name + '_db.json', 'w') as f:
        f.write(json.dumps(data_dict, indent=4))
