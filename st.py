import streamlit as st
import pandas as pd
import utils as ut
from streamlit_plotly_events import plotly_events



def main():
    df = pd.read_csv(r"data\us_county_latlng.csv")
    state_lat_lng_figure = ut.build_state_lat_lng_figure(df)
    state_to_tip = plotly_events(
        state_lat_lng_figure,
        click_event = True,
        hover_event= True,
        select_event= True,
    ) 
    county_index_list = state_to_tip[0]['pointNumber']
    
    target_county = df.loc[int(county_index_list),'name']

    st.session_state.df = ut.generate_covid_data()

    # col1_1, col1_2 = st.columns(2)
    # states_list, county_list = ut.generate_states_county()
    # with col1_1:
    #     target_states = st.selectbox("Select Your State", states_list)

    # with col1_2:
    #     target_county = st.selectbox("Select Your County", county_list)
    if target_county is not None:
        county_to_state_figure = ut.build_county_to_state_figure(
            st.session_state.df.loc[st.session_state.df['county'] == target_county]
            )
        st.plotly_chart(county_to_state_figure)

if __name__ == "__main__":
    main()