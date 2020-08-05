# coding=utf-8
'''
author : Liujun Chen
date : 2020/8/5 18:29
'''

import  time
from fib import fib
start=time.time()
result=fib(40)
end=time.time()
print('结果为{}'.format(result))
print('时间为{}'.format(end-start))