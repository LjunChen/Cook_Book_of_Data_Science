### 排序算法

这里介绍插入，选择，冒泡，归并，快速排序这5种常见的排序算法。当然还有其他算法，这里不加以介绍了。这里的代码不是最优的，没有考虑一些空间的占用问题（特别是对于归并排序和快速排序，其实是不用占用额外空间的），不过比较好理解。

#### 插入排序

插入排序是一种简单直观的排序算法。它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。

从第一个元素，如果第1个元素小于第0个元素，就把第1个元素和第0个元素交换（前2个位置已经排好序）

到第二个元素，如果第2个元素小于第1个元素，就把第2个元素和第1个元素交换，然后比较一直交换到前3个元素排好位置

以此类推....

插入排序的平均时间复杂度是

```python
def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i
        while j >= 1 and key <= arr[j - 1]:
            arr[j] = arr[j - 1]
            j = j - 1
        arr[j] = key
```



#### 选择排序

选择排序是一种简单直观的排序算法。

* 首先找出整个序列中最小的元素，放在第一位
* 然后从未排序的序列中找出最小的，放到已排序序列的末尾

```python
def selection_sort(arr):
    for i in range(0,len(arr)):
        key_index=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[key_index]:
                key_index=j
        arr[i],arr[key_index]=arr[key_index],arr[i]
```



#### 冒泡排序

冒泡排序（Bubble Sort）也是一种简单直观的排序算法。

它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。

走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。

这个算法的名字由来是因为越小的元素会经由交换慢慢"浮"到数列的顶端。

```python
def bubble_sort(arr):
    print('开始进行冒泡排序')
    for j in range(len(arr)-1,1,-1):
        for i in range(0,j):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
```



#### 归并排序

归并排序是递归算法在排序上的应用。或者说是 Divide and Conquer 的一个非常典型的应用。

* 递归地把当前序列平均分割成两半
* 在保持元素顺序的同时将上一步得到的子序列集成到一起（归并）

```python
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
    if len(arr)>=2:
        m=int(len(arr)/2)
        l_arr=merge_sort(arr[:m].copy())
        u_arr=merge_sort(arr[m:].copy())
        return (merge(l_arr,u_arr))

```



#### 快速排序

快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分为较小和较大的2个子序列，然后递归地排序两个子序列。

* 挑选基准值：从数列中挑出一个元素，称为"基准"（pivot）
* 重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面（与基准值相等的数可以到任何一边）。在这个分割结束之后，对基准值的排序就已经完成;
* 递归排序子序列：递归地将小于基准值元素的子序列和大于基准值元素的子序列排序。

递归到最底部的判断条件是数列的大小是零或一，此时该数列显然已经有序。

```python
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
```





