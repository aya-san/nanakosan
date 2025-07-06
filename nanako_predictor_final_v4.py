import streamlit as st
import pandas as pd
import random
import base64

# --- 背景画像設定 ---
def set_background(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# --- メイン画像を中央表示 ---
def show_centered_image(image_path, width=300):
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center;">
            <img src="data:image/png;base64,{base64.b64encode(open(image_path, 'rb').read()).decode()}" width="{width}">
        </div>
        """,
        unsafe_allow_html=True
    )

# --- ボタン画像表示 ---
def image_button(image_path, key):
    button_html = f"""
        <style>
            .img-button {{
                background: none;
                border: none;
                padding: 0;
            }}
        </style>
        <button class="img-button" onclick="document.getElementById('{key}').click()">
            <img src="data:image/png;base64,{base64.b64encode(open(image_path, 'rb').read()).decode()}" width="300">
        </button>
        <input type="submit" id="{key}" style="display: none;">
    """
    return st.markdown(button_html, unsafe_allow_html=True)

# --- 数字生成 ---
def generate_lucky_numbers():
    return sorted(random.sample(range(1, 38), 7))

# --- 出現頻度ランキング ---
def show_ranking(data):
    numbers = data.iloc[:, 1:].values.flatten()
    frequency = pd.Series(numbers).value_counts().sort_values(ascending=False)
    freq_df = pd.DataFrame({
        "数字": frequency.index,
        "出現回数": frequency.values
    }).head(10)
    st.table(freq_df)

# --- アプリ本体 ---
def main():
    sset_background("nanako_haikei.png")
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ロゴ
    show_centered_image("logo.png", width=250)

    # セリフ
    show_centered_image("serif.png", width=400)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("♡ななこさんに占ってもらう♡"):
            numbers = generate_lucky_numbers()
            st.markdown(f"<h3 style='text-align:center'>今日のラッキー数字は：</h3>", unsafe_allow_html=True)
            st.markdown(f"<h1 style='text-align:center; color:hotpink'>{', '.join(map(str, numbers))}</h1>", unsafe_allow_html=True)

    with col2:
        if st.button("出現数字ランキング"):
            data = pd.read_csv("data.csv")
            st.markdown(f"<h3 style='text-align:center'>出現頻度ランキング</h3>", unsafe_allow_html=True)
            show_ranking(data)

    # コメント表示（任意）
    with open("nanako_comment.txt", encoding="utf-8") as f:
        comment = f.read()
    st.markdown(f"<div style='text-align:center; margin-top:40px;'>{comment}</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
