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
