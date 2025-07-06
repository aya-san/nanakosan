import streamlit as st
import random
import base64
import pandas as pd

# 背景画像を設定
def set_background(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
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

# ロゴを中央に表示
def show_logo():
    st.markdown(
        """
        <div style="text-align: center;">
            <img src="data:image/png;base64,{}" style="width: 300px;" />
        </div>
        """.format(base64.b64encode(open("logo.png", "rb").read()).decode()),
        unsafe_allow_html=True
    )

# セリフ画像を表示
def show_serif():
    st.markdown(
        """
        <div style="text-align: center; margin-top: 10px;">
            <img src="data:image/png;base64,{}" style="width: 400px;" />
        </div>
        """.format(base64.b64encode(open("serif.png", "rb").read()).decode()),
        unsafe_allow_html=True
    )

# ランダムコメントを取得
def get_random_comment(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        comments = f.read().split("。")
    return random.choice([c for c in comments if c.strip()]) + "。"

# 数字をランダムに7つ選ぶ
def generate_lucky_numbers():
    return sorted(random.sample(range(1, 38), 7))

# 出現頻度ランキング
def get_frequency_ranking(data_path):
    df = pd.read_csv(data_path)
    all_numbers = df.iloc[:, 1:].values.flatten()
    freq = pd.Series(all_numbers).value_counts().sort_values(ascending=False)
    return freq.head(10)

# メインアプリ
def main():
    set_background("nanako_haikei.jpeg")  # または .png に変更してもOK

    show_logo()
    show_serif()

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("♡ ななこさんに占ってもらう ♡", use_container_width=True):
            numbers = generate_lucky_numbers()
            st.markdown(f"<h3 style='text-align: center;'>🎱 ラッキー数字: {', '.join(map(str, numbers))}</h3>", unsafe_allow_html=True)
            st.markdown(f"<p style='text-align: center;'>{get_random_comment('nanako_comment.txt')}</p>", unsafe_allow_html=True)

    with col2:
        if st.button("出現数字ランキング", use_container_width=True):
            ranking = get_frequency_ranking("data.csv")
            st.markdown("### 🔢 よく出る数字ランキング")
            st.dataframe(ranking.reset_index().rename(columns={"index": "数字", 0: "出現回数"}))

# 実行
if __name__ == "__main__":
    main()
