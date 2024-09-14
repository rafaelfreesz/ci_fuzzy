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
    print(groups[6])
    print(groups[7])
    print(groups[8])
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
