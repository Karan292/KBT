import streamlit as st

st.title("welcome to basic streamlit app")

age =st.slider("Select your age ", 1 , 100)
city =st.selectbox("Select your city",["Delhi", "Mumbai" ,"Nashik", "pune"])

if st.button("show details"):
    st.write("Age", age)
    st.write("City", city)