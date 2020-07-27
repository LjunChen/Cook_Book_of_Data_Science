

import time
import numpy as np
from multiprocessing.dummy import Pool


def run(name):
    a = np.random.randint(0, 10)
    print('Process {} runing, this needs {} seconds '.format(name, a))
    time.sleep(a)
    print('Process {} running end, The return value is {}'.format(name, a))
    return (a)


if __name__ == '__main__':
    p = Pool(4)
    res = []
    for i in range(8):
        res_temp = p.apply_async(run, args=(i,))
        res.append(res_temp)
    p.close()
    p.join()
    print('主线程')
    for res_temp in res:
        print(res_temp.get())
