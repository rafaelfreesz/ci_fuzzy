import streamlit as st
import plotly.graph_objects as go
import probmaq as pmaq


def run_wash():
    sujeira = st.sidebar.slider("Selecione a quantidade de sujeira:", min_value=0, max_value=100,value=50,step=1)
    mancha = st.sidebar.slider("Selecione a quantidade de manchas:", min_value=0, max_value=100,value=50,step=1)

    graphs,strs, groups = pmaq.fuzzify(sujeira, mancha)

    st.write("### 1. Fuzzificação")

    #Imprimindo Gráfico de Sujeira
    st.plotly_chart(graphs[0])
    st.write(strs[0])
    
    #Imprimindo Gráfico de Mancha
    st.plotly_chart(graphs[1])
    st.write(strs[1])
    
    st.write("### 2. Inferência")

    rules, str_rules = pmaq.infer(groups,sujeira,mancha)
    st.write(str_rules)

    st.write("### 3. Defuzzificação")

    graph_y = pmaq.defuzzify(groups,sujeira,mancha)
    st.plotly_chart(graph_y)
    st.write("FIM")

problema_selecionado = st.sidebar.selectbox(
    "Selecione um Problema:",
    ("Home","Máquina de Lavar","Autopeças"),
    index=1
)

if problema_selecionado == "Máquina de Lavar":
    run_wash()