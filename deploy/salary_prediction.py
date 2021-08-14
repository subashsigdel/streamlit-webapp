import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

data = pd.read_csv("Salary_Data.csv")
x = np.array(data['YearsExperience']).reshape(-1, 1)
lr = LinearRegression()
lr.fit(x, np.array(data['Salary']))

st.title("Salary Predictor")
st.image("salla.jpg", width=800)
nav = st.sidebar.radio("Navigation", ["Home", "Prediction", "bored?"])
if nav == "Home":

    if st.checkbox("Show Table"):
        st.table(data)


if nav == "Prediction":
    st.header("Know your Salary")
    val = st.number_input("Enter you exp", 0.00, 20.00, step=0.25)
    val = np.array(val).reshape(1, -1)
    pred = lr.predict(val)[0]

    if st.button("Predict"):
        st.success(f"Your predicted salary is {round(pred)}")

if nav == "bored?":
    st.title("number guessing game")
    st.header("start guessing game")
    if st.button('yup!!'):
        st.write("step1: think of a number.")
    if st.button('ok'):
        st.write("step2: double it")
    if st.button('done'):
        st.write("step3: add 6 in it")
    if st.button("if done click here"):
        st.write("step4: divide the number you got with 2")
    if st.button("after that.."):
        st.write("step5: subtract the number with number you started ")
        st.write("# your answer is 3")



