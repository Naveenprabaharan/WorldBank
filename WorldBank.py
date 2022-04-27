import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
import streamlit as st

# showing title 
st.title("World data bank - India")
#India = pd.read_csv('World_Bank_India.csv')

#edited

India = pd.read_csv('World_Bank_India.csv',skiprows=4)
st.write(India)
st.write(India.index)
# individual row
st.title("World data bank - India")
id1 = India[0:10][0:3]
st.write(id1)
