import streamlit as st
import random
import pandas as pd
import base64

# 背景画像設定
def set_background(image_file):
    with open(image_file, "rb") as f:
        data_url = base64.b64encode(f.read()).decode("utf-8")
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{data_url}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# メインアプリ
def main():
    st.set_page_config(page_title="ななこさん", layout="centered")
    set_background("nanako_haikei.png")

    # ロゴ（中央配置）
    st.markdown(
        '<div style="text-align: center;">'
        '<img src="data:image/png;base64,' + get_base64("logo.png") + '" width="200">'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # セリフ画像表示（中央配置）
    st.markdown(
        '<div style="text-align: center;">'
        '<img src="data:image/png;base64,' + get_base64("serif.png") + '" width="300">'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # ランダム数字生成
    if "numbers" not in st.session_state:
        st.session_state.numbers = random.sample(range(1, 38), 7)

    numbers = st.session_state.numbers
    numbers_str = ', '.join(str(n) for n in numbers)

    st.markdown(f"<h4 style='text-align: center;'>ラッキー数字: {numbers_str}</h4>", unsafe_allow_html=True)

    # コメント（テキストファイルからランダム1行）
    with open("nanako_comment.txt", "r", encoding="utf-8") as f:
        comments = [line.strip().rstrip("。") for line in f if line.strip()]
    comment = random.choice(comments)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>{comment}</p>", unsafe_allow_html=True)

# Base64エンコード関数
def get_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

if __name__ == "__main__":
    main()
