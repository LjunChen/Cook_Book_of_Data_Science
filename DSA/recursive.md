

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

我们最常用的求斐波那契的过程就是一个动态规划算法的应用。

下面，我们考虑一个博物馆大盗问题，这也是一个很有名的问题。

> 大盗潜入博物馆，面前有5件宝物，分别有重量和价值。大盗的背包仅能负重20kg, 请问如何选择宝物，总价值最高？
>
> | item | weight | Value |
> | ---- | ------ | ----- |
> | 1    | 2      | 3     |
> | 2    | 3      | 4     |
> | 3    | 4      | 8     |
> | 4    | 5      | 8     |
> | 5    | 9      | 10    |
>
> 

我们把$m(i,w)$ 记为前 i 个宝物中，组合不超过w重量，得到的最大价值。

则 $m(i,w)$ 应该为 $m(i-1,w)$ 和 $m(i-1,w-w_i)+v_i$两者最大值。



```python
tr=[None,{'w':2,'v':3},{'w':3,'v':4},{'w':4,'v':8},{'w':5,'v':8},{'w':9,'v':10}]
max_w=20

m={(i,w):0 for i in range(len(tr)) for w in range(max_w+1)}

for i in range(1,len(tr)):
    for w in range(1,max_w+1):
        if tr[i]['w']>w:
            m[(i,w)]=m[(i-1,w)]
        else:
            m[(i,w)]=max(m[(i-1,w)],m[(i-1,w-tr[i]['w'])]+tr[i]['v'])

print(m[(len(tr)-1,max_w)])
```

这个问题也可以用递归算法来解决

```python
tr={(2,3),(3,4),(4,8),(5,8),(9,10)}
max_w=20
m={}

def chief(tr,w):
    if tr==set() or w==0:
        m[(tuple(tr),w)]=0 ##tuple鏄痥ey鐨勮姹傦紝涓嶈兘鐢╯et鍋歬ey
        return 0
    elif (tuple(tr),w) in m:
        return m[(tuple(tr),w)]
    else:
        vmax=0
        for t in tr:
            if t[0] <=w:
                v=chief(tr-{t},w-t[0])+t[1]
                vmax=max(vmax,v)
        m[(tuple(tr),w)]=vmax
        return vmax
print(chief(tr,max_w))
	
```

在这个问题，递归算法可能更加简单（想法上更加简单）。

> p.s. 就我个人的理解，递归（+记忆）在大多数情况下都能完成动态规划所能实现的功能，并且在想法上更加简单。



