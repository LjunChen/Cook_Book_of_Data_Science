# coding=utf-8
'''
author : Liujun Chen
date : 2020/8/5 18:15
'''

from setuptools import  setup
from Cython.Build import cythonize

setup(ext_modules=cythonize('fib.pyx'))

