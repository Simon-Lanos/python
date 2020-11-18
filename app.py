import os
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Petite app Streamlit de data visualisation")
st.header("Voyons ce que ce framework à dans le ventre")
st.subheader("Chargez-moi ce dataset !")

st.sidebar.header("Configuration")

DATA_DIR = '\\data'
DIR = os.path.dirname(os.path.abspath(__file__))

f = []
for (dirpath, dirnames, filenames) in os.walk(DIR + DATA_DIR):
    f.extend(filenames)
    break

dataset_select = st.sidebar.selectbox("Dataset", filenames)
nrows = st.sidebar.slider("Combiens de ligne à charger ?", 0, 10000)

@st.cache
def load_data(path):
    data = pd.read_csv(path, nrows=nrows)
    #data['Date'] = pd.to_datetime(data['Date'])
    data.dropna()
    return data

loading = st.text('Chargement en cours de ' + dataset_select)

data = load_data(DIR + DATA_DIR + '\\' + dataset_select)

loading.text('Chargement terminé de ' + dataset_select)

st.write(data)

st.text('Quelle colonne avons nous ?')
st.write(data.columns)

st.text('Quelle type de colonne avons nous ?')
st.write(data.dtypes)

st.text('A quoi resemble notre dataset ?')
st.write(data.shape)
st.write(data.describe())

st.text('On affiche une petite heatmap de correlation')

st.write(sns.heatmap(data.corr(), annot=True))
st.pyplot()
