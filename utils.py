#Aplica uma função genérica a um vetor de atributos genéricos
def array_apply(xs,fun):
    res = []
    for x in range(len(xs)):
        res.append(fun(xs[x]))
    return res