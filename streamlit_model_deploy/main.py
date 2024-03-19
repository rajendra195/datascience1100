import streamlit as st
import pickle

with open("model.pickle", "rb") as file:
    model = pickle.load(file)

st.title("Salary Prediction App")
yoe = st.text_input("Enter Years of experience")

if st.button("submit"):
    yoe = int(yoe)
    y_pred = model.predict([[yoe]])
    st.text(f"Your expected salary is {round(y_pred[0])}.")