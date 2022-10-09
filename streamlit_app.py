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

streamlit.dataframe(my_fruit_list)

my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

# Display the table on the page.


fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)


import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

streamlit.header("Fruityvice Fruit Advice!")

import requests
Fruityvice_response = requests.get ("https://fruityvice.com/api/fruit/kiwi")


# write your own comment -Normalize the advice
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - simple language return
streamlit.dataframe(fruityvice_normalized)






