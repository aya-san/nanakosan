
import streamlit as st
import pandas as pd
import random
import base64

# 背景画像とロゴを表示する関数
def set_background(image_path):
    with open(image_path, "rb") as img_file:
        b64_image = base64.b64encode(img_file.read()).decode()
        bg_style = f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{b64_image}");
            background-size: cover;
            background-position: center;
        }}
        </style>
        """
        st.markdown(bg_style, unsafe_allow_html=True)

def center_logo(image_path):
    st.markdown(
        f"""
        <div style="text-align:center;">
            <img src="data:image/png;base64,{base64.b64encode(open(image_path, "rb").read()).decode()}" width="300"/>
        </div>
        """,
        unsafe_allow_html=True
    )

# 背景とロゴ
set_background("nanako_haikei.jpeg")
center_logo("nanako_logo.png")

# フォントをレトロ風にカスタム（Google Fontsなどを読み込む例）
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Kiwi+Maru&display=swap');

html, body, [class*="css"]  {
    font-family: 'Kiwi Maru', serif;
}
</style>
""", unsafe_allow_html=True)

# タイトル＆説明
st.markdown("<h2 style='text-align: center;'>迷っているのね</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>ワタクシが数字を選んでさしあげましょう</h4>", unsafe_allow_html=True)

# CSVの読み込み（ファイル名は適宜修正）
df = pd.read_csv("___________.csv")

# 数値の列（7つの当選数字）だけを取得（1列目は日付と仮定）
numbers = df.iloc[:, 1:].values.flatten()
numbers = pd.Series(numbers).dropna().astype(int)

# 出現回数をカウント
counts = numbers.value_counts().sort_index()

# ランダム予想生成（重み付き）
def weighted_sample(counts, k=7):
    return sorted(random.choices(
        population=counts.index.tolist(),
        weights=counts.values.tolist(),
        k=k
    ))

# コメント読み込み
with open("nanako_comment.txt", encoding="utf-8") as f:
    comments = [line.strip() for line in f if line.strip()]

# 予想を表示
if st.button("♡ ななこさんに占ってもらう ♡"):
    st.markdown("### 💡 ナナコさんのひとこと")
    st.markdown(f"**「{random.choice(comments)}」**")

    for i in range(3):
        nums = weighted_sample(counts)
        st.markdown(f"#### ✨ 提案 {i+1}: {'・'.join(map(str, nums))}")

# 出現数ランキングボタン
if st.button("出現数字ランキング"):
    st.markdown("### 出現数ランキング")
    st.bar_chart(counts)
