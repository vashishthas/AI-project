import streamlit as st
from run2 import *

opt = st.sidebar.selectbox("",("Home", "Identifier"))

if opt=="Home":
    html_temp = '''
        <div>
        <h2></h2>
        <center><h3>Language Identifier - An NLP Project</h3></center>
        </div>
        <hr>
        This project involves using Language Detection dataset for training a machine learning/deep learning algorithm. 
        <br>
        This dataset has two columns: text and language. After performing text preprocessing methods, you can use your preferred algorithm to predict the correct target variable of language for a given text.
        <br>
        <br>
        Head down to Indentify tab and enter the text of your chosen language and the algorithm will run the dataset and identify the language entered.
        <br>
        '''
    st.markdown(html_temp, unsafe_allow_html=True)
    st.header("")
    
else:
    input_txt = st.text_input('Input Text')
    if st.button("Identify"):
        output = predict(input_txt)
        st.success("The given text has been identified as '{}'".format(output))
