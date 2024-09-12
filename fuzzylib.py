def fuzzify(xs, function):
    ys=[]
    for x in xs:
       ys.append(function(x))
    return ys; 