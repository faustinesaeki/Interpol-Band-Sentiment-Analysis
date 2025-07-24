import streamlit as st
import pandas as pd
import plotly.express as px
import json

from visuals_markdown import markdown

def draw_covers(df):
    cols = st.columns(len(df["Album Name"].unique()))
    for idx, album in enumerate(df["Album Name"].unique()):
        with cols[idx]:
            st.image(df[df["Album Name"] == album]["Album Cover"].iloc[0],
                width=50)
    st.markdown("""
    <style>
        [data-testid="stHorizontalBlock"] {
            overflow-x: auto !important;
            flex-wrap: nowrap !important;
        }
    </style>
    """, unsafe_allow_html=True)


st.set_page_config(page_title="Interpol Sentiment Analysis", page_icon= "💽", layout='wide')
st.markdown(markdown, unsafe_allow_html=True)

file_name= "interpol_complete"

@st.cache_data
def load_data():
    with open(f'data/{file_name}.json') as f:
        return pd.DataFrame(json.load(f))

df = load_data()


st.title("Interpol Songs Sentiment Analysis")
st.subheader("(Анализ эмоций песен группы Interpol)")


st.image('assets/1.png')
st.markdown('---')


st.title("Мрачность (Gloom Score)")

fig = px.scatter(df, x="Album Name", y='Gloom',
    hover_data={"Track Name": True}, color="Album Name",
    width=800, height=600,
    color_discrete_sequence=px.colors.qualitative.Dark2_r)

#наведение на элемент
fig.update_traces(
    hovertemplate="<b>%{customdata[0]}</b><br>" +  #жирным шрифтом название трека
                 f"Gloom: <b>%{{y:.2f}}</b>" + 
                 "<extra></extra>"  #убираем лишнюю инфу
)

fig.update_layout(showlegend = False, plot_bgcolor='rgba(0,0,0,1)',
    paper_bgcolor='rgba(0,0,0,1)')

st.plotly_chart(fig, use_container_width=True)
draw_covers(df)

st.markdown('---')

st.subheader("Данные в таблице (Data):")
st.dataframe(df[['Album Name', 'Track Name', 'Gloom']].sort_values('Gloom', ascending=False))

st.markdown('---')

st.title("По эмоциям (sadness, anger, fear, joy, love, surprise)")

emotions = ["sadness", "anger", "fear", "joy", "love", "surprise"]

emotion = st.selectbox("Выберите эмоцию (Pick an emotion): ", emotions, index=0)

#график
fig1 = px.scatter(
    df, x="Album Name", y=emotion,
    hover_data={"Track Name": True, "Album Cover": True},
    color="Album Name", width=800, height=600,
    color_discrete_sequence=px.colors.qualitative.Dark2_r)

#наведение на элемент
fig1.update_traces(
    hovertemplate="<b>%{customdata[0]}</b><br>" +  #жирным шрифтом название трека
                 f"{emotion}: <b>%{{y:.2f}}</b>" + 
                 "<extra></extra>"  #убираем лишнюю инфу
)

fig1.update_layout(showlegend = False, plot_bgcolor='rgba(0,0,0,1)', paper_bgcolor='rgba(0,0,0,1)')

st.plotly_chart(fig1, use_container_width=True)
draw_covers(df)


st.markdown('---')
st.subheader("Данные в таблице по эмоциям (Data by emotions):")
st.dataframe(df[['Album Name', 'Track Name', emotion]].sort_values(emotion, ascending=False))