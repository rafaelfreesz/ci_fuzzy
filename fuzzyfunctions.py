def trap_desc(c,d,x):
    if x <= c:
        return 1
    elif x >= d:
        return 0
    else:
        return (d-x)/(d-c)
def trap_asc(a,b,x):
    if x <= a:
        return 0
    elif x >= b:
        return 1
    else:
        return (x-a)/(b-a)
def trap_desc(a,b,c,d,x):
    if x <= a or x >= d:
        return 0
    elif x > a and x < b:
        return (x-a)/(b-a)
    elif x > c and x < d:
        return (d-x)/(d-c)
    else:
        return 1
