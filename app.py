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

st.subheader("Graph dynamique")

columns_names = data.columns.tolist()
type_of_graph = st.selectbox("Choisir un type", ["area", "bar", "line", "hist", "box", "kde"])
selected_columns_names = st.multiselect("Choisir une/des colonne(s)", columns_names)

if st.button("Générer le graphique"):
    st.success("Génération de graph personalisé de type {} pour {}".format(type_of_graph, selected_columns_names))

    if type_of_graph == 'area':
        sub_data = data[selected_columns_names]
        st.area_chart(sub_data)

    elif type_of_graph == 'bar':
        sub_data = data[selected_columns_names]
        st.bar_chart(sub_data)

    elif type_of_graph == 'line':
        sub_data = data[selected_columns_names]
        st.line_chart(sub_data)

    # Custom Plot 
    elif type_of_graph:
        cust_graph = data[selected_columns_names].plot(kind=type_of_graph)
        st.write(cust_graph)
        st.pyplot()
