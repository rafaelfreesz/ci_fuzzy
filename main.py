import streamlit as st
import fuzzylib as fl
import plotly.graph_objects as go
import numpy as np
import utils as ut


groups = fl.prepare("01_wash/wash_x.csv")

k = ut.group_by(groups,"f_name")


print(k)

xi = np.linspace(0,100,101)

x_selecionado = st.sidebar.slider("Selecione a idade:", min_value=0, max_value=100,value=50,step=1)

fig = go.Figure()
fig.add_trace(go.Scatter(x=xi, y=ut.array_apply(xi,groups[0].function), mode='lines', name=f"{groups[0].f_name}_{groups[0].f_spec}"))
fig.add_trace(go.Scatter(x=xi, y=ut.array_apply(xi,groups[1].function), mode='lines', name=f"{groups[1].f_name}_{groups[1].f_spec}"))
fig.add_trace(go.Scatter(x=xi, y=ut.array_apply(xi,groups[2].function), mode='lines', name=f"{groups[2].f_name}_{groups[2].f_spec}"))
fig.add_vline(x=x_selecionado, line_width=3, line_dash="dash",line_color="green")


st.write("GRAFICOS")
st.plotly_chart(fig)
st.write("FIM")

# k = fl.fuzzify(xs,function)
# print(k)
# for i in range(len(groups)):
#     print(groups[i])

st.write("Hello World")