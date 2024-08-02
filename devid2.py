import math

def devid(f:list,g:list):
    tmp=[]

    if(len(f)<len(g)):
        return g,f

    product = f[len(f)-1]/g[len(g)-1]

    for i in range(0,len(g)):
        tmp.append(f[len(f)-1-i]-(g[len(g)-i-1]*product))
    for i in range(len(f)-len(g)-1,-1,-1):
        tmp.append(f[i])
    
    count=len(tmp)
    for i in range(0,len(tmp)):
        if(tmp[i]!=0):
            count=i
            break
    
    del(tmp[0:count])
    tmp.reverse()
    return devid(tmp,g)

def poly_gcd(f:list,g:list):
    gcd = []
    while(True):
        r = devid(f,g)
        print(r)
        if(r[1]==[]):
            gcd = g
            break
        f=r[0]
        g=r[1]
    gcd = [gcd[i]/abs(gcd[0]) for i in range(0,len(gcd))]
    return gcd

f=[-2,7,-4,-7,6]
g=[1,-2,1]
print(poly_gcd(f,g))