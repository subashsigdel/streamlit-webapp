import streamlit as st

st.title("Adding Widget To The Streamlit")


name=st.text_input("enter your full name")
age=st.text_input("enter your age")
Class=st.text_input("enter your class")
school=st.text_input("enter your school name")
date=st.date_input("enter date")
time=st.time_input("enter time")
st.selectbox("select one",["happy","satisfied","normal"])
st.multiselect("select more than one",["1","2","3","4"])
st.slider("experience",min_value=0,max_value=10)
description=st.text_area("write about yourself")
st.file_uploader("upload the cv")
if st.checkbox("you accept the terms & conditions",value=False):
    if st.button("done"):
        st.write("hello",name,"thankyou for applying")


