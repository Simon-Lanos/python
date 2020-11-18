import os
import streamlit as st
import pandas as pd
import numpy as np

st.title("Streamlit Crash course")
st.header("Simple Header")
st.subheader("Another sub header")

st.sidebar.header("Configuration")

DATA_DIR = '\\data'
DIR = os.path.dirname(os.path.abspath(__file__))

f = []
for (dirpath, dirnames, filenames) in os.walk(DIR + DATA_DIR):
    f.extend(filenames)
    break

dataset_select = st.sidebar.selectbox("Dataset", filenames)

@st.cache
def load_data(path):
    data = pd.read_csv(path)

loading = st.text('Loading dataset ' + dataset_select)

load_data(DIR + DATA_DIR + '\\' + dataset_select)

loading.text('Done loading dataset ' + dataset_select)
