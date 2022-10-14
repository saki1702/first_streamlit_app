import streamlit

import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My parents new healthy diner')

streamlit.header('Breakfast Menu')

streamlit.text('🥣 Omega 3 & blueberry Oatmeal')

streamlit.text('🥬 Kale, Spinach & Rocket smoothie')

streamlit.text('🐔 Hard-Boiled Free-Range Egg')

streamlit.text('🥑 Avacado Toast')

streamlit.header('🍌🍑Build your own fruit smoothie🥝🍇')

my_fruit_list= pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)

my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

# Display the table on the page.


fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)



fruityvice_response = requests.get("https://fruityvice.com/api/fruit/kiwi")
streamlit.text(fruityvice_response)

streamlit.header("Fruityvice Fruit Advice!")

#fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
#streamlit.write('The user entered ', fruit_choice)
try:
    fruit_choice = streamlit.text_input("What fruit would you like information about?")
    if not fruit_choice:
      streamlit.error('Please select a fruit to get information')
    else:
        back_from_function = get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)
        #Fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
        #fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
        #streamlit.dataframe(fruityvice_normalized)
    
#except URLError as e:
 #   streamlit.error()

#streamlit.write('The user entered ', fruit_choice)

#import requests
#Fruityvice_response = requests.get ("https://fruityvice.com/api/fruit/kiwi")

# write your own comment -Normalize the advice

# write your own comment - simple language return
#dont run anything here while we troubleshoot


    streamlit.header("The fruit load list contains:")
#snowflake-related functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT * from fruit_load_list")
        return my_cur.fetchall()
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
 
    #add a button to load the fruit


if streamlit.button('Get fruit load list');
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)

streamlit.stop()

my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")

fruit_choice = streamlit.text_input (("What fruit would you like to add?"))
streamlit.write('Thanks for adding', fruit_choice)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")

