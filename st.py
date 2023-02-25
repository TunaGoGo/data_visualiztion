import streamlit as st
import pandas as pd
import utils as ut
from streamlit_plotly_events import plotly_events

def initialize_state():
    """Initializes all filters and counter in Streamlit Session State
    """
    for q in ["county_index_list"]:
        if f"{q}_query" not in st.session_state:
            st.session_state[f"{q}_query"] = set()

    if "counter" not in st.session_state:
        st.session_state.counter = 0


def update_state(current_query):
    """Stores input dict of filters into Streamlit Session State.

    If one of the input filters is different from previous value in Session State, 
    rerun Streamlit to activate the filtering and plot updating with the new info in State.
    """
    rerun = False
    for q in ["bill_to_tip", "size_to_time", "day"]:
        if current_query[f"{q}_query"] - st.session_state[f"{q}_query"]:
            st.session_state[f"{q}_query"] = current_query[f"{q}_query"]
            rerun = True

    if rerun:
        st.experimental_rerun()

def plot_state_map():
    df = pd.read_csv(r"data\us_county_latlng.csv")
    state_lat_lng_figure = ut.build_state_lat_lng_figure(df)
    state_to_tip = plotly_events(
        state_lat_lng_figure,
        select_event= True,
    )

    if state_to_tip :
        county_index = state_to_tip[0]['pointNumber'] 
        df = ut.generate_covid_data()
        target_county = df.loc[int(county_index),'county']
        county_to_state_figure = ut.build_county_to_state_figure(
            df.loc[df['county'] == target_county]
            )
        st.plotly_chart(county_to_state_figure)
    
def main():
    plot_state_map()

if __name__ == "__main__":
    main()
    initialize_state()