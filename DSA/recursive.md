

## 递归与动态规划算法

### 递归算法

递归常与分治思想（Divide and Conquer）同时使用，一般的想法都是我们把问题分成很多个小问题，然后先处理这些小问题，最后将这些问题合并。递归算法的一个基本特征就是包含对自身的调用。



#### 汉诺塔问题

汉诺塔问题应该算是递归算法的一个最简单的案例了。

```python
def hannoi(n,from_tower,mid_tower,to_tower):
    if n==1:
        print('Move {} to {}'.format(from_tower,to_tower))
    else:
        hannoi(n-1,from_tower,to_tower,mid_tower)
        print('Move {} to {}'.format(from_tower,to_tower))
        hannoi(n-1,mid_tower,from_tower,to_tower)

hannoi(3,'A','B','C')
```



#### 排序算法

快速快速或者归并排序都是递归思想的运用



> 递归算法是一个很好的方法，然而递归算法在很多情况下的计算效率是很低的。举例来说，比如用递归实现斐波那契问题:

```python
def fab(n):
	if n==1 or n==2:
		return 1
	else:
		return fab(n-1)+fab(n-2)
```

简单的分析，我们可以发现，这个算法的计算复杂度是 $$O(2^n)$$, 其主要原因在于做了过多的重复计算，当然我们可以使用空间来换时间，从而降低算法的复杂度。

```python
def fab(n,ser):
    if n==1 or n==2:
        return 1
    elif n<=len(ser):
        return ser[n-1]
    else:
        f=fab(n-1,ser)+fab(n-2,ser)
        ser.append(f)
        return f
print(fab(10,[1,1]))
```

用list实现的略微有点怪，最好还是用数组或者dict。



## 动态规划算法

针对上述的很多问题，我们都是在用递归算法解。递归算法是一种逆向思维，那么我们是否存在一些使用正向思维的有效算法的，答案是有的，这就是我们要介绍的动态规划。

这两种方法各有优劣，最关键的是看问题本身以及看思维的习惯。

