# import streamlit as st
import fuzzylib as fl

function = lambda x: x**2
xs = [1,2,3]

k = fl.fuzzify(xs,function)
print(k)

fl.prepare_run("wash.csv")

# st.write("Hello World")