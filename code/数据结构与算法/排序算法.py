import numpy as np
##插入排序
def insert_sort(arr):
    print('开始进行插入排序')
    for i in range(1, len(arr)):
        key = arr[i]
        j = i
        while j >= 1 and key <= arr[j - 1]:
            arr[j] = arr[j - 1]
            j = j - 1
        arr[j] = key
##选择排序
def selection_sort(arr):
    print('开始进行选择排序')
    for i in range(0,len(arr)):
        key_index=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[key_index]:
                key_index=j
        arr[i],arr[key_index]=arr[key_index],arr[i]
## 冒泡排序
def bubble_sort(arr):
    print('开始进行冒泡排序')
    for j in range(len(arr)-1,1,-1):
        for i in range(0,j):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]

###归并排序
def merge(l_arr,u_arr):
    new_arr=[]
    while len(l_arr)>0 and len(u_arr)>0:
        if l_arr[0]>u_arr[0]:
            new_arr.append(u_arr.pop(0))
        else:
            new_arr.append(l_arr.pop(0))
    if len(l_arr)>0:
        new_arr.extend(l_arr)
    if len(u_arr)>0:
        new_arr.extend(u_arr)
    return (new_arr)

def merge_sort(arr):
    if len(arr)<=1:
        return (arr)
    else:
        m=int(len(arr)/2)
        l_arr=merge_sort(arr[:m].copy())
        u_arr=merge_sort(arr[m:].copy())
        return (merge(l_arr,u_arr))




def quick_sort(arr):
    if len(arr)<=1:
        return (arr)
    else:
        mid = arr[int(len(arr)/2)]
        arr.remove(mid)
        l_array,u_array=[],[]
        for item in arr:
            if item>=mid:
                u_array.append(item)
            else:
                l_array.append(item)
    return quick_sort(l_array)+[mid]+quick_sort(u_array)


def main_sort(method):
    arr = list(np.arange(0, 11, 1))
    np.random.shuffle(arr)
    print('未排序之前的数组为{}'.format(arr))
    arr=method(arr)
    print('排序之后的数组为{}'.format(arr))


if __name__=='__main__':
    main_sort(quick_sort)

