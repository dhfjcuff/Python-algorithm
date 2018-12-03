# -*- coding:utf-8 -*-
def insert_sort(alist):
    n = len(alist)
    for j in range(1, n):
        i = j
        while i > 0:
            print('a', alist[i], alist[i - 1])
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                print(alist[i], alist[i - 1])
                i -= 1
            else:
                break


if __name__ == '__main__':
    list = [1, 99, 2, 7, 66, 8]
    insert_sort(list)
    print(list)

#优化
# def insert_sort(alist):
#     # 从第二个位置，即下标为1的元素开始向前插入
#     for i in range(1, len(alist)):
#         # 从第i个元素开始向前比较，如果小于前一个元素，交换位置
#         for j in range(i, 0, -1):
#             if alist[j] < alist[j-1]:
#                 alist[j], alist[j-1] = alist[j-1], alist[j]
#
# alist = [54,26,93,17,77,31,44,55,20]
# insert_sort(alist)
# print(alist)