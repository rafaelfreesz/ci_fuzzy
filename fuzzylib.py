import pandas as pd
import fuzzyfunctions as ff
import fuzzygroup as fg

def prepare_infer_assoc_mem(filename):
    file = pd.read_csv(filename)
    matriz = [file.columns.tolist()]+file.values.tolist()

    rules = []
    index = 1
    for i in range(len(matriz)-1):
        for j in range(1,len(matriz[i])):
            # print(j)
            rule = fg.Rule()
            rule.index=index
            rule.vars.append(matriz[i][0])
            rule.vars.append(matriz[len(matriz)-1][j])
            rule.vars.append(matriz[i][j])
            rule.values.append(0)
            rule.values.append(0)
            rule.values.append(0)
            rules.append(rule)
            index = index+1


    return rules

def prepare_fuzz(filename):
    file = pd.read_csv(filename)

    groups = build_groups(file)

    return groups

def build_groups(file):
    fuzzy_groups=[]
    for a in range(len(file)):
        obj=fg.Group()
        obj.v_type = file.iloc[a]['v_type']
        obj.f_type = file.iloc[a]['f_type']
        obj.f_name = file.iloc[a]['f_name']
        obj.f_spec = file.iloc[a]['f_spec']
        obj.a = file.iloc[a]['a']
        obj.b = file.iloc[a]['b']
        obj.c = file.iloc[a]['c']
        obj.d = file.iloc[a]['d']
        obj.m = file.iloc[a]['m']
        obj.define_f()
        fuzzy_groups.append(obj)
     
    return fuzzy_groups