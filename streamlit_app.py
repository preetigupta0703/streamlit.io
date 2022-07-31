
import streamlit
import pandas
import requests


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

streamlit.header("Fruityvice Fruit Advice!")

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

# normalize
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
