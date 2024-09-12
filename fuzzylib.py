import pandas as pd
import fuzzyfunctions as ff
import fuzzygroup as fg

def fuzzify(xs, function):
    ys=[]
    for x in xs:
       ys.append(function(x))
    return ys

def prepare_run(filename):
    file = pd.read_csv(filename)
    build_functions(file)

def build_functions(file):
    fuzzy_groups=[]
    for a in range(len(file)):
        obj=fg.Fuzzy()
        obj.f_type = file.iloc[a]['f_type']
        obj.f_name = file.iloc[a]['f_name']
        obj.f_spec = file.iloc[a]['f_spec']
        obj.a = file.iloc[a]['a']
        obj.b = file.iloc[a]['b']
        obj.c = file.iloc[a]['c']
        obj.d = file.iloc[a]['d']
        obj.m = file.iloc[a]['m']
        obj.define_function()
        fuzzy_groups.append(obj)
     
    print(len(fuzzy_groups))
    for a in range(len(file)):
        print(fuzzy_groups[a])

    # print(type(file))


    