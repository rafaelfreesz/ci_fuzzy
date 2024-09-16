import numpy as np
import fuzzylib as fl
import utils as ut
import plotly.graph_objects as go
import copy

def fuzzify(velocidade, distancia):
    groups = fl.prepare_fuzz("03_overtaking/overtaking_x.csv")

    graphs=[]
    strs=[]

    #Grafico e resultados para a velocidade
    graph_velocidade = build_graph_velocidade(velocidade,groups)
    str_resultado_velocidade = get_velocidade_result_string(groups,velocidade)
    graphs.append(graph_velocidade)
    strs.append(str_resultado_velocidade)

    #Grafico e resultados para a distancia
    graph_distancia = build_graph_distancia(distancia,groups)
    str_resultado_distancia = get_distancia_result_string(groups,distancia)
    graphs.append(graph_distancia)
    strs.append(str_resultado_distancia)

    return (graphs,strs,groups)

def build_graph_velocidade(velocidade,groups):
    
    graph = go.Figure()
    x_b = np.linspace(30.0,65.0,int((65.0-30.0)*100.0))
    x_m = np.linspace(38.0,113.0,int((113.0-38.0)*100.0))
    x_a = np.linspace(65.0,120.0,int((120.0-65.0)*100.0))
    
    graph.add_trace(go.Scatter(x=x_b, y=ut.array_apply(x_b,groups[0].f), mode='lines', name=f"{groups[0].f_name}_{groups[0].f_spec}"))
    graph.add_trace(go.Scatter(x=x_m, y=ut.array_apply(x_m,groups[1].f), mode='lines', name=f"{groups[1].f_name}_{groups[1].f_spec}"))
    graph.add_trace(go.Scatter(x=x_a, y=ut.array_apply(x_a,groups[2].f), mode='lines', name=f"{groups[2].f_name}_{groups[2].f_spec}"))
    graph.add_vline(x=velocidade, line_width=3, line_dash="dash",line_color="green")

    graph.update_layout(width=840, height = 180, margin = dict(t=20,b=0), title = "Velocidade")
    return graph

#Retorna string para imprimir resultado da fuzzificação da Velocidade
def get_velocidade_result_string(groups,velocidade):
    return f"Velocidade: x = {velocidade}km/h  \n Baixa (b): {'{0:.3f}'.format(groups[0].f(velocidade))}  \n Média (m): {'{0:.3f}'.format(groups[1].f(velocidade))}  \n Alta(a): {'{0:.3f}'.format(groups[2].f(velocidade))}"

def build_graph_distancia(distancia,groups):
    
    graph = go.Figure()
    x_c = np.linspace(180.0,438.0,int((438.0-180.0)*100.0))
    x_m = np.linspace(263.0,800.0,int((800.0-263.0)*100.0))
    x_l = np.linspace(438.0,800.0,int((800.0-438.0)*100.0))
    
    graph.add_trace(go.Scatter(x=x_c, y=ut.array_apply(x_c,groups[3].f), mode='lines', name=f"{groups[3].f_name}_{groups[3].f_spec}"))
    graph.add_trace(go.Scatter(x=x_m, y=ut.array_apply(x_m,groups[4].f), mode='lines', name=f"{groups[4].f_name}_{groups[4].f_spec}"))
    graph.add_trace(go.Scatter(x=x_l, y=ut.array_apply(x_l,groups[5].f), mode='lines', name=f"{groups[5].f_name}_{groups[5].f_spec}"))
    graph.add_vline(x=distancia, line_width=3, line_dash="dash",line_color="green")

    graph.update_layout(width=840, height = 180, margin = dict(t=20,b=0), title = "Distancia")
    return graph

#Retorna string para imprimir resultado da fuzzificação da distancia
def get_distancia_result_string(groups,distancia):
    return f"distancia: x = {distancia}m  \n curta (b): {'{0:.3f}'.format(groups[0].f(distancia))}  \n Média (m): {'{0:.3f}'.format(groups[1].f(distancia))}  \n Longa(l): {'{0:.3f}'.format(groups[2].f(distancia))}"

