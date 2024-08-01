def devid(f:list,g:list,quotient:list):
    if(len(f)<len(g)):
        return quotient,f
    tmp = []

    quotient.append(f[0]/g[0])
    if(f[1]==0):
        quotient.append(0)
    for j in range(0,len(g)):
        tmp.append(f[j]-(g[j]*(f[0]/g[0])))
    for j in range(len(g),len(f)):
        tmp.append(f[j])

    count=0
    for i in range(0,len(tmp)):
        if(tmp[i]!=0):
            count=i
            break
    
    del(tmp[0:count])
    print(tmp)
    return devid(tmp,g,quotient)
    

quotient=[]
r = devid([3,0,2,6,7],[1,0,1],quotient)
print(f"{r[0]} {r[1]}")