import pandas as pd
import fuzzyfunctions as ff
import fuzzyentities as fe

def define_color(tg,groups,i_groups, is_area):
    color_area=["rgba(255,54,54,0.5)","rgba(61,54,255,0.5)","rgba(255,110,251,0.5)","rgba(255,241,110,0.5)","rgba(96,236,75,0.5)","rgba(75,231,236,0.5)","rgba(218,160,0,0.5)"]
    color_line=["rgb(255,54,54)","rgb(61,54,255)","rgb(255,110,251)","rgb(255,241,110)","rgb(96,236,75)","rgb(75,231,236)","rgb(218,160,0)"]

    i=0
    print(len(groups))

    while tg.f_spec != groups[i_groups].f_spec:
        print(tg.f_spec,groups[i_groups].f_spec)
        i = i+1
        i_groups = i_groups + 1

    if is_area:
        return color_area[i]
    else:
        return color_line[i]
        
    
#Calcula o ponto medio de uma area
def calculate_midle_point(group):
    if group.f_type == "trap_full":
        return group.a + (group.d - group.a)/2
    elif group.f_type == "trap_asc":
        return group.a + (group.b - group.a)/2
    elif group.f_type == "trap_desc":
        return group.c + (group.d - group.c)/2
    elif group.f_type == "tri_full":
        return group.a + (group.b - group.a)/2
    elif group.f_type == "tri_asc":
        return group.a + (group.m - group.a)/2
    elif group.f_type == "tri_full":
        return group.m + (group.b - group.m)/2
    
#Calcula a média ponderada do ponto médio de cada forma
def defuzz_weighted_average(triggered_groups,triggered_rules):
    sum = 0
    denominator = 0
    
    for i in range(len(triggered_groups)):
        group = triggered_groups[i]
        rule = None
        for j in range(len(triggered_rules)):
            if triggered_rules[j].vars[-1] == group.f_spec:
                rule = triggered_rules[j]
                break
        middle = calculate_midle_point(group)
        sum = sum + middle * rule.values[-1]
        denominator = denominator + rule.values[-1]
    return sum/denominator

def prepare_infer_assoc_mem(filename):
    file = pd.read_csv(filename)
    matriz = [file.columns.tolist()]+file.values.tolist()

    rules = []
    index = 1
    for i in range(1,len(matriz)-1):
        for j in range(1,len(matriz[i])):
            # print(j)
            rule = fe.Rule()
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
        obj=fe.Group()
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