import streamlit

streamlit.title('My parents new healthy diner')

streamlit.header('Breakfast Menu')

streamlit.text('🥣 Omega 3 & blueberry Oatmeal')

streamlit.text('🥬 Kale, Spinach & Rocket smoothie')


streamlit.text('🐔 Hard-Boiled Free-Range Egg')

streamlit.text('🥑 Avacado Toast')

streamlit.header('🍌🍑Build your own fruit smoothie🥝🍇')


import pandas

my_fruit_list= pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
