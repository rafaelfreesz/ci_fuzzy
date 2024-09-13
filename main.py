import streamlit as st
import plotly.graph_objects as go
import probmaq as pmaq

problema_selecionado = st.sidebar.selectbox(
    "Selecione um Problema:",
    ("Home","Máquina de Lavar","Autopeças"),
    index=1
)

if problema_selecionado == "Máquina de Lavar":
    
    sujeira = st.sidebar.slider("Selecione a quantidade de sujeira:", min_value=0, max_value=100,value=50,step=1)

    graph=pmaq.set_graph(sujeira)

    st.write("GRAFICOS")
    st.plotly_chart(graph)
    st.write("FIM")