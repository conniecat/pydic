#coding=utf-8
import time

# 1 hour, 60*60 second
DELTA_TIME = 3600

class hashtable:
    def __init__(self, size=12):
        self._size = size
        self._mindate = time.time()
        self._table = []
        for i in range(0, self._size):
            self._table.append({})

    def _remove(self):
        if len(self._table) > 0:
            self._table.pop()
            self._table.insert(0, {})

    def _hash(self, key):
        return key[:8]

    def exist(self, key, value):
        index = self._hash(key)
        for dic in self._table:
            if dic.has_key(index):
                for item in dic[index]:
                    if item == value:
                        return True
        return False


    def add(self, key, value):
        if self.exist(key, value):
            return False
        index = self._hash(key)
        dic = self._table[0]
        if dic.has_key(index):
            dic[index].append(value)
        else:
            dic.setdefault(index, [value,])


        if time.time() - self._mindate > DELTA_TIME:
            print 'removed'
            self._remove()
            self._mindate += DELTA_TIME

    def print_table(self):
        for i in range(0, self._size):
            dic = self._table[i]
            print str(i) + ': ' + str(len(dic.items()))
        print '*********************************'


