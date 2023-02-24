import re
import pandas as pd
import streamlit as st
from glob import glob
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode
import plotly_express as px
import plotly.graph_objects as go

def generate_covid_data(file_path=r"data\us-counties-2022.csv"):
    df = pd.read_csv(file_path)
    df['date'] = pd.to_datetime(df['date'])
    return df

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

def build_county_to_state_figure(df: pd.DataFrame):
    return px.line(df, x="date", y="cases", color = 'county',height=400)

def build_state_lat_lng_figure(df: pd.DataFrame):
    # px.set_mapbox_access_token(open(".mapbox_token").read())
    fig = px.scatter_mapbox(df,
                        lat='lat',
                        lon='lon',
                        hover_name='name',
                        color_discrete_sequence=["fuchsia"], zoom=3, height= 500)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(
        title = 'Covid impact in US<br>(Hover for state names)',
        geo_scope='usa',
    )

    return fig