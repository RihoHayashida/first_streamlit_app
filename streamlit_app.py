import streamlit
import pandas

# fruityviceからJSONデータを取得して使用
# リクエスト：https://docs.python-requests.org/en/latest/
# リクエストを使用すると、HTTP/1.1 リクエストを非常に簡単に送信できます。
# URL にクエリ文字列を手動で追加したり、POST データをフォーム エンコードしたりする必要はありません。
import requests

# connect to snowflake
# requirements.txtファイルは、プロジェクトで使用する予定のライブラリをStreamlitに伝え、事前にライブラリを追加できるようにします。
# 以下に示す行は、プロジェクトに追加したライブラリを使用するように py ファイルに指示します。 
import snowflake.connector

from urllib.error import URLError

#############################################################################################################################

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#############################################################################################################################

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#############################################################################################################################

# ここに選択リストを置き、スムージーに入れたい果物を選択できるようにしましょう。初期選択はアボカドとイチゴです。
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# ページにテーブルを表示します。
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")

try:
  # テキスト入力
  # fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit")
  else:
    # fruityviceからJSONデータを取得して使用
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    # jsonデータを正規化
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    # 正規化されたjsonデータでテーブルを作成
    streamlit.dataframe(fruityvice_normalized)
    # テキスト表示
    streamlit.write('The user entered ', fruit_choice)
except URLError as e:
  streamlit.error()

# streamlit.text(fruityvice_response)
# streamlit.text(fruityvice_response.json())

#############################################################################################################################

# connect to snowflake

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("select * from fruit_load_list")

# my_data_rows = my_cur.fetchone()
my_data_rows = my_cur.fetchall()

# streamlit.text("Hello from Snowflake:")
streamlit.header("The fruit load list contains: ")

# streamlit.text(my_data_row)
streamlit.dataframe(my_data_rows)

# テキスト入力
add_my_fruit = streamlit.text_input('What fruit would you like add?', "kiwi")
# my_cur.execute("select * from fruit_load_list")
streamlit.write("thanks for adding", add_my_fruit)

streamlit.stop()

# if add_my_fruit != "":
my_cur.execute("insert into fruit_load_list values ('" + add_my_fruit + "')")

#############################################################################################################################

