import streamlit as st
import numpy as np
import pandas as pd
st.title("My First Streamlit App")
st.write(":streamlit: Hello, World!")
st.text("This is a simple Streamlit app.")
st.subheader("DataFrame Example")

name = st.text_input("Enter your name:")
if st.button("Submit"):
    st.success(f"Hello, {name}!")

    # displaying data
    df = pd.DataFrame(np.random.randn(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
    st.line_chart(df)
    st.bar_chart(df)


    #media layout
    st.sidebar.header("Media Example")
    st.image("img.png", width=200)
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    st.video("https://www.youtube.com/watch?v=2Vv-BfVoq4g")

    #upload file
upload_file = st.file_uploader("Upload a file", type=['csv', 'xlsx'])

if upload_file is not None:
    try:
        if upload_file.name.endswith('.csv'):
            df = pd.read_csv(upload_file)
        else:
            df = pd.read_excel(upload_file)

        st.subheader("Uploaded Data")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Error reading file: {e}")


st.title("Text and markdown demo")
st.header("this is header")
st.subheader("this is sub header")
st.markdown("**Bold**,**Italic*, `Code`, [Link](https://www.streamlit.io/)")
st.code("print('Hello, Streamlit!')", language='python')
st.text_input("enter your name")
st.text_area("write something")
st.number_input("pick a number", min_value=0, max_value=100, value=50)
st.slider("choose a range", 0, 100)
st.selectbox("select an programming language", ["Java", "Python", "JavaScript"])
st.multiselect("select multiple roles", ["tester", "developer", "manager"])
st.radio("select one option", ["male", "female", "other"])
st.checkbox("I agree to the terms and conditions")



if st.checkbox("show details"):
    st.info("Here are some details about the app...")

    option = st.radio("Choose a view", ["show chart", "show table"])
    if option == "show chart":
        st.write("chart would appear here")
    else:
        st.write("table would appear here")

