import pickle
import pandas as pd
import streamlit as st
#import numpy as np
#from pycaret.classification import *
import matplotlib.pyplot as plt
#import seaborn as sns
#from sklearn import preprocessing

# load the model from disk
#loaded_model = pickle.load(open(r'C:\users\lenovo\desktop\msdeclassifrf.pkl', 'rb'))

# Creating the Titles and Image
st.title("Predict loans")
st.header("how to predict loans")

uploaded_file = st.file_uploader("Choose a file to load tabboun mouk")
if uploaded_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    df = pd.read_csv(uploaded_file)
    st.write(df)
    model_loan=pickle.load(open(r'C:\users\lenovo\desktop\msdeclassifrf.pkl', 'rb'))
    prediction = model_loan.predict(df)
    prediction_proba = model_loan.predict_proba(df)
    
