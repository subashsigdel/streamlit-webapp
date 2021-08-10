import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

st.title("visualizing data in streamlit")

data=pd.DataFrame(np.random.rand(5,3),columns=['a','b','c'])
#print(data)
st.write("# line chart")
st.line_chart(data)

st.write("# area chart")
st.area_chart(data)

st.write("# bar cchart")
st.bar_chart(data)

st.write("# using matplotlib for visualization")
plt.scatter(data['a'],data['b'])
st.pyplot()


st.write("# using altair for visulaization")
charts=alt.Chart(data).mark_circle().encode(x='a',y='b',tooltip=['a','b'])
st.altair_chart(charts,use_container_width=True)


st.write("# drawing flow chart")
st.graphviz_chart("""
digraph{
watch -> like
like -> share
share -> subscribe
share ->watch
}
""")

st.write("# drawing map in streamlit")
st.map()

st.write("# adding image in streamlit")
st.image("download.png")


st.write("# adding video in streamlit")
st.video("output_video.mp4")