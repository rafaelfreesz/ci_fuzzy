import numpy as np
import fuzzylib as fl
import utils as ut
import plotly.graph_objects as go
import copy

#Defuzzificação
def defuzzify(groups,trigged_rules, method):

    trigged_groups=None

    if(method == 'mamdani'):
        trigged_groups = calculate_mamdani(trigged_rules,groups)

    graph_y = build_graph_y(groups,trigged_groups)
    
    return graph_y

def build_graph_y(groups,trigged_groups):
    graph = go.Figure()
    x_mc = np.linspace(0,int(groups[6].b),int(groups[6].b)+1)
    x_c = np.linspace(int(groups[7].a),int(groups[7].b),int(groups[7].b)+1)
    x_m = np.linspace(int(groups[8].a),int(groups[8].b),int(groups[8].b)+1)
    x_l = np.linspace(int(groups[9].a),int(groups[9].b),int(groups[8].b)+1)
    x_ml = np.linspace(int(groups[10].a),int(groups[10].m),int(groups[10].m-groups[10].a)+1)

    graph.add_trace(go.Scatter(x=x_mc, y=ut.array_apply(x_mc,groups[6].f), mode='lines', name=f"{groups[6].f_name}_{groups[6].f_spec}"))
    graph.add_trace(go.Scatter(x=x_c, y=ut.array_apply(x_c,groups[7].f), mode='lines', name=f"{groups[7].f_name}_{groups[7].f_spec}"))
    graph.add_trace(go.Scatter(x=x_m, y=ut.array_apply(x_m,groups[8].f), mode='lines', name=f"{groups[8].f_name}_{groups[8].f_spec}"))
    graph.add_trace(go.Scatter(x=x_l, y=ut.array_apply(x_l,groups[9].f), mode='lines', name=f"{groups[9].f_name}_{groups[9].f_spec}"))
    graph.add_trace(go.Scatter(x=x_ml, y=ut.array_apply(x_ml,groups[10].f), mode='lines', name=f"{groups[10].f_name}_{groups[10].f_spec}"))

    print(trigged_groups[0])
    tg=None
    for i in range(len(trigged_groups)):
        if trigged_groups[i].f_spec == "mc":
            tg = trigged_groups[i]
            break
    
    if tg is not None:
        if tg.f_type != "tri_desc":
            xs=np.linspace(0,tg.d,10*int(tg.d)+1)
        else:
            xs = x_mc
        graph.add_trace(go.Scatter(x=xs, y=ut.array_apply(xs,tg.f), mode='lines', name=f"y({tg.f_name}_{tg.f_spec})", stackgroup=1))
        
    tg=None
    for i in range(len(trigged_groups)):
        if trigged_groups[i].f_spec == "c":
            tg = trigged_groups[i]
            break
    
    if tg is not None:
        if tg.f_type != "tri_full":
            xs=np.linspace(int(tg.a),int(tg.d),10*int(tg.d-tg.a)+1)
        else:
            xs = x_c
        graph.add_trace(go.Scatter(x=xs, y=ut.array_apply(xs,tg.f), mode='lines', name=f"y({tg.f_name}_{tg.f_spec})", stackgroup=2))

    tg=None
    for i in range(len(trigged_groups)):
        if trigged_groups[i].f_spec == "m":
            tg = trigged_groups[i]
            break
    
    if tg is not None:
        if tg.f_type != "tri_full":
            xs=np.linspace(int(tg.a),int(tg.d),10*int(tg.d-tg.a)+1)
        else:
            xs = x_m
        graph.add_trace(go.Scatter(x=xs, y=ut.array_apply(xs,tg.f), mode='lines', name=f"y({tg.f_name}_{tg.f_spec})", stackgroup=3))
    tg=None
    for i in range(len(trigged_groups)):
        if trigged_groups[i].f_spec == "l":
            tg = trigged_groups[i]
            break
    
    if tg is not None:
        if tg.f_type != "tri_full":
            xs=np.linspace(int(tg.a),int(tg.d),10*int(tg.d-tg.a)+1)
        else:
            xs = x_l
        graph.add_trace(go.Scatter(x=xs, y=ut.array_apply(xs,tg.f), mode='lines', name=f"y({tg.f_name}_{tg.f_spec})", stackgroup=4))
    tg=None
    for i in range(len(trigged_groups)):
        if trigged_groups[i].f_spec == "ml":
            tg = trigged_groups[i]
            break
    
    if tg is not None:
        if tg.f_type != "tri_asc":
            print(tg)
            xs=np.linspace(int(tg.a),int(tg.b),10*int(tg.b-tg.a)+1)
        else:
            xs = x_ml
        graph.add_trace(go.Scatter(x=xs, y=ut.array_apply(xs,tg.f), mode='lines', name=f"y({tg.f_name}_{tg.f_spec})", stackgroup=5))
        

    # for i in range(len(trigged_groups)):
    #     xs=None
    #     if(trigged_groups[i].f_spec == "mc"):
    #         if trigged_groups[i].f_type != "tri_full":
    #             xs=np.linspace(0,trigged_groups[i].d,int(trigged_groups[i].d)+1)
    #         else:
    #             xs = x_mc
    #     elif(trigged_groups[i].f_spec == "c"):
    #         if trigged_groups[i].f_type != "tri_full":
    #             xs=np.linspace(int(trigged_groups[i].a),int(trigged_groups[i].d),int(trigged_groups[i].d-trigged_groups[i].a)+1)
    #         else:
    #             xs = x_c
    #     elif(trigged_groups[i].f_spec == "m"):
    #         if trigged_groups[i].f_type != "tri_full":
    #             xs=np.linspace(int(trigged_groups[i].a),int(trigged_groups[i].d),int(trigged_groups[i].d-trigged_groups[i].a)+1)
    #         else:
    #             xs = x_m
    #     elif(trigged_groups[i].f_spec == "l"):
    #         print(trigged_groups[i])
    #         if trigged_groups[i].f_type != "tri_full":
    #             xs=np.linspace(int(trigged_groups[i].a),int(trigged_groups[i].d),int(trigged_groups[i].d-trigged_groups[i].a)+1)
    #         else:
    #             xs = x_l
    #     elif(trigged_groups[i].f_spec == "ml"):
    #         if trigged_groups[i].f_type != "tri_full":
    #             xs=xs=np.linspace(int(trigged_groups[i].a),60,61-int(trigged_groups[i].a))
    #         else:
    #             xs = x_ml
    #     else:
    #         print("SUMB")
        
    #     if xs is not None:
    #         print(trigged_groups[i])
    #         graph.add_trace(go.Scatter(x=xs, y=ut.array_apply(xs,trigged_groups[i].f), mode='lines', name=f"y({trigged_groups[i].f_name}_{trigged_groups[i].f_spec})", stackgroup='one'))
    
    graph.update_layout(width=480, height = 180, margin = dict(t=20,b=0), title = "Saída")
    return graph

