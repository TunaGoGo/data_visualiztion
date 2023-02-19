import streamlit as st
import pandas as pd
import utils as ut


df = pd.read_csv(r"data\us_county_latlng.csv")

st.map(data = df)

