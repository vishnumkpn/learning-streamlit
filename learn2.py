import streamlit as st

st.title("Dashboard app")

mkdsh=st.button("Update dashboard")
if mkdsh:
    st.success("Updated dashboard displayed below")

attrib = st.radio("Analysis attributes: ", ['Std','Mean','Range','Min','Max'])
st.write(f'Atribute selected: {attrib}')

lev = st.slider("Intensity",0,100,50)

nu = st.number_input("Vals", min_value=0, max_value=10, step=2)

te= st.text_input("Name: ")