"""
读取yaml文件
"""

import yaml

def read_yaml(file):
    with open("./data/"+file,"r",encoding="utf8") as f:
        data=list()
        for i in yaml.safe_load(f).values():
            data.append(tuple(i.values()))
    return data


if __name__ == '__main__':
    print(read_yaml("mp_login.yaml"))