import streamlit as st
import pandas as pd
import random
import base64

# ページ設定（1回だけ）
st.set_page_config(layout="centered")

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

# ロゴ表示（少し小さく、中央、スマホ対応）
def show_large_logo():
    with open("logo.png", "rb") as f:
        logo_encoded = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <div style='text-align: center; padding-top: 20px;'>
            <img src='data:image/png;base64,{logo_encoded}'
                 style='width: 70%; max-width: 280px; height: auto;'>
        </div>
        """,
        unsafe_allow_html=True
    )

# セリフ画像表示（大きめ、中央）
def show_serif_image():
    st.markdown("<div style='text-align: center;'><img src='data:image/png;base64," +
                base64.b64encode(open("serif.png", "rb").read()).decode() +
                "' style='width: 90%; max-width: 500px;'></div>", unsafe_allow_html=True)

# コメントをランダム表示
def show_random_comment():
    with open("nanako_comment.txt", "r", encoding="utf-8") as f:
        comments = f.read().splitlines()
    
    # ランダムに1つ選び、末尾の「。」があれば削除
    comment = random.choice(comments).rstrip("。")
    
    st.markdown(
        f"<div style='text-align: center; padding: 20px;'>{comment}</div>",
        unsafe_allow_html=True
    )

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
    set_background("nanako_haikei.png")
    show_large_logo()
    show_serif_image()

    if show_uranai_button():
        numbers = generate_numbers()
        st.markdown(
            f"<div style='text-align:center; font-size: 22px;'>{', '.join(map(str, numbers))}</div>",
            unsafe_allow_html=True
        )
        show_random_comment()

   # 中央寄せの大きな占いボタン（スマホ対応）
def show_uranai_button():
    button_html = """
        <div style="text-align: center; padding: 30px;">
            <button onclick="document.getElementById('click-button').click();"
                style="
                    background-color: #ffccdd;
                    color: black;
                    font-size: 20px;
                    padding: 15px 30px;
                    border: none;
                    border-radius: 10px;
                    cursor: pointer;
                    box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
                ">
                ♡ ななこさんに占ってもらう ♡
            </button>
        </div>
    """
    st.markdown(button_html, unsafe_allow_html=True)
    return st.button("", key="click-button")

if __name__ == "__main__":
    main()
