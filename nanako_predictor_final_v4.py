
import streamlit as st
import pandas as pd
import random
import base64

# 背景画像を設定
def set_background(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""<style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded}");
            background-size: cover;
        }}
        </style>""",
        unsafe_allow_html=True
    )

# ロゴ表示
def show_logo():
    st.markdown("<div style='text-align: center;'><img src='data:image/png;base64," + 
                base64.b64encode(open("logo.png", "rb").read()).decode() + 
                "' style='width: 40%;'></div>", unsafe_allow_html=True)

# セリフ画像表示
def show_serif_image():
    st.markdown("<div style='text-align: center;'><img src='data:image/png;base64," + 
                base64.b64encode(open("serif.png", "rb").read()).decode() + 
                "' style='width: 60%;'></div>", unsafe_allow_html=True)

# コメントをランダム表示
def show_random_comment():
    with open("nanako_comment.txt", "r", encoding="utf-8") as f:
        comments = f.read().splitlines()
    comment = random.choice(comments)
    st.markdown(f"<div style='text-align: center; padding: 20px;'>{comment}</div>", unsafe_allow_html=True)

# 数字をランダムに7つ表示
def generate_numbers():
    return sorted(random.sample(range(1, 38), 7))

# 数字ランキング表示
def show_ranking():
    df = pd.read_csv("data.csv")
    numbers = df.iloc[:, 1:].values.flatten()
    freq = pd.Series(numbers).value_counts().sort_values(ascending=False)
    st.subheader("出現数字ランキング")
    st.write(freq.head(10))

# メイン関数
def main():
    set_background("haikei.jpeg")
    show_logo()
    show_serif_image()

    col1, col2 = st.columns(2)
    with col1:
        if st.button("♡ ななこさんに占ってもらう ♡"):
            numbers = generate_numbers()
            st.markdown(f"<h3 style='text-align: center;'>ラッキーナンバー：{', '.join(map(str, numbers))}</h3>", unsafe_allow_html=True)
            show_random_comment()
    with col2:
        if st.button("出現数字ランキング"):
            show_ranking()

if __name__ == "__main__":
    main()
