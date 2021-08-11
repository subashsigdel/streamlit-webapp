import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import time

plt.style.use("ggplot")
data={
    "num":[x for x in range(1,11)],
    "square":[x**2 for x in range(1,11)],
    "twice":[x*2 for x in range(1,11)],
    "thrice":[x*3 for x in range(1,11)]
}
df=pd.DataFrame(data)

rad=st.sidebar.radio("navigation",["home","about us"])
if rad=="about us":
    st.write("hello i am a developer")

if rad=="home":
    x=st.sidebar.selectbox("select x axis",df.columns)
    y=st.sidebar.selectbox("select y axis",df.columns)
    plt.plot(df[x],df[y])
    st.pyplot()