 # リクエスト：https://docs.python-requests.org/en/latest/
# リクエストを使用すると、HTTP/1.1 リクエストを非常に簡単に送信できます。
# URL にクエリ文字列を手動で追加したり、POST データをフォーム エンコードしたりする必要はありません。
import reqests
Fruityvice_response =requests.get("https://fruityvice.com/api/fruit/watermelon") 
streamlit.header("Fruityvice Fruit Advice!")
streamlit.text(fruityvice_response)
streamlit.text(fruityvice_response.jspn())

import streamlit
import pandas
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
