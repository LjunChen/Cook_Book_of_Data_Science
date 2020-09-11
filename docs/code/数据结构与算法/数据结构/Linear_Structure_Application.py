from time_cal import time_cal
from Linear_Structure import Stack
from Linear_Structure import Queue
from Linear_Structure import Deque


def parCheck(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced == True:
        symbol =symbolString[index]
        if symbol == '(':
            s.push('(')
        else:
            if s.size() == 0:
                balanced = False
            else:
                s.pop()
        index +=1
    
    if balanced == True and s.isEmpty():
        return True
    else:
        return False

print(parCheck('(())'))


def hotPotato(namelist,num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)
    
    while simqueue.size() > 1:
        for _ in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()
    return simqueue.dequeue()

print(hotPotato(['a','b','c','d','e','f'],7))


def palchecker(aString):
    chardeque =  Deque()
    for ch in aString:
        chardeque.addRear(ch)
    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual= False
    return stillEqual

print(palchecker('上海自来水来自海上'))


