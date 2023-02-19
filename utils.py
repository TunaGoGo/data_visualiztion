import re
import pandas as pd
import streamlit as st
from glob import glob

@st.cache
def generate_data(file_path=r"data\*.csv"):
    file_path_ = glob(file_path)
    arr = []
    for i in file_path_[:4]:
        df = pd.read_csv(i)
        arr.append(df)
    
    df = pd.concat(arr)
    return df