import streamlit as st
import pandas as pd
import utils as ut


# df = pd.read_csv(r"data\us_county_latlng.csv")

# st.map(data = df)

def main():
    # st.session_state.df = ut.generate_data()
    # df_json = ut.aggrid_interactive_table(
    #     df = st.session_state.df
    #     )

    col1_1, col1_2 = st.columns(2)
    states_list, county_list = ut.generate_states_county()
    with col1_1:
        target_states = st.selectbox("Select Your State", states_list)

    with col1_2:
        target_county = st.selectbox("Select Your County", county_list)

if __name__ == "__main__":
    main()