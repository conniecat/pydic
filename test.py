#coding=utf-8
import hashlib
import time
from pydic import hashtable

def test_list():
    dic = {}
    dic.setdefault('1', ['aaaa'])
    print dic['1']
    dic['1'].append('bbbbbb')
    print dic['1']


def test_dic():
    htable = hashtable(6)
    for i in range(1, 1000):
        key = hashlib.md5(str(time.time())).hexdigest()
        htable.add(key, key)
        if i%10 == 0:
            htable.print_table()
        time.sleep(0.33)


test_dic()

