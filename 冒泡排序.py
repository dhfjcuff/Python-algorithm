# -*- coding:utf-8 -*-
def bubble_sort(alist):
    """冒泡排序"""
    n = len(alist)
    for j in range(n-1):    # 保证把每个数取到
        for i in range(n-1-j):  # 保证每个都比较
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]


if __name__ == '__main__':
    list = [3, 5, 2, 6, 84, 6, 9]
    bubble_sort(list)
    print(list)