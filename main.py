import streamlit as st
import fuzzylib as fl
import plotly.graph_objects as go
import numpy as np



groups = fl.prepare("01_wash/wash.csv")

st.write("GRAFICOS")
# st.line_chart(groups[0].function(1))

def apply(xs,fun):
    res = []
    for x in range(len(xs)):
        res.append(fun(x))
    return res

xi = np.linspace(0,100,200)

fig = go.Figure()
fig.add_trace(go.Scatter(x=xi, y=apply(xi,groups[0].function), mode='lines', name=f"{groups[0].f_name}_{groups[0].f_spec}"))
fig.add_trace(go.Scatter(x=xi, y=apply(xi,groups[1].function), mode='lines', name=f"{groups[1].f_name}_{groups[1].f_spec}"))
fig.add_trace(go.Scatter(x=xi, y=apply(xi,groups[2].function), mode='lines', name=f"{groups[2].f_name}_{groups[2].f_spec}"))
st.plotly_chart(fig)

# k = fl.fuzzify(xs,function)
# print(k)
# for i in range(len(groups)):
#     print(groups[i])

# st.write("Hello World")