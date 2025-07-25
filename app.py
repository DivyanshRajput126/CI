import streamlit as st


st.title("Power Calculator")
st.write("Enter the number to calculate its square, cube, and fifth power.")

n = st.number_input("Enter a number:", value=1,step=1)

square = n ** 2
cube = n ** 3
fifth_power = n ** 5

st.write(f"Square: {square}")
st.write(f"Cube: {cube}")
st.write(f"Fifth Power: {fifth_power}")