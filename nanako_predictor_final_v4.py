import streamlit as st
import pandas as pd
import random
import base64

# ページ設定（レイアウトとタイトル）
st.set_page_config(layout="centered", page_title="ななこさん")

# 背景画像を設定
def set_background(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""<style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded}");
            background-size: cover;
            background-attachment: fixed;
        }}
        </style>""",
        unsafe_allow_html=True
    )

# ロゴ表示（中央・大きめ・スマホ対応）
def show_large_logo():
    with open("logo.png", "rb") as f:
        logo_encoded = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <div style='text-align: center; padding-top: 20px;'>
            <img src='data:image/png;base64,{logo_encoded}'
                 style='width: 90%; max-width: 400px; height: auto;'>
        </div>
        """,
        unsafe_allow_html=True
    )

# セリフ画像表示
def show_serif_image():
    with open("serif.png", "rb") as f:
        serif_encoded = base64.b64encode(f.read()).decode()
    st.markdown(
        f"<div style='text-align: center;'><img src='data:image/png;base64,{serif_encoded}' style='width: 90%; max-width: 500px;'></div>",
        unsafe_allow_html=True
    )

# コメントをランダムに表示（末尾の「。」は除去）
def show_random_comment():
    with open("nanako_comment.txt", "r", encoding="utf-8") as f:
        comments = f.read().splitlines()
    comment = random.choice(comments).rstrip("。")
    st.markdown(f"<div style='text-align: center; padding: 20px;'>{comment}</div>", unsafe_allow_html=True)

# ラッキー数字をランダムに7つ
def generate_numbers():
    return sorted(random.sample(range(1, 38), 7))

# 出現数字ランキング
def show_ranking():
    df = pd.read_csv("data.csv")
    numbers = df.iloc[:, 1:].values.flatten()
    freq = pd.Series(numbers).value_counts().sort_values(ascending=False)
    st.subheader("出現数字ランキング")
    st.write(freq.head(10))

# メイン関数
def main():
    set_background("nanako_haikei.png")
    show_large_logo()
    show_serif_image()

    # セッションでクリック判定
    if "clicked" not in st.session_state:
        st.session_state.clicked = False

    # ↓ 画面下部に余白を確保しボタンを最後に表示
    st.markdown("<div style='height:50px;'></div>", unsafe_allow_html=True)

    # 中央配置されたボタン（スマホ対応）
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("♡ ななこさんに占ってもらう ♡"):
            st.session_state.clicked = True

    # ボタンクリック後の表示処理
    if st.session_state.clicked:
        numbers = generate_numbers()
        st.markdown(
            f"<div style='text-align:center; font-size: 24px; font-weight:bold; padding: 10px;'>{', '.join(map(str, numbers))}</div>",
            unsafe_allow_html=True
        )
        show_random_comment()

if __name__ == "__main__":
    main()
