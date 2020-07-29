tr={(2,3),(3,4),(4,8),(5,8),(9,10)}
max_w=20
m={}

def chief(tr,w):
    if tr==set() or w==0:
        m[(tuple(tr),w)]=0 ##tuple是key的要求，不能用set做key
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

