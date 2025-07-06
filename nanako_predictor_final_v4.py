import streamlit as st
import random
import base64
import pandas as pd

# 背景画像
def set_background(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded}");
            background-size: cover;
        }}
        </style>
    """, unsafe_allow_html=True)

# ロゴ表示
def show_logo():
    st.markdown(
        f"""
        <div style="text-align: center;">
            <img src="data:image/png;base64,{base64.b64encode(open("logo.png", "rb").read()).decode()}" width="300px">
        </div>
        """,
        unsafe_allow_html=True
    )

# セリフ画像表示
def show_serif():
    st.markdown(
        f"""
        <div style="text-align: center; margin-top: 10px;">
            <img src="data:image/png;base64,{base64.b64encode(open("serif.png", "rb").read()).decode()}" width="400px">
        </div>
        """,
        unsafe_allow_html=True
    )

# コメント1つだけランダム表示
def get_random_comment(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        comments = [c.strip() for c in f.read().split("。") if c.strip()]
    return random.choice(comments) + "。"

# ランダム数字生成
def generate_lucky_numbers():
    return sorted(random.sample(range(1, 38), 7))

# 頻出ランキング
def get_frequency_ranking(data_path):
    df = pd.read_csv(data_path)
    all_numbers = df.iloc[:, 1:].values.flatten()
    freq = pd.Series(all_numbers).value_counts().sort_values(ascending=False)
    return freq.head(10)

# アプリ本体
def main():
    set_background("nanako_haikei.png")  # 拡張子注意
    show_logo()
    show_serif()
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("♡ ななこさんに占ってもらう ♡", use_container_width=True):
            numbers = generate_lucky_numbers()
            st.markdown(
                f"<h3 style='text-align: center;'>🎱 ラッキー数字: {', '.join(map(str, numbers))}</h3>",
                unsafe_allow_html=True
            )
            comment = get_random_comment("nanako_comment.txt")
            st.markdown(f"<p style='text-align: center;'>{comment}</p>", unsafe_allow_html=True)

    with col2:
        if st.button("出現数字ランキング", use_container_width=True):
            ranking = get_frequency_ranking("data.csv")
            st.markdown("### 🔢 よく出る数字ランキング")
            st.dataframe(ranking.reset_index().rename(columns={"index": "数字", 0: "出現回数"}))

# 実行
if __name__ == "__main__":
    main()
