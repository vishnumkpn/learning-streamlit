import streamlit as st

st.title("Poll")

col1, col2 = st.columns(2)
if "v1" not in st.session_state:
    st.session_state.v1 = 0
if "v2" not in st.session_state:
    st.session_state.v2 = 0

with col1:
    st.header("Happy")
    vot1 = st.button("Vote for Happy")
    if vot1:
        st.session_state.v1+=1
        st.success("Your vote has been recorded")
with col2:
    st.header("Sad")
    vot2 = st.button("Vote for Sad")
    if vot2:
        st.session_state.v2+=1
        st.success("Your vote has been recorded")

if st.button("Show results"):
    st.text(f"Vote count for Happy {st.session_state.v1} and Vote count for sad {st.session_state.v2}")