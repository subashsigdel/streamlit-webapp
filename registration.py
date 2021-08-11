import streamlit as st

st.title("registration Form")

first,last=st.columns(2)
first.text_input("first name")
last.text_input("last name")

email,mob=st.columns([3,2])
email.text_input("email")
mob.text_input("mobile number")

user,pw,pw2=st.columns(3)
user.text_input("enter username")
pw.text_input("enter password",type="password")
pw2.text_input("retype password",type="password")

ch,bl,sub=st.columns(3)
ch.checkbox("I agree terms and conditions")
sub.button("submit")