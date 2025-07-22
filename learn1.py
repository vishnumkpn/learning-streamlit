import streamlit as st

st.title("Admin Dashboard")
st.subheader("The below data is visualized for college admins")
st.text("Welcome ADMIN")
st.write("Happy / Sad")
moodArr= ["", "Happy", "Sad", "Motivated"]
mood = st.selectbox("Your mood: ", moodArr)
if mood==moodArr[1]:
    st.success("Lets fucking go, have a great day ahead")
elif mood==moodArr[2]:
    st.write("I'm sorry you're having a bad day, keep pushing you're gonna be okay")
elif mood==moodArr[3]:
    st.success("Who is the boss, thats right you are")