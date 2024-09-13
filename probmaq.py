import numpy as np
import fuzzylib as fl
import utils as ut
import plotly.graph_objects as go

def infer():
    fl.prepare_infer_assoc_mem("01_wash/wash_rules.csv")

#Calcula e retorna os valores e gráficos para a Fuzzificação
def set_values(sujeira, mancha):
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