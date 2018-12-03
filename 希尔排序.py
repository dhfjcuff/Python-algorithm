# -*- coding:utf-8 -*-
def shell_sort(alist):
    """希尔排序"""
    n = len(alist)
    gap = n // 2

    i = 1
    while gap > 0:
        for j in range(gap, n):
            i = j
            while i > 0:
                if alist[i] < alist[i - gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                    i -= gap
                else:
                    break
        gap //= 2


if __name__ == '__main__':
    list = [3, 6, 2, 8, 6, 9, 1]
    shell_sort(list)
    print(list)