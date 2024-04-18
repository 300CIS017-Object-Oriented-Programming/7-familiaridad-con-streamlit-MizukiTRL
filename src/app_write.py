import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.header("st.write")

st.write("hello, world")

st.write(12245)

df = pd.DataFrame({
    "col 1": [1, 2, 3, 4], "col 2": [4, 6, 2, 6]
})

st.write(df)

st.write("dataframe: ", df, "end of data :b")

df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns = ["a", "b", "c"]
)
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
)

st.write("dataframe: ", df2)
st.write("alt chart: ", c)