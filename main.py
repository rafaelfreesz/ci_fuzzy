# import streamlit as st
import fuzzylib as fl

function = lambda x: x**2
xs = [1,2,3]

k = fl.fuzzify(xs,function)
print(k)

# st.write("Hello World")