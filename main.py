import streamlit as st
st.title("hello world")
st.header("header")
st.subheader("suheader")

st.text("hello i am subash sigdel")
st.markdown(""" # h1 tag
## h2 tag
### h3 tag
:moon: <br> 
:sunglasses:
""",True)

st.write("# subash")

st.write(st)
d={"a":'subash',
   "b":'sigdel'}
st.write(d)