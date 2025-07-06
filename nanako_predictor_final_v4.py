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
    st.markdown(
        """
        <div style='text-align:center;'>
            <img src='data:image/png;base64,{}' width='180'>
        </div>
        """.format(get_base64("logo.png")),
        unsafe_allow_html=True
    )

def display_serif():
    st.image("serif.png", use_column_width=False, width=280)

def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def display_buttons():
    st.markdown(
        """
        <div style='text-align:center;'>
            <form action="?predict" method="post">
                <button style="border:none;background:none;">
                    <img src='data:image/png;base64,{}' width='250'>
                </button>
            </form>
            <br>
            <form action="?ranking" method="post">
                <button style="border:none;background:none;">
                    <img src='data:image/png;base64,{}' width='250'>
                </button>
            </form>
        </div>
        """.format(get_base64("botann.png"), get_base64("button2.png")),
        unsafe_allow_html=True
    )

def show_prediction():
    df = pd.read_csv("data.csv")
    numbers = sorted(random.sample(range(1, 38), 7))
    st.markdown(
        f"<h3 style='text-align:center;'>ラッキー数字: {', '.join(map(str, numbers))}</h3>",
        unsafe_allow_html=True
    )
    comments = load_comments("nanako_comment.txt")
    comment = random.choice(comments).strip()
    st.markdown(f"<div style='text-align:center;'>{comment}</div>", unsafe_allow_html=True)

def main():
    set_background("nanako_haikei.png")
    st.markdown("<br>", unsafe_allow_html=True)

    display_logo()
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
    display_serif()
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    display_buttons()

    # クエリ処理によってボタンを識別
    query_params = st.experimental_get_query_params()
    if "predict" in query_params:
        show_prediction()
    elif "ranking" in query_params:
        st.subheader("出現数字ランキング（仮）")

if __name__ == "__main__":
    main()
