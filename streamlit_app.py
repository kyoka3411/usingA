import streamlit as st
import pandas as pd

# 学習記録のデータを読み込む
df = pd.read_csv("learning_records.csv")

# 学習内容の登録
def register_learning_content(content):
    df = df.append({"content": content}, ignore_index=True)
    df.to_csv("learning_records.csv", index=False)

# 学習時間の登録
def register_learning_time(time):
    df.loc[df["content"] == content, "learning_time"] += time
    df.to_csv("learning_records.csv", index=False)

# 学習進捗の確認
def show_learning_progress():
    st.table(df)

# 学習記録のグラフ化
def show_learning_records_graph():
    st.line_chart(df["learning_time"])

# メイン画面
st.title("学習記録アプリ")

# メニュー
st.sidebar.title("メニュー")
st.sidebar.button("学習内容を登録", on_click=register_learning_content)
st.sidebar.button("学習時間を登録", on_click=register_learning_time)
st.sidebar.button("学習進捗を確認", on_click=show_learning_progress)
st.sidebar.button("学習記録をグラフ化", on_click=show_learning_records_graph)

# 学習内容の登録
if st.button("学習内容を登録"):
    content = st.text_input("学習内容")
    register_learning_content(content)

# 学習時間の登録
if st.button("学習時間を登録"):
    content = st.selectbox("学習内容", df["content"].tolist())
    time = st.number_input("学習時間")
    register_learning_time(time)

# 学習進捗の確認
if st.button("学習進捗を確認"):
    show_learning_progress()

# 学習記録のグラフ化
if st.button("学習記録をグラフ化"):
    show_learning_records_graph()