def calculate_mamdani(trigged_rules,groups):
    trigged_groups = []
    group_rule_tuples = []
    for i in range(len(trigged_rules)):
        j=-1
        group = groups[j]

        while group.f_spec != trigged_rules[i].vars[-1]:
            j=j-1
            group = groups[j]

        trigged_group = copy.deepcopy(group)
        group_rule_tuples.append((trigged_group,trigged_rules[i]))
        
        trigged_groups.append(trigged_group)

    #Modificando a área do grafico em função das regras disparadas
    for i in range(len(group_rule_tuples)):
        if group_rule_tuples[i][1].values[-1] < 1:
            if group_rule_tuples[i][0].f_type == "tri_asc":
               fl.ff.reverse_tri_asc(group_rule_tuples[i][0],group_rule_tuples[i][1])
            elif group_rule_tuples[i][0].f_type == "tri_desc":
               fl.ff.reverse_tri_desc(group_rule_tuples[i][0],group_rule_tuples[i][1])  
            elif group_rule_tuples[i][0].f_type == "tri_full":
               fl.ff.reverse_tri_full(group_rule_tuples[i][0],group_rule_tuples[i][1])  
            elif group_rule_tuples[i][0].f_type == "trap_desc":
               fl.ff.reverse_trap_desc(group_rule_tuples[i][0],group_rule_tuples[i][1])  
            elif group_rule_tuples[i][0].f_type == "trap_asc":
               fl.ff.reverse_trap_asc(group_rule_tuples[i][0],group_rule_tuples[i][1])  
            elif group_rule_tuples[i][0].f_type == "trap_full":
               fl.ff.reverse_trap_full(group_rule_tuples[i][0],group_rule_tuples[i][1])
            else:
                print("DUMB")
            
    return trigged_groups

#Calcula e retorna os resultados da inferência
def infer(groups,sujeira,mancha):
    rules = fl.prepare_infer_assoc_mem("01_wash/wash_rules.csv")

    val_sujeira = [groups[0].f(sujeira),groups[1].f(sujeira),groups[2].f(sujeira)]
    val_mancha = [groups[3].f(mancha),groups[4].f(mancha),groups[5].f(mancha)]

    rules[0].values[0] = val_sujeira[0]
    rules[0].values[1] = val_mancha[0]
    rules[0].values[2] = min(rules[0].values[0], rules[0].values[1])
    
    rules[1].values[0] = val_sujeira[0]
    rules[1].values[1] = val_mancha[1]
    rules[1].values[2] = min(rules[1].values[0], rules[1].values[1])

    rules[2].values[0] = val_sujeira[0]
    rules[2].values[1] = val_mancha[2]
    rules[2].values[2] = min(rules[2].values[0], rules[2].values[1])

    rules[3].values[0] = val_sujeira[1]
    rules[3].values[1] = val_mancha[0]
    rules[3].values[2] = min(rules[3].values[0], rules[3].values[1])

    rules[4].values[0] = val_sujeira[1]
    rules[4].values[1] = val_mancha[1]
    rules[4].values[2] = min(rules[4].values[0], rules[4].values[1])

    rules[5].values[0] = val_sujeira[1]
    rules[5].values[1] = val_mancha[2]
    rules[5].values[2] = min(rules[5].values[0], rules[5].values[1])

    rules[6].values[0] = val_sujeira[2]
    rules[6].values[1] = val_mancha[0]
    rules[6].values[2] = min(rules[6].values[0], rules[6].values[1])

    rules[7].values[0] = val_sujeira[2]
    rules[7].values[1] = val_mancha[1]
    rules[7].values[2] = min(rules[7].values[0], rules[7].values[1])

    rules[8].values[0] = val_sujeira[2]
    rules[8].values[1] = val_mancha[2]
    rules[8].values[2] = min(rules[8].values[0], rules[8].values[1])

    str_rules = f""

    for i in range(len(rules)):
        if rules[i].values[2] == 0:
            str_rules = str_rules + f"-  :gray[~~{rules[i]}~~]  \n"
        else:
            str_rules = str_rules + f"- {rules[i]}  \n"

    trigged_rules = get_rules_max_min(rules)
    str_trigged_rules = ""
    for i in range(len(trigged_rules)):
        str_trigged_rules = str_trigged_rules + f"- {trigged_rules[i]}  \n"


    return rules, str_rules, trigged_rules, str_trigged_rules

#Cria um subgrupo de regras disparadas de acordo com o critério Max-Min
def get_rules_max_min(rules):
    rules_sel=[None,None,None,None,None]
    for i in range(len(rules)):
        rule = rules[i]
        index = -1
        if rule.vars[-1] == "mc":
            index = 0
        elif rule.vars[-1] == "c":
            index = 1
        elif rule.vars[-1] == "m":
            index = 2
        elif rule.vars[-1] == "l":
            index = 3
        elif rule.vars[-1] == "ml":
            index = 4
        else:
            print("DUMB"+str(rule.vars[-1]))
        
        if rules_sel[index] is None or rules_sel[index].values[-1] < rule.values[-1]:
            rules_sel[index] = rules[i]

    rules_max_min=[]

    for i in range(len(rules_sel)):
        if rules_sel[i] is not None and rules_sel[i].values[-1] > 0.0:
            rules_max_min.append(rules_sel[i])
    
    return rules_max_min

#Calcula e retorna os valores e gráficos para a Fuzzificação
def fuzzify(sujeira, mancha):
    groups = fl.prepare_fuzz("01_wash/wash_x.csv")

    graphs=[]
    strs=[]

    #Grafico e resultados para Quantidade de Sujeira
    graph_sujeira = build_graph_sujeira(sujeira,groups)
    str_resultado_sujeira = get_sujeira_result_string(groups,sujeira)
    graphs.append(graph_sujeira)
    strs.append(str_resultado_sujeira)

    #Grafico e resultados para Quantidade de Mancha
    graph_mancha = build_graph_mancha(mancha,groups)
    str_resultado_mancha = get_mancha_result_string(groups,mancha)
    graphs.append(graph_mancha)
    strs.append(str_resultado_mancha)

    return (graphs,strs,groups)

#Constroi e seta atributos do grafico de sujeira
def build_graph_sujeira(sujeira,groups):
    graph = go.Figure()
    x_ps = np.linspace(0,int(groups[0].b),int(groups[0].b)+1)
    x_ms = np.linspace(int(groups[1].a),int(groups[1].b),int(groups[1].b)+1)
    x_gs = np.linspace(int(groups[2].a),int(groups[2].m),int(groups[2].m-groups[2].a)+1)

    graph.add_trace(go.Scatter(x=x_ps, y=ut.array_apply(x_ps,groups[0].f), mode='lines', name=f"{groups[0].f_name}_{groups[0].f_spec}"))
    graph.add_trace(go.Scatter(x=x_ms, y=ut.array_apply(x_ms,groups[1].f), mode='lines', name=f"{groups[1].f_name}_{groups[1].f_spec}"))
    graph.add_trace(go.Scatter(x=x_gs, y=ut.array_apply(x_gs,groups[2].f), mode='lines', name=f"{groups[2].f_name}_{groups[2].f_spec}"))
    graph.add_vline(x=sujeira, line_width=3, line_dash="dash",line_color="green")

    graph.update_layout(width=480, height = 180, margin = dict(t=20,b=0), title = "Quantidade de Sujeira")
    return graph

#Retorna string para imprimir resultado da fuzzificação da quantidade de sujeira
def get_sujeira_result_string(groups,sujeira):
    return f"Sujeira: x = {sujeira}  \n Pouca Sujeira: {groups[0].f(sujeira)}  \n Média Sujeira: {groups[1].f(sujeira)}  \n Grande Sujeira: {groups[2].f(sujeira)}"

#Constroi e seta atributos do grafico de mancha
def build_graph_mancha(mancha,groups):
    graph = go.Figure()
    x_sm = np.linspace(0,int(groups[3].b),int(groups[3].b)+1)
    x_mm = np.linspace(int(groups[4].a),int(groups[4].b),int(groups[1].b)+1)
    x_gm = np.linspace(int(groups[5].a),int(groups[5].m),int(groups[2].m-groups[2].a)+1)

    graph.add_trace(go.Scatter(x=x_sm, y=ut.array_apply(x_sm,groups[3].f), mode='lines', name=f"{groups[3].f_name}_{groups[3].f_spec}"))
    graph.add_trace(go.Scatter(x=x_mm, y=ut.array_apply(x_mm,groups[4].f), mode='lines', name=f"{groups[4].f_name}_{groups[4].f_spec}"))
    graph.add_trace(go.Scatter(x=x_gm, y=ut.array_apply(x_gm,groups[5].f), mode='lines', name=f"{groups[5].f_name}_{groups[6].f_spec}"))
    graph.add_vline(x=mancha, line_width=3, line_dash="dash",line_color="green")

    graph.update_layout(width=480, height = 180, margin = dict(t=20,b=0), title = "Quantidade de Mancha")
    return graph

#Retorna string para imprimir resultado da fuzzificação da quantidade de sujeira
def get_mancha_result_string(groups,mancha):
    return f"Mancha: x = {mancha}  \n Sem mancha: {groups[0].f(mancha)}  \n Média Mancha: {groups[1].f(mancha)}  \n Grande Mancha: {groups[2].f(mancha)}"