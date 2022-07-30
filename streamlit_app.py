
import streamlit
import pandas

streamlit.title("My parents new healthy diner")
streamlit.header("Main Menu")
streamlit.text("🥣 Omega 3 cereal")
streamlit.text("🥬 kale smoothie")
streamlit.text("🥗 salad")

my_fruit_salad = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_salad = my_fruit_salad.set_index('Fruit')
streamlit.multiselect("Pick some fruit:", list(my_fruit_salad.index)['Avacado','Strawberries'])
streamlit.dataframe(my_fruit_salad)
