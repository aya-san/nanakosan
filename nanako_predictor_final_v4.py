import streamlit as st
import random
from PIL import Image
import base64
import pandas as pd

# --- 背景画像の設定 ---
def set_background(image_file):
    with open(image_file, "rb") as f:
        base64_image = base64.b64encode(f.read()).decode()
    bg_style = f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{base64_image}");
            background-size: cover;
        }}
        </style>
    """
    st.markdown(bg_style, unsafe_allow_html=True)

# --- ロゴ画像の表示（中央・サイズ調整） ---
def show_logo():
    st.markdown(
        """
        <div style="text-align: center;">
            <img src="data:image/png;base64,{}" width="200">
        </div>
        """.format(get_base64("logo.png")),
        unsafe_allow_html=True
    )

# --- セリフ画像の表示（中央） ---
def show_serif():
    st.markdown(
        """
        <div style="text-align: center; margin-top: -40px;">
            <img src="data:image/png;base64,{}" width="300">
        </div>
        """.format(get_base64("serif.png")),
        unsafe_allow_html=True
    )

# --- base64変換 ---
def get_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# --- ラッキー数字の表示 ---
def show_lucky_numbers():
    data = pd.read_csv("data.csv")
    numbers = []
    for col in data.columns[1:8]:  # 数字1〜数字7
        numbers.extend(data[col].tolist())
    lucky = sorted(random.sample(set(numbers), 7))
    st.markdown(
        f"""
        <div style="text-align: center; font-size: 28px; font-weight: bold; margin-top: 20px;">
            ラッキー数字: {', '.join(map(str, lucky))}
        </div>
        """,
        unsafe_allow_html=True
    )

# --- コメント表示 ---
def show_random_comment():
    with open("nanako_comment.txt", "r", encoding="utf-8") as f:
        comments = [line.strip() for line in f if line.strip()]
    comment = random.choice(comments)
    st.markdown(
        f"""
        <div style="text-align: center; font-size: 18px; margin-top: 20px;">
            {comment}
        </div>
        """,
        unsafe_allow_html=True
    )

# --- メイン関数 ---
def main():
    st.set_page_config(page_title="ななこさん", layout="centered")
    set_background("haikei.jpeg")

    show_logo()
    show_serif()
    show_lucky_numbers()
    show_random_comment()

# --- 実行 ---
if __name__ == "__main__":
    main()
