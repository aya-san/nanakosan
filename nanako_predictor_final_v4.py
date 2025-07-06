import streamlit as st
import pandas as pd
import random
import base64

def set_background(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def load_comments(txt_path):
    with open(txt_path, encoding="utf-8") as f:
        comments = f.read().split("。")
    return [c for c in comments if c.strip()]

def display_logo():
    st.image("logo.png", use_column_width=False, width=300)

def display_serif():
    st.image("serif.png", use_column_width=False, width=300)

def display_buttons():
    col1, col2 = st.columns(2)
    with col1:
        clicked = st.button("♡ななこさんに占ってもらう♡", key="uranai", help="画像ボタンに差し替え予定")
        if clicked:
            show_prediction()
    with col2:
        clicked2 = st.button("出現数字ランキング", key="ranking", help="画像ボタンに差し替え予定（仮）")
        if clicked2:
            st.subheader("出現数字ランキング（仮）")  # 仮の機能

def show_prediction():
    df = pd.read_csv("data.csv")
    numbers = sorted(random.sample(range(1, 38), 7))
    st.markdown(
        f"<h3 style='text-align:center;'>🎱 ラッキー数字: {', '.join(map(str, numbers))}</h3>",
        unsafe_allow_html=True
    )
    comments = load_comments("nanako_comment.txt")
    comment = random.choice(comments)
    st.write(f"**{comment.strip()}**")

def main():
    set_background("nanako_haikei.png")
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
    display_logo()
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
    display_serif()
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    display_buttons()

if __name__ == "__main__":
    main()
