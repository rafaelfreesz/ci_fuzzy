import numpy as np
import fuzzylib as fl
import utils as ut
import plotly.graph_objects as go

def set_graph(sujeira):
    groups = fl.prepare("01_wash/wash_x.csv")
    k = ut.group_by(groups,"f_name")

    fig = go.Figure()

    x_ps = np.linspace(0,int(groups[0].b),int(groups[0].b)+1)
    x_ms = np.linspace(int(groups[1].a),int(groups[1].b),int(groups[1].b)+1)
    x_gs = np.linspace(int(groups[2].a),int(groups[2].m),int(groups[2].m-groups[2].a)+1)

    fig.add_trace(go.Scatter(x=x_ps, y=ut.array_apply(x_ps,groups[0].f), mode='lines', name=f"{groups[0].f_name}_{groups[0].f_spec}"))
    fig.add_trace(go.Scatter(x=x_ms, y=ut.array_apply(x_ms,groups[1].f), mode='lines', name=f"{groups[1].f_name}_{groups[1].f_spec}"))
    fig.add_trace(go.Scatter(x=x_gs, y=ut.array_apply(x_gs,groups[2].f), mode='lines', name=f"{groups[2].f_name}_{groups[2].f_spec}"))
    fig.add_vline(x=sujeira, line_width=3, line_dash="dash",line_color="green")

    return fig

