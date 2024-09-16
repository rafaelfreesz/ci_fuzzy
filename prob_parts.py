import numpy as np
import fuzzylib as fl
import utils as ut
import plotly.graph_objects as go
import copy

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
    
    
    x_mp = np.linspace(0.0,groups[9].d,(int(groups[9].d)+1)*1000)
    graph.add_trace(go.Scatter(x=x_mp, y=ut.array_apply(x_mp,groups[9].f), mode='lines', name="Muito Pequeno", line=dict(color="rgb(255,54,54)")))
        
    x_p = np.linspace(groups[10].a,groups[10].b,(int(groups[10].b)+1)*1000)
    graph.add_trace(go.Scatter(x=x_p, y=ut.array_apply(x_p,groups[10].f), mode='lines', name="Pequeno", line=dict(color="rgb(61,54,255)")))
    
    x_pp = np.linspace(groups[11].a,groups[11].b,(int(groups[11].b)+1)*1000)
    graph.add_trace(go.Scatter(x=x_pp, y=ut.array_apply(x_pp,groups[11].f), mode='lines', name="Pouco Pequeno", line=dict(color="rgb(255,110,251)")))
    
    x_m = np.linspace(groups[12].a,groups[12].b,(int(groups[12].b)+1)*1000)
    graph.add_trace(go.Scatter(x=x_m, y=ut.array_apply(x_m,groups[12].f), mode='lines', name="Médio", line=dict(color="rgb(255,241,110)")))
    
    x_pg = np.linspace(groups[13].a,groups[13].b,(int(groups[13].b)+1)*1000)
    graph.add_trace(go.Scatter(x=x_pg, y=ut.array_apply(x_pg,groups[13].f), mode='lines', name="Grande", line=dict(color="rgb(96,236,75)")))
    
    x_g = np.linspace(groups[14].a,groups[14].b,(int(groups[14].b-groups[14].a)+1)*1000)
    graph.add_trace(go.Scatter(x=x_g, y=ut.array_apply(x_g,groups[14].f), mode='lines', name="Pouco Grande", line=dict(color="rgb(75,231,236)")))
    
    x_mg = np.linspace(groups[15].a,1,1000)
    graph.add_trace(go.Scatter(x=x_mg, y=ut.array_apply(x_mg,groups[15].f), mode='lines', name="Muito Grande", line=dict(color="rgb(218,160,0)")))


    #Gráficos de área para resultado
    for i in range(len(triggered_groups)):
        tg = triggered_groups[i]
        plot = True

        if triggered_groups[i].f_spec == "mp":
            xs = x_mp
        elif triggered_groups[i].f_spec == "p":
            if tg.f_type != "tri_full":
                xs=np.linspace(tg.a,tg.d,1000*int(tg.d-tg.a+1))
            else:
                xs = x_p
        elif triggered_groups[i].f_spec == "pp":
            if tg.f_type != "tri_full":
                xs=np.linspace(tg.a,tg.d,1000*int(tg.d-tg.a+1))
            else:
                xs = x_pp
        elif triggered_groups[i].f_spec == "m":
            if tg.f_type != "tri_full":
                xs=np.linspace(tg.a,tg.d,1000*int(tg.d-tg.a+1))
            else:
                xs = x_m
        elif triggered_groups[i].f_spec == "pg":
            if tg.f_type != "tri_full":
                xs=np.linspace(tg.a,tg.d,1000*int(tg.d-tg.a+1))
            else:
                xs = x_pg
        elif triggered_groups[i].f_spec == "g":
            if tg.f_type != "tri_full":
                xs=np.linspace(tg.a,tg.d,1000*int(tg.d-tg.a+1))
            else:
                xs = x_g
        elif triggered_groups[i].f_spec == "mg":
            xs = x_mg
        else:
            plot = False
            print("DUMB")
        
        graph.add_trace(go.Scatter(x=xs, y=ut.array_apply(xs,tg.f), mode='lines',showlegend=False, stackgroup=i, fillcolor=fl.define_color(tg,groups,9,True), line=dict(color=fl.define_color(tg,groups,9,False))))
        
    
    graph.update_layout(width=840, height = 280, xaxis_title="Número de Peças Extras", yaxis_title="Pertinência", margin = dict(t=20,b=0), title = "Saída (n)")
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


