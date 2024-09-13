import numpy as np
import fuzzylib as fl
import utils as ut
import plotly.graph_objects as go

def set_graph(sujeira):
    xi = np.linspace(0,100,101)
    groups = fl.prepare("01_wash/wash_x.csv")
    k = ut.group_by(groups,"f_name")

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=xi, y=ut.array_apply(xi,groups[0].function), mode='lines', name=f"{groups[0].f_name}_{groups[0].f_spec}"))
    fig.add_trace(go.Scatter(x=xi, y=ut.array_apply(xi,groups[1].function), mode='lines', name=f"{groups[1].f_name}_{groups[1].f_spec}"))
    fig.add_trace(go.Scatter(x=xi, y=ut.array_apply(xi,groups[2].function), mode='lines', name=f"{groups[2].f_name}_{groups[2].f_spec}"))
    fig.add_vline(x=sujeira, line_width=3, line_dash="dash",line_color="green")

    return fig