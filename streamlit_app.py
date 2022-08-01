
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title("My parents new healthy diner")
streamlit.header("Main Menu")
streamlit.text("🥣 Omega 3 cereal")
streamlit.text("🥬 kale smoothie")
streamlit.text("🥗 salad")

my_fruit_salad = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_salad = my_fruit_salad.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruit:", list(my_fruit_salad.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_salad.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

def get_fruityvice_data(fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  # normalize
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
    
try:
  streamlit.header("Fruityvice Fruit Advice!")

  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
  else:
    fruityvice_response = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(fruityvice_response)
except URLError as e:
  streamlit.error()
  
streamlit.header("The fruit load list contains:")

def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
    return my_cur.fetchall()
  
if streamlit.button('Get Fruit Load List!'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe(my_data_rows)
  
streamlit.stop()

def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("INSERT INTO FRUIT_LOAD_LIST VALUES ('from streamlit')")
    return 'Thanks for adding ' + new_fruit
  
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a fruit to the list):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_fruit = insert_row_snowflake(add_my_fruit)
  streamlit.write(my_fruit)
