#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 10:54:20 2022

@author: philippgunther
"""

import pandas as pd  # pip install pandas openpyxl
import plotly_express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Aufgabendashboard", page_icon=":bar_chart:", layout="wide")


df = pd.read_excel(
        io="Aufgaben.xlsx",
        engine="openpyxl",
        sheet_name="Tasks",
        usecols="A:D",
        nrows=4,
    )
st.dataframe(df)