import streamlit as st
import pandas as pd
import random
import base64

# 背景画像を設定する関数
def set_background(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    page_bg_img = f"""
    <style>
    [data-testid="stApp"] {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: top left;
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# ランダムコメントを読み込む関数
def load_random_comment(file_path):
    with open(file_path, encoding="utf-8") as f:
        comments = [line.strip() for line in f if line.strip()]
    return random.choice(comments)

# 占いページ
def show_fortune():
    st.image("logo.png", width=300)
    st.markdown("<h3 style='text-align: center;'>迷っているのね<br>アタクシが数字を選んでさしあげましょう</h3>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    comment = load_random_comment("nanako_comment.txt")
    st.markdown(f"<div style='text-align:center; font-size:18px;'>{comment}</div>", unsafe_allow_html=True)

# ランキングページ
def show_ranking():
    df = pd.read_csv("data.csv")
    numbers = df.iloc[:, 1:].values.flatten()
    counts = pd.Series(numbers).value_counts().sort_values(ascending=False)
    ranking_df = counts.reset_index()
    ranking_df.columns = ['数字', '出現回数']
    st.markdown("<h3 style='text-align: center;'>出現数字ランキング</h3>", unsafe_allow_html=True)
    st.table(ranking_df)

# メイン
def main():
    set_background("nanako_haikei.png")
    st.image("logo.png", width=300)
    st.markdown("<h3 style='text-align: center;'>迷っているのね<br>アタクシが数字を選んでさしあげましょう</h3>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.image("botann.png", use_column_width=True):
            st.session_state.page = "fortune"
    with col2:
        if st.image("button2.png", use_column_width=True):
            st.session_state.page = "ranking"

    if "page" in st.session_state:
        if st.session_state.page == "fortune":
            show_fortune()
        elif st.session_state.page == "ranking":
            show_ranking()

if __name__ == "__main__":
    main()
