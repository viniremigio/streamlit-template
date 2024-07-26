# -*- coding: utf-8 -*-
from PIL import Image
import pandas as pd
import streamlit as st
import duckdb


# main App layout

st.header("Premier League Stats")
image = Image.open('img/pl_logo2.png')
st.image(image, use_column_width=True)
st.markdown("### Standings")

st.markdown("---")

pl_duck = duckdb.connect('data/pl.duck.db')

objects = (pl_duck
           .execute(query="SELECT pos, team_name, matches, wins, draws, losses, favor_goals, against_goals, difference, points FROM pl_standings_2023_2024")
           .df()
           .set_index("pos"))

st.table(objects)

st.markdown("---")