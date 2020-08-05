import time
for i in range(10):
    time.sleep(0.5)
    print(('*'*i+' '*(10-i)+'第 {}/{} 轮').format(i+1,10),end='\r')



from tqdm import tqdm
t=[]
for i in tqdm(range(10)):
    time.sleep(0.5)


bar=tqdm(range(10))
for i in bar:
    time.sleep(0.5)
    bar.set_description('第{}轮'.format(i))


