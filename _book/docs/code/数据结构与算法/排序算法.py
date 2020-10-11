import numpy as np

##测试装饰器
def print_format(func):
    def wrapper(*args):
        print('未排序之前的数组为{}'.format(*args))
        arr=func(*args)
        print('排序之后的数组为{}'.format(arr))
    return wrapper

##插入排序
@print_format
def insert_sort(arr):
    print('开始进行插入排序')
    for i in range(1, len(arr)):
        key = arr[i]
        j = i
        while j >= 1 and key <= arr[j - 1]:
            arr[j] = arr[j - 1]
            j = j - 1
        arr[j] = key
    return arr
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
## 希尔排序
def shell_sort(arr):
    gap = len(arr)//2
    while gap>0:
        for i in range(gap):
            gap_insert_sort(arr,i,gap)
        gap = gap //2
    return arr
def gap_insert_sort(arr,start,gap):
    for i in range(start+gap,len(arr),gap):
        current = arr[i]
        position = i
        while position>=gap and current < arr[position-gap]:
            arr[position] = arr[position-gap]
            position = position -gap 
        arr[position] = current


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

##快速排序
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


@print_format
def quick_sort_type2(arr):
    '''
    这才是快速排序的最好的实现，这种实现下，不占额外的内存，而且可以实现O(nlogn)的速度
    但是写起来比较复杂，上面实现的快速排序理解起来就比较简单了
    '''
    quick_sort_helper(arr,0,len(arr)-1)

def quick_sort_helper(arr,first,last):
    if first<last:
        splitpoint = partition(arr,first,last)
        quick_sort_helper(arr,first,splitpoint-1)
        quick_sort_helper(arr,splitpoint+1,last)
def partition(arr,first,last):
    pivot = arr[first]
    left = first + 1
    right = last 
    done = False
    while not done:
        while left <= right and arr[left]<=pivot:
            left = left +1
        while left <= right and arr[right]>=pivot:
            right = right -1
        if right < left:
            done = True
        else:
            arr[left],arr[right] = arr[right],arr[left]
    arr[first], arr[right] = arr[right],arr[first]
    return right

if __name__=='__main__':
    arr = list(np.arange(0, 11, 1)) 
    np.random.shuffle(arr)
    quick_sort_type2(arr)
    print(arr)
