import re
import pandas as pd
import streamlit as st
from glob import glob
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode

@st.cache
def generate_data(file_path=r"data\us-counties-2020-2023.feather"):
    return pd.read_feather(file_path)

def aggrid_interactive_table(df: pd.DataFrame):
    """Creates an st-aggrid interactive table based on a dataframe.

    Args:
        df (pd.DataFrame]): Source dataframe

    Returns:
        dict: The selected row
    """
    options = GridOptionsBuilder.from_dataframe(
        df, enableRowGroup=True, enableValue=True, enablePivot=True
    )

    options.configure_side_bar()

    options.configure_selection("single")
    selection = AgGrid(
        df,
        height = 300,
        enable_enterprise_modules=True,
        gridOptions=options.build(),
        update_mode=GridUpdateMode.MODEL_CHANGED,
        allow_unsafe_jscode=True,
    )

    return selection

def generate_states_county(file_path = r"data\us-states-county.csv"):
    df = pd.read_csv(file_path)
    return df.loc[:,'state'].unique(),df.loc[:,'county'].unique()
