def divid_in_polynomial(f:list,g:list):
    if(len(f)<len(g)):
        return []
    
    quotient = []
    remainder = []
    
    tmp = []

    quotient.append(f[0]/g[0])
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

    for i in range(0,len(f)):
        tmp1 = tmp
        tmp=[]
        if (f[i]==0):
            quotient.append(0)
            continue
        product = f[i]/g[0]
        quotient.append(product)
        for j in range(0,len(tmp1)):
            tmp.append(tmp1[j]-(g[j]*product))
        for j in range(len(tmp1),len(f)):
            tmp.append(f[i])
        print(tmp)