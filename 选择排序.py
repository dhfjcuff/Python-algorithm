# -*- coding:utf-8 -*-
def selecvt_sort(alist):
    n = len(alist)
    for j in range(n-1):
        m = j
        for i in range(j+1, n):
            if alist[m] > alist[i]:
                m = i
        alist[j], alist[m] = alist[m], alist[j]


if __name__ == '__main__':
    list = [1, 4, 6, 3, 8, 4]
    selecvt_sort(list)
    print(list)