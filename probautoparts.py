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

    return (graphs,strs,groups)

#Constroi e seta atributos do grafico de tempo
def build_graph_tempo(tempo,groups):
    graph = go.Figure()
    x_mp = np.linspace(0.0,0.3,int(0.3*100.0))
    x_p = np.linspace(0.1,0.5,int((0.5-0.1)*100.0))
    x_m = np.linspace(0.4,0.7,int((0.7-0.4)*100.0))

    graph.add_trace(go.Scatter(x=x_mp, y=ut.array_apply(x_mp,groups[0].f), mode='lines', name=f"{groups[0].f_name}_{groups[0].f_spec}"))
    graph.add_trace(go.Scatter(x=x_p, y=ut.array_apply(x_p,groups[1].f), mode='lines', name=f"{groups[1].f_name}_{groups[1].f_spec}"))
    graph.add_trace(go.Scatter(x=x_m, y=ut.array_apply(x_m,groups[2].f), mode='lines', name=f"{groups[2].f_name}_{groups[2].f_spec}"))
    graph.add_vline(x=tempo, line_width=3, line_dash="dash",line_color="green")

    graph.update_layout(width=480, height = 180, margin = dict(t=20,b=0), title = "Tempo Médio de Espera")
    return graph

#Constroi e seta atributos do grafico de fator
def build_graph_fator(fator,groups):
    graph = go.Figure()
    x_b = np.linspace(0.0,0.4,int(0.4*100.0))
    x_m = np.linspace(0.3,0.7,int((0.7-0.3)*100.0))
    x_a = np.linspace(0.6,1.0,int((1.0-0.6)*100.0))
    print(groups[3])
    print(groups[4])
    print(groups[5])
    graph.add_trace(go.Scatter(x=x_b, y=ut.array_apply(x_b,groups[3].f), mode='lines', name=f"{groups[3].f_name}_{groups[3].f_spec}"))
    graph.add_trace(go.Scatter(x=x_m, y=ut.array_apply(x_m,groups[4].f), mode='lines', name=f"{groups[4].f_name}_{groups[4].f_spec}"))
    graph.add_trace(go.Scatter(x=x_a, y=ut.array_apply(x_a,groups[5].f), mode='lines', name=f"{groups[5].f_name}_{groups[5].f_spec}"))
    graph.add_vline(x=fator, line_width=3, line_dash="dash",line_color="green")

    graph.update_layout(width=480, height = 180, margin = dict(t=20,b=0), title = "Fator de Utilização")
    return graph

#Retorna string para imprimir resultado da fuzzificação do Fator de Utilização
def get_fator_result_string(groups,fator):
    return f"Fator de Utilização: x = {'{0:.3f}'.format(fator)}  \n Baixo (b): {'{0:.3f}'.format(groups[3].f(fator))}  \n Médio (m): {'{0:.3f}'.format(groups[4].f(fator))}  \n Alto (a): {'{0:.3f}'.format(groups[5].f(fator))}"

#Retorna string para imprimir resultado da fuzzificação do tempo de espera
def get_tempo_result_string(groups,tempo):
    return f"Tempo: x = {'{0:.3f}'.format(tempo)}  \n Muito Pequeno (mp): {'{0:.3f}'.format(groups[0].f(tempo))}  \n Pequeno (p): {'{0:.3f}'.format(groups[1].f(tempo))}  \n Médio (m): {'{0:.3f}'.format(groups[2].f(tempo))}"
