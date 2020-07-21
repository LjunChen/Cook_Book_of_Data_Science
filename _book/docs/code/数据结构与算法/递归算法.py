### 汉诺塔问题
# def hannoi(n,from_tower,mid_tower,to_tower):
#     if n==1:
#         print('Move {} to {}'.format(from_tower,to_tower))
#     else:
#         hannoi(n-1,from_tower,to_tower,mid_tower)
#         print('Move {} to {}'.format(from_tower,to_tower))
#         hannoi(n-1,mid_tower,from_tower,to_tower)
#
# try :
#     n = int(input("please input a integer :"))
#     print ("移动步骤如下: ")
#     hannoi(n, 'A', 'B', 'C')
# except ValueError:
#     print ("please input a integer n(n > 0)!")

import numpy as np
def fab(n,ser):
    if n==1 or n==2:
        return 1
    elif n<=len(ser):
        return ser[n-1]
    else:
        f=fab(n-1,ser)+fab(n-2,ser)
        ser.append(f)
        return f
print(fab(i,[1,1]))