# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Copyright 2021 zhangt2333. All Rights Reserved.
# Author-Github: github.com/zhangt2333

import sys
import requests
import re
from bs4 import BeautifulSoup

username = ''

def hw1():
    response = requests.get('https://raw.githubusercontent.com/{}/hw-gitBranchAndCommit/theLooooooooooongestBranch/1plus1.txt'.format(username))
    sys.exit(0 if '1+1=2' in response.text.strip().replace(' ', '') else -1)

def hw2():
    response = requests.get('https://raw.githubusercontent.com/{}/hw-gitBranchAndCommit/usedForRollback/1plus1.txt'.format(username))
    s = response.text.strip().replace(' ', '')
    sys.exit(0 if '1+1=2' in s and '1+2=3' in s and '1+3=4' in s else -1)

methods = [hw1]
if __name__ == '__main__':
    f = open('in.txt', 'r', encoding='utf-8')
    argv = f.read()
    hw_index = int(re.findall(r'I finished homework: `(.*?)`', argv)[0])
    username = re.findall(r'`https://github.com/(.*?)/hw-gitBranchAndCommit`', argv)[0]
    methods[hw_index - 1]()