#Calcula e retorna os resultados da inferência
def infer(groups,velocidade,distancia):
    rules = fl.prepare_infer_assoc_mem("03_overtaking/overtaking_rules.csv")
    
    val_velocidade = [groups[0].f(velocidade),groups[1].f(velocidade),groups[2].f(velocidade)]
    val_fator = [groups[3].f(distancia),groups[4].f(distancia),groups[5].f(distancia)]
    
    #R1 - Se g e mp entao mp
    rules[0].values[0] = val_velocidade[0]
    rules[0].values[1] = val_fator[0]
    rules[0].values[2] = min(rules[0].values[0], rules[0].values[1])
    
    #R2 - Se g e p entao p
    rules[1].values[0] = val_velocidade[0]
    rules[1].values[1] = val_fator[1]
    rules[1].values[2] = min(rules[1].values[0], rules[1].values[1])

    #R3 - Se g e m entao mp
    rules[2].values[0] = val_velocidade[0]
    rules[2].values[1] = val_fator[2]
    rules[2].values[2] = min(rules[2].values[0], rules[2].values[1])

    #R4 - Se m e mp entao pg
    rules[3].values[0] = val_velocidade[1]
    rules[3].values[1] = val_fator[0]
    rules[3].values[2] = min(rules[3].values[0], rules[3].values[1])

    #R5 - Se m e p entao pp
    rules[4].values[0] = val_velocidade[1]
    rules[4].values[1] = val_fator[1]
    rules[4].values[2] = min(rules[4].values[0], rules[4].values[1])

    #R6 - Se m e m entao p
    rules[5].values[0] = val_velocidade[1]
    rules[5].values[1] = val_fator[2]
    rules[5].values[2] = min(rules[5].values[0], rules[5].values[1])

    rules[6].values[0] = val_velocidade[2]
    rules[6].values[1] = val_fator[0]
    rules[6].values[2] = min(rules[6].values[0], rules[6].values[1])

    #R8 - Se p e p entao g
    rules[7].values[0] = val_velocidade[2]
    rules[7].values[1] = val_fator[1]
    rules[7].values[2] = min(rules[7].values[0], rules[7].values[1])

    #R9 - Se p e m entao m
    rules[8].values[0] = val_velocidade[2]
    rules[8].values[1] = val_fator[2]
    rules[8].values[2] = min(rules[8].values[0], rules[8].values[1])

    str_rules = f""

    for i in range(len(rules)):
        if rules[i].values[2] == 0:
            str_rules = str_rules + f"-  :gray[~~{rules[i]}~~]  \n"
        else:
            str_rules = str_rules + f"- {rules[i]}  \n"

    triggered_rules = get_rules_max_min(rules)
    str_triggered_rules = ""
    for i in range(len(triggered_rules)):
        str_triggered_rules = str_triggered_rules + f"- {triggered_rules[i]}  \n"


    return rules, str_rules, triggered_rules, str_triggered_rules

#Cria um subgrupo de regras disparadas de acordo com o critério Max-Min
def get_rules_max_min(rules):
    rules_sel=[None,None,None,None,None,None,None]

    for i in range(len(rules)):
        rule = rules[i]
        index = -1
        if rule.vars[-1] == "rm":
            index = 0
        elif rule.vars[-1] == "s":
            index = 1
        elif rule.vars[-1] == "a":
            index = 2
        elif rule.vars[-1] == "p":
            index = 3
        else:
            print("DUMB "+str(rule.vars))
        
        if rules_sel[index] is None or rules_sel[index].values[-1] < rule.values[-1]:
            rules_sel[index] = rules[i]

    rules_max_min=[]

    for i in range(len(rules_sel)):
        if rules_sel[i] is not None and rules_sel[i].values[-1] > 0.0:
            rules_max_min.append(rules_sel[i])
    
    return rules_max_min

