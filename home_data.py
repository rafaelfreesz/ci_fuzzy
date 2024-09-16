import plotly.graph_objects as go
import numpy as np

def build_text(source):
    f = open(source,"r",encoding='utf8')
    
    return f"{f.read()}"

def build_speed_distance_graph():
    velocidade = [30,40,50,60,70,80,90,100,110,120]
    dvu = [180,270,350,420,490,560,620,680,730,800]

    graph = go.Figure()
    xs = np.linspace(velocidade[0],velocidade[-1],len(velocidade))
    graph.add_trace(go.Scatter(x=xs, y=dvu, mode='lines'))
    graph.update_layout(title=f"Velocidade x distância", xaxis_title="Velocidade (km/h)", yaxis_title="Distância Percorrida(m)")
    return graph

