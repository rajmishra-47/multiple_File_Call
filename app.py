import streamlit as st
from a2 import apple

st.title("hello")

x=st.text_input("Enter a Number")

if x:
    st.write(apple(x))