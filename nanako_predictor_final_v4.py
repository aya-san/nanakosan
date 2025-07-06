import streamlit as st
import random
import pandas as pd
import base64

# --- 背景画像設定 ---
def set_background(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
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

# --- コメント1つランダム表示 ---
def display_random_comment(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        comments = f.read().splitlines()
    comment = random.choice(comments)
    st.write(comment)

# --- メイン関数 ---
def main():
    set_background("haikei.jpeg")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- ロゴ中央配置 ---
    st.markdown(
        """
        <div style='text-align: center;'>
            <img src='data:image/png;base64,{}' width='200'>
        </div>
        """.format(base64.b64encode(open("logo.png", "rb").read()).decode()),
        unsafe_allow_html=True,
    )

    # --- セリフ画像 ---
    st.image("serif.png", use_container_width=True)

    # --- ボタン画像で選択肢 ---
    col1, col2 = st.columns(2)

    with col1:
        if st.markdown(
            f"""
            <a href='?page=uranai'>
                <img src='data:image/png;base64,{base64.b64encode(open("botann.png", "rb").read()).decode()}' width='250'/>
            </a>
            """,
            unsafe_allow_html=True,
        ):
            pass

    with col2:
        if st.markdown(
            f"""
            <a href='?page=ranking'>
                <img src='data:image/png;base64,{base64.b64encode(open("button2.png", "rb").read()).decode()}' width='250'/>
            </a>
            """,
            unsafe_allow_html=True,
        ):
            pass

    # --- URLクエリで分岐処理 ---
    query_params = st.experimental_get_query_params()
    if "page" in query_params:
        if query_params["page"][0] == "uranai":
            st.subheader(" ななこさんの占い ")
            display_random_comment("nanako_comment.txt")

        elif query_params["page"][0] == "ranking":
            st.subheader("出現数字ランキング")
            df = pd.read_csv("data.csv")
            all_numbers = df.iloc[:, 1:].values.flatten()
            top = pd.Series(all_numbers).value_counts().head(10)
            st.write(top.sort_values(ascending=False))

if __name__ == "__main__":
    main()
