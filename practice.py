import streamlit as st
import pandas as pd
import numpy as np
import time

st.title("Frist Day In Streamlit")
a=[1,2,3,4,5,6,7,8,9,10]
n=np.array(a)
#print(n)
nd=n.reshape((2,5))
#print(nd)
dic={"name":'subash sigdel',
     "age":'19',
     "city":'kathmandu'}
data=pd.read_csv('data.csv')
#print(data)
st.dataframe(data)
st.table(n)
st.json(dic)
st.write(a)



@st.cache
def ret_time (dic):
     time.sleep(5)
     return time.time()


if st.checkbox("1"):
     st.write(ret_time())

if st.checkbox("2"):
     st.write(ret_time())