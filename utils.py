def array_apply(xs,fun):
    res = []
    for x in range(len(xs)):
        res.append(fun(xs[x]))
    return res

def group_by(lst, param):
    big=[]
    small=[]
    
    for i in range(len(lst)):
        if len(small)==0:
            small.append(lst[i])
        else:
            if getattr(small[-1],param) != getattr(lst[i],param) or i == (len(lst)-1):
                big.append(small)
                small=[lst[i]]
            else:
                small.append(lst[i])
                
    return big