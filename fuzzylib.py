import pandas as pd
def fuzzify(xs, function):
    ys=[]
    for x in xs:
       ys.append(function(x))
    return ys

def prepare_run(filename):
    file = pd.read_csv(filename)
    print(file)
    # file.set_index('f_name') talvez nao precise
    # build_functions()

# def build_functions():
    