def fuzzify(tempo, fator, funcionarios):
    groups = fl.prepare_fuzz("02_parts/parts_x.csv")

    graphs=[]
    strs=[]

    #Grafico e resultados para Tempo
    graph_tempo = build_graph_tempo(tempo,groups)
    str_resultado_tempo = get_tempo_result_string(groups,tempo)
    graphs.append(graph_tempo)
    strs.append(str_resultado_tempo)

    #Grafico e resultados para Fator de Utilização
    graph_fator = build_graph_fator(fator,groups)
    str_resultado_fator = get_fator_result_string(groups,fator)
    graphs.append(graph_fator)
    strs.append(str_resultado_fator)

    #Grafico e resultados para Número de Funcionários
    graph_funcionarios = build_graph_funcionarios(funcionarios,groups)
    str_resultado_funcionarios = get_funcionarios_result_string(groups,funcionarios)
    graphs.append(graph_funcionarios)
    strs.append(str_resultado_funcionarios)

    return (graphs,strs,groups)

#Constroi e seta atributos do grafico de Número de Funcionários
def build_graph_funcionarios(funcionarios,groups):
    graph = go.Figure()
    x_mp = np.linspace(0.0,0.6,int(0.6*100.0))
    x_p = np.linspace(0.4,0.8,int((0.8-0.4)*10000.0))
    x_m = np.linspace(0.6,1.0,int((1.0-0.6)*1000.0))
    
    graph.add_trace(go.Scatter(x=x_mp, y=ut.array_apply(x_mp,groups[6].f), mode='lines', name="Pequeno"))
    graph.add_trace(go.Scatter(x=x_p, y=ut.array_apply(x_p,groups[7].f), mode='lines', name="Médio"))
    graph.add_trace(go.Scatter(x=x_m, y=ut.array_apply(x_m,groups[8].f), mode='lines', name="Grande"))
    graph.add_vline(x=funcionarios, line_width=3, line_dash="dash",line_color="green")

    graph.update_layout(width=840, height = 280, margin = dict(t=20,b=0), xaxis_title="Número de Funcionários", yaxis_title="Pertinência", title = "Número de Funcionários (s)")
    return graph

#Constroi e seta atributos do grafico de tempo
def build_graph_tempo(tempo,groups):
    graph = go.Figure()
    x_mp = np.linspace(0.0,0.3,int(0.3*1000.0))
    x_p = np.linspace(0.1,0.5,int((0.5-0.1)*1000.0))
    x_m = np.linspace(0.4,0.7,int((0.7-0.4)*1000.0))

    graph.add_trace(go.Scatter(x=x_mp, y=ut.array_apply(x_mp,groups[0].f), mode='lines', name="Muito Pequeno"))
    graph.add_trace(go.Scatter(x=x_p, y=ut.array_apply(x_p,groups[1].f), mode='lines', name="Pequeno"))
    graph.add_trace(go.Scatter(x=x_m, y=ut.array_apply(x_m,groups[2].f), mode='lines', name="Médio"))
    graph.add_vline(x=tempo, line_width=3, line_dash="dash",line_color="green")

    graph.update_layout(width=840, height = 280, margin = dict(t=20,b=0), xaxis_title="Tempo Médio de Espera", yaxis_title="Pertinência", title = "Tempo Médio de Espera (m)")
    return graph

#Constroi e seta atributos do grafico de fator
def build_graph_fator(fator,groups):
    graph = go.Figure()
    x_b = np.linspace(0.0,0.4,int(0.4*1000.0))
    x_m = np.linspace(0.3,0.7,int((0.7-0.3)*1000.0))
    x_a = np.linspace(0.6,1.0,int((1.0-0.6)*1000.0))

    graph.add_trace(go.Scatter(x=x_b, y=ut.array_apply(x_b,groups[3].f), mode='lines', name="Baixo"))
    graph.add_trace(go.Scatter(x=x_m, y=ut.array_apply(x_m,groups[4].f), mode='lines', name="Médio"))
    graph.add_trace(go.Scatter(x=x_a, y=ut.array_apply(x_a,groups[5].f), mode='lines', name="Alto"))
    graph.add_vline(x=fator, line_width=3, line_dash="dash",line_color="green")
    
    graph.update_layout(width=840, height = 280, margin = dict(t=20,b=0), xaxis_title="Fator de Utilização", yaxis_title="Pertinência", title = f"Fator de Utilização(p) (Não Aplicável)")
    return graph

#Retorna string para imprimir resultado da fuzzificação do Número de Funcionários
def get_funcionarios_result_string(groups,funcionarios):
    return f"Número de Funcionários: x = {'{0:.3f}'.format(funcionarios)}  \n Pequeno (p): {'{0:.3f}'.format(groups[6].f(funcionarios))}  \n Médio (m): {'{0:.3f}'.format(groups[7].f(funcionarios))}  \n Grande(g): {'{0:.3f}'.format(groups[8].f(funcionarios))}"

#Retorna string para imprimir resultado da fuzzificação do Fator de Utilização
def get_fator_result_string(groups,fator):
    return f"Fator de Utilização: x = {'{0:.3f}'.format(fator)}  \n Baixo (b): {'{0:.3f}'.format(groups[3].f(fator))}  \n Médio (m): {'{0:.3f}'.format(groups[4].f(fator))}  \n Alto (a): {'{0:.3f}'.format(groups[5].f(fator))}"

#Retorna string para imprimir resultado da fuzzificação do tempo de espera
def get_tempo_result_string(groups,tempo):
    return f"Tempo: x = {'{0:.3f}'.format(tempo)}  \n Muito Pequeno (mp): {'{0:.3f}'.format(groups[0].f(tempo))}  \n Pequeno (p): {'{0:.3f}'.format(groups[1].f(tempo))}  \n Médio (m): {'{0:.3f}'.format(groups[2].f(tempo))}"

#Calcula e retorna os resultados da inferência
def infer(groups,tempo,funcionarios):
    rules = fl.prepare_infer_assoc_mem("02_parts/parts_rules.csv")
    
    val_tempo = [groups[0].f(tempo),groups[1].f(tempo),groups[2].f(tempo)]
    val_fator = [groups[3].f(funcionarios),groups[4].f(funcionarios),groups[5].f(funcionarios)]
    
    #R1 - Se g e mp entao mp
    rules[0].values[0] = val_tempo[0]
    rules[0].values[1] = val_fator[0]
    rules[0].values[2] = min(rules[0].values[0], rules[0].values[1])
    
    #R2 - Se g e p entao p
    rules[1].values[0] = val_tempo[0]
    rules[1].values[1] = val_fator[1]
    rules[1].values[2] = min(rules[1].values[0], rules[1].values[1])

    #R3 - Se g e m entao mp
    rules[2].values[0] = val_tempo[0]
    rules[2].values[1] = val_fator[2]
    rules[2].values[2] = min(rules[2].values[0], rules[2].values[1])

    #R4 - Se m e mp entao pg
    rules[3].values[0] = val_tempo[1]
    rules[3].values[1] = val_fator[0]
    rules[3].values[2] = min(rules[3].values[0], rules[3].values[1])

    #R5 - Se m e p entao pp
    rules[4].values[0] = val_tempo[1]
    rules[4].values[1] = val_fator[1]
    rules[4].values[2] = min(rules[4].values[0], rules[4].values[1])

    #R6 - Se m e m entao p
    rules[5].values[0] = val_tempo[1]
    rules[5].values[1] = val_fator[2]
    rules[5].values[2] = min(rules[5].values[0], rules[5].values[1])

    rules[6].values[0] = val_tempo[2]
    rules[6].values[1] = val_fator[0]
    rules[6].values[2] = min(rules[6].values[0], rules[6].values[1])

    #R8 - Se p e p entao g
    rules[7].values[0] = val_tempo[2]
    rules[7].values[1] = val_fator[1]
    rules[7].values[2] = min(rules[7].values[0], rules[7].values[1])

    #R9 - Se p e m entao m
    rules[8].values[0] = val_tempo[2]
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
        if rule.vars[-1] == "mp":
            index = 0
        elif rule.vars[-1] == "p":
            index = 1
        elif rule.vars[-1] == "pp":
            index = 2
        elif rule.vars[-1] == "m":
            index = 3
        elif rule.vars[-1] == "pg":
            index = 4
        elif rule.vars[-1] == "g":
            index = 5
        elif rule.vars[-1] == "mg":
            index = 6
        else:
            print("DUMB "+str(rule.vars))
        
        if rules_sel[index] is None or rules_sel[index].values[-1] < rule.values[-1]:
            rules_sel[index] = rules[i]

    rules_max_min=[]

    for i in range(len(rules_sel)):
        if rules_sel[i] is not None and rules_sel[i].values[-1] > 0.0:
            rules_max_min.append(rules_sel[i])
    
    return rules_max_min
