# -*- coding: utf-8 -*-
import duckdb
import streamlit as st
from PIL import Image

# main App layout

st.header("Premier League Stats")
image = Image.open("img/pl_logo2.png")
st.image(image, use_column_width=True)
st.markdown("### Standings")

st.markdown("---")

pl_duck = duckdb.connect("data/pl.duck.db")

data = """
        SELECT
            pos,
            team_name as Team,
            matches as Matches,
            wins as Wins,
            draws as Draws,
            losses as Losses,
            favor_goals as FG,
            against_goals as AG,
            difference as SG,
            points as Points
        FROM pl_standings_2023_2024
    """

objects = pl_duck.execute(query=data).df().set_index("pos")

st.table(objects)

st.markdown("---")
