import streamlit as st
import plotly.graph_objects as go
import probwash as p_wash


def run_wash():
    sujeira = st.sidebar.slider("Selecione a quantidade de sujeira:", min_value=0, max_value=100,value=50,step=1)
    mancha = st.sidebar.slider("Selecione a quantidade de manchas:", min_value=0, max_value=100,value=50,step=1)
    metodo_defuzz = st.sidebar.selectbox(
        "Selecione o Método de Defuzzificação:",
        ("Média Ponderada","Centro de Gravidade - CoG"),
        index=0
    )

    graphs,strs, groups = p_wash.fuzzify(sujeira, mancha)

    st.write("### 1. Fuzzificação")

    #Imprimindo Gráfico de Sujeira
    st.plotly_chart(graphs[0])
    st.write(strs[0])
    
    #Imprimindo Gráfico de Mancha
    st.plotly_chart(graphs[1])
    st.write(strs[1])
    
    st.write("### 2. Inferência")

    rules, str_rules, triggered_rules, str_triggered_rules = p_wash.infer(groups,sujeira,mancha)
    
    st.write(str_rules + "\n Regras selecionadas de acordo com critério MAX-MIN:\n" + str_triggered_rules)


    st.write("### 3. Defuzzificação")

    graph_y, res_str = p_wash.defuzzify(groups,triggered_rules, "mamdani")
    st.plotly_chart(graph_y)
    st.write(res_str)
    st.write("FIM")

problema_selecionado = st.sidebar.selectbox(
    "Selecione um Problema:",
    ("Home","Máquina de Lavar","Autopeças"),
    index=1
)

if problema_selecionado == "Máquina de Lavar":
    run_wash()