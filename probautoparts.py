import numpy as np
import fuzzylib as fl
import utils as ut
import plotly.graph_objects as go
import copy

def fuzzify(tempo, fator, funcionarios):
    groups = fl.prepare_fuzz("02_autoparts/autoparts_x.csv")

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
    
    graph.add_trace(go.Scatter(x=x_mp, y=ut.array_apply(x_mp,groups[6].f), mode='lines', name=f"{groups[6].f_name}_{groups[6].f_spec}"))
    graph.add_trace(go.Scatter(x=x_p, y=ut.array_apply(x_p,groups[7].f), mode='lines', name=f"{groups[7].f_name}_{groups[7].f_spec}"))
    graph.add_trace(go.Scatter(x=x_m, y=ut.array_apply(x_m,groups[8].f), mode='lines', name=f"{groups[8].f_name}_{groups[8].f_spec}"))
    graph.add_vline(x=funcionarios, line_width=3, line_dash="dash",line_color="green")

    graph.update_layout(width=480, height = 180, margin = dict(t=20,b=0), title = "Número de Funcionários")
    return graph

#Constroi e seta atributos do grafico de tempo
def build_graph_tempo(tempo,groups):
    graph = go.Figure()
    x_mp = np.linspace(0.0,0.3,int(0.3*1000.0))
    x_p = np.linspace(0.1,0.5,int((0.5-0.1)*1000.0))
    x_m = np.linspace(0.4,0.7,int((0.7-0.4)*1000.0))

    graph.add_trace(go.Scatter(x=x_mp, y=ut.array_apply(x_mp,groups[0].f), mode='lines', name=f"{groups[0].f_name}_{groups[0].f_spec}"))
    graph.add_trace(go.Scatter(x=x_p, y=ut.array_apply(x_p,groups[1].f), mode='lines', name=f"{groups[1].f_name}_{groups[1].f_spec}"))
    graph.add_trace(go.Scatter(x=x_m, y=ut.array_apply(x_m,groups[2].f), mode='lines', name=f"{groups[2].f_name}_{groups[2].f_spec}"))
    graph.add_vline(x=tempo, line_width=3, line_dash="dash",line_color="green")

    graph.update_layout(width=480, height = 180, margin = dict(t=20,b=0), title = "Tempo Médio de Espera")
    return graph

#Constroi e seta atributos do grafico de fator
def build_graph_fator(fator,groups):
    graph = go.Figure()
    x_b = np.linspace(0.0,0.4,int(0.4*1000.0))
    x_m = np.linspace(0.3,0.7,int((0.7-0.3)*1000.0))
    x_a = np.linspace(0.6,1.0,int((1.0-0.6)*1000.0))

    graph.add_trace(go.Scatter(x=x_b, y=ut.array_apply(x_b,groups[3].f), mode='lines', name=f"{groups[3].f_name}_{groups[3].f_spec}"))
    graph.add_trace(go.Scatter(x=x_m, y=ut.array_apply(x_m,groups[4].f), mode='lines', name=f"{groups[4].f_name}_{groups[4].f_spec}"))
    graph.add_trace(go.Scatter(x=x_a, y=ut.array_apply(x_a,groups[5].f), mode='lines', name=f"{groups[5].f_name}_{groups[5].f_spec}"))
    graph.add_vline(x=fator, line_width=3, line_dash="dash",line_color="green")

    graph.update_layout(width=480, height = 180, margin = dict(t=20,b=0), title = "Fator de Utilização")
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
def infer(groups,tempo,fator,funcionarios):
    rules = fl.prepare_infer_assoc_mem("02_autoparts/autoparts_rules.csv")

    val_tempo = [groups[0].f(tempo),groups[1].f(tempo),groups[2].f(tempo)]
    val_fator = [groups[3].f(fator),groups[4].f(fator),groups[5].f(fator)]

    rules[0].values[0] = val_tempo[0]
    rules[0].values[1] = val_fator[0]
    rules[0].values[2] = min(rules[0].values[0], rules[0].values[1])
    
    rules[1].values[0] = val_tempo[0]
    rules[1].values[1] = val_fator[1]
    rules[1].values[2] = min(rules[1].values[0], rules[1].values[1])

    rules[2].values[0] = val_tempo[0]
    rules[2].values[1] = val_fator[2]
    rules[2].values[2] = min(rules[2].values[0], rules[2].values[1])

    rules[3].values[0] = val_tempo[1]
    rules[3].values[1] = val_fator[0]
    rules[3].values[2] = min(rules[3].values[0], rules[3].values[1])

    rules[4].values[0] = val_tempo[1]
    rules[4].values[1] = val_fator[1]
    rules[4].values[2] = min(rules[4].values[0], rules[4].values[1])

    rules[5].values[0] = val_tempo[1]
    rules[5].values[1] = val_fator[2]
    rules[5].values[2] = min(rules[5].values[0], rules[5].values[1])

    rules[6].values[0] = val_tempo[2]
    rules[6].values[1] = val_fator[0]
    rules[6].values[2] = min(rules[6].values[0], rules[6].values[1])

    rules[7].values[0] = val_tempo[2]
    rules[7].values[1] = val_fator[1]
    rules[7].values[2] = min(rules[7].values[0], rules[7].values[1])

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

    # for i in range(len(rules)):
    #     print(rules[i])

    for i in range(len(rules)):
        rule = rules[i]
        index = -1
        # print(rule)
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
