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

    # ボタンを中央に表示（スマホでもクリック可能な方式）
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    if st.button("♡ ななこさんに占ってもらう ♡"):
        numbers = generate_numbers()
        st.markdown(
            f"<div style='text-align:center; font-size: 22px;'>{', '.join(map(str, numbers))}</div>",
            unsafe_allow_html=True
        )
        show_random_comment()
    st.markdown("</div>", unsafe_allow_html=True)

    # ↓ 画面下部に余白を確保しボタンを最後に表示
    st.markdown("<div style='height:50px;'></div>", unsafe_allow_html=True)

    # ボタン画像クリックで占い
col1, col2 = st.columns(2)
with col1:
    if st.button("♡ ななこさんに占ってもらう ♡", key="uranai"):
        numbers = sorted(random.sample(range(1, 38), 7))
        comment = get_random_comment("nanako_comment.txt")
        st.markdown(f"<h3 style='text-align:center;'>{'・'.join(map(str, numbers))}</h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align:center; font-size:22px;'>{comment}</p>", unsafe_allow_html=True)

with col2:
    if st.button("出現数字ランキング", key="ranking"):
        freq = calc_number_frequency("data.csv")
        st.markdown("### 出現ランキング")
        for num, count in freq.items():
            st.write(f"{int(num):2d} → {count}回")
        show_random_comment()

if __name__ == "__main__":
    main()
