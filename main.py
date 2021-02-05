#!/usr/bin/env python3

from sys import argv
from getopt import gnu_getopt
from get_source import get_source_name
from list_binary import get_list_binary
from utils import get_file_info


def usage():
    info = """
main -h
main -a <action> -n <search_name> [ -c <code_name> -f <file> ]
    -h 
        usage
    -a <action>
        action: get_source[default], list_binary
    -n <search_name>
        search_name: package or source name 
    -c <code_name>
        code_name: buster[default], stretch, jessie
    -f <file>
        file contain package or source name
    """
    print(info)


if __name__ == '__main__':
    action_list = ['get_source', 'list_binary']
    action = 'get_source'
    search_name = ''
    code_name = 'buster'
    file_name = ''

    opts, _ = gnu_getopt(argv[1:], 'ha:n:c:f:')
    if not opts:
        print("参数错误， -h查看")
        exit()
    for o, v in opts:
        if o == '-h':
            usage()
            exit()
        elif o == '-a' and v:
            if v not in action_list:
                print("未知行为")
                exit()
            action = v
        elif o == '-n' and v:
            search_name = v
        elif o == '-c' and v:
            code_name = v
        elif o == '-f' and v:
            file_name = v
    if not search_name and not file_name:
        print("单个搜索名称为必须")
        exit()

    if action == 'get_source':
        if file_name:
            search_list = get_file_info(file_name)
            for search_name in search_list:
                get_source_name(search_name, code_name)
        else:
            get_source_name(search_name, code_name)

    elif action == 'list_binary':
        if file_name:
            search_list = get_file_info(file_name)
            for search_name in search_list:
                get_list_binary(search_name,code_name)
        else:
            get_list_binary(search_name, code_name)