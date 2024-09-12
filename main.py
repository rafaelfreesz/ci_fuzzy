import streamlit as st
import fuzzylib as fl
import fuzzygroup as fg
import plotly.graph_objects as go
import numpy as np



groups = fl.prepare("01_wash/wash.csv")

st.write("GRAFICOS")
# st.line_chart(groups[0].function(1))

def uuu(x):
    return x**3

xi = np.linspace(0,10,11)

fig = go.Figure()
fig.add_trace(go.Scatter(x=xi, y=uuu(xi), mode='lines', name='lines'))
fig.add_trace(go.Scatter(x=xi, y=200*xi+2, mode='lines', name='bull'))
st.plotly_chart(fig)

# k = fl.fuzzify(xs,function)
# print(k)
# for i in range(len(groups)):
#     print(groups[i])

# st.write("Hello World")