#Defuzzificação
def defuzzify(groups,triggered_rules, method):

    triggered_groups = calculate_mamdani(triggered_rules,groups)

    graph_y = build_graph_y(groups,triggered_groups)
    
    
    weighted_average = 0

    res_str = ""
    if method == 'Média Ponderada':
        weighted_average = fl.defuzz_weighted_average(triggered_groups,triggered_rules)
        res_str = f"O resultado com média ponderada é {'{0:.2f}'.format(weighted_average)}"
    elif method == 'Centro de Gravidade - CoG':
        #TODO implementar centro de gravidade
        weighted_average = fl.defuzz_weighted_average(triggered_groups,triggered_rules)
        res_str = f"O resultado com Centro de Gravidade - CoG é {'{0:.2f}'.format(weighted_average)}"
    else:
        res_str = "DUMB"
    return graph_y, res_str

def build_graph_y(groups,triggered_groups):

    #Graficos variável de saída
    graph = go.Figure()
    print("UUUUUUUUUUUU")
    for g in groups:
        print(g)
    
    x_rm = np.linspace(0.0,groups[6].b,(int(groups[6].b)+1)*1000)
    graph.add_trace(go.Scatter(x=x_rm, y=ut.array_apply(x_rm,groups[6].f), mode='lines', name=f"{groups[6].f_name}_{groups[6].f_spec}"))
        
    x_s = np.linspace(groups[7].a,groups[7].b,(int(groups[7].b)+1)*1000)
    graph.add_trace(go.Scatter(x=x_s, y=ut.array_apply(x_s,groups[7].f), mode='lines', name=f"{groups[7].f_name}_{groups[7].f_spec}"))
    
    x_a = np.linspace(groups[8].a,groups[8].b,(int(groups[8].b)+1)*1000)
    graph.add_trace(go.Scatter(x=x_a, y=ut.array_apply(x_a,groups[8].f), mode='lines', name=f"{groups[8].f_name}_{groups[8].f_spec}"))
    
    x_p = np.linspace(groups[9].a,groups[9].m,(int(groups[9].m)+1)*1000)
    graph.add_trace(go.Scatter(x=x_p, y=ut.array_apply(x_p,groups[9].f), mode='lines', name=f"{groups[9].f_name}_{groups[9].f_spec}"))
    
    print("AAAAAAAAAAAAAAAAA")
    for r in triggered_groups:
        print(r)

    #Gráficos de área para resultado
    for i in range(len(triggered_groups)):
        tg = triggered_groups[i]
        plot = True
    
        if triggered_groups[i].f_spec == "rm":
            if tg.f_type != "tri_desc":
                xs=np.linspace(0,tg.d,100*int(tg.d+1))
            else:
                xs = x_p
        elif triggered_groups[i].f_spec == "s":
            if tg.f_type != "tri_full":
                xs=np.linspace(tg.a,tg.d,100*int(tg.d-tg.a+1))
            else:
                xs = x_p
        elif triggered_groups[i].f_spec == "a":
            if tg.f_type != "tri_full":
                xs=np.linspace(tg.a,tg.d,100*int(tg.d-tg.a+1))
            else:
                xs = x_a
        elif triggered_groups[i].f_spec == "p":
            if tg.f_type != "tri_asc":
                xs=np.linspace(tg.a,100,100*int(100-tg.a+1))
            else:
                xs = x_p
        else:
            plot = False
            print("DUMB")
        
        graph.add_trace(go.Scatter(x=xs, y=ut.array_apply(xs,tg.f), mode='lines', name=f"y({tg.f_name}_{tg.f_spec})", stackgroup=i))
        
    
    graph.update_layout(width=840, height = 180, margin = dict(t=20,b=0), title = "Saída")
    return graph


#Calcula e retorna as regioes conforme o metodo de Mamdani
def calculate_mamdani(triggered_rules,groups):
    triggered_groups = []
    group_rule_tuples = []
    for i in range(len(triggered_rules)):
        j=-1
        group = groups[j]

        while group.f_spec != triggered_rules[i].vars[-1]:
            j=j-1
            group = groups[j]

        triggered_group = copy.deepcopy(group)
        group_rule_tuples.append((triggered_group,triggered_rules[i]))
        
        triggered_groups.append(triggered_group)

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
            
    return triggered_groups
