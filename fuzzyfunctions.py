#Trapeze Functions
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
    
def trap_full(a,b,c,d,x):
    if x <= a or x >= d:
        return 0
    elif x > a and x < b:
        return (x-a)/(b-a)
    elif x > c and x < d:
        return (d-x)/(d-c)
    else:
        return 1

#Triangle Functions
def tri_desc(m,b,x):
    if x < m or x > b:
        return 0
    else:
        return (b-x)/(b-m)
    
def tri_asc(a,m,x):
    if x < a or x > m:
        return 0
    else:
        return (x-a)/(m-a)
    
def tri_full(a,b,m,x):
    if x >= a and x <= m:
        return (x-a)/(m-a)
    elif x > m and x < b:
        return (b-x)/(b-m)
    else:
        return 0
