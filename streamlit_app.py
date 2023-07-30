import streamlit
import pandas

# リクエスト：https://docs.python-requests.org/en/latest/
# リクエストを使用すると、HTTP/1.1 リクエストを非常に簡単に送信できます。
# URL にクエリ文字列を手動で追加したり、POST データをフォーム エンコードしたりする必要はありません。
import requests

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# ここに選択リストを置き、スムージーに入れたい果物を選択できるようにしましょう。初期選択はアボカドとイチゴです。
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# ページにテーブルを表示します。
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")

# text input
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon/" + fruit_choice)

# streamlit.text(fruityvice_response)
# streamlit.text(fruityvice_response.json())

# normalize json data
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# create table by use normalized json data
streamlit.dataframe(fruityvice_normalized)



