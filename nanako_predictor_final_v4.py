import streamlit as st
import pandas as pd
import random
import base64

# --- 警告の非表示 ---
st.set_page_config(page_title="ななこさん", layout="centered")
st.markdown("""<style>.stDeployButton, .st-emotion-cache-1avcm0n, footer {visibility: hidden;}</style>""", unsafe_allow_html=True)

# --- 背景設定 ---
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

set_background("nanako_haikei.png")

# --- 画像表示 ---
st.image("logo.png", width=250)  # ロゴを小さく中央表示
st.image("serif.png", use_column_width="auto")  # セリフ画像

# --- ボタン画像の配置（上下） ---
button1 = st.image("botann.png", use_column_width="auto")
button2 = st.image("button2.png", use_column_width="auto")

# --- 抽選データの読み込みと数字予測 ---
def predict_numbers():
    df = pd.read_csv("data.csv")
    numbers = df.iloc[:, 1:].values.flatten()
    selected = random.sample(list(numbers), 7)
    selected.sort()
    return selected

# --- コメント読み込み ---
def get_random_comment():
    with open("nanako_comment.txt", "r", encoding="utf-8") as f:
        comments = [line.strip("。\n") for line in f if line.strip()]
    return random.choice(comments)

# --- メイン処理 ---
query_params = st.query_params  # ボタン判定用
if "占う" in query_params:
    lucky_numbers = predict_numbers()
    comment = get_random_comment()

    st.markdown("## ラッキー数字: " + ", ".join(str(n) for n in lucky_numbers))
    st.markdown(f"#### {comment}")

elif "ランキング" in query_params:
    df = pd.read_csv("data.csv")
    numbers = df.iloc[:, 1:].values.flatten()
    freq = pd.Series(numbers).value_counts().sort_values(ascending=False)
    st.markdown("## 出現数字ランキング（仮）")
    st.dataframe(freq.head(20))

# --- JavaScriptで画像クリックをURLパラメータ付きで再読み込み ---
st.markdown("""
    <script>
    const imgs = window.parent.document.querySelectorAll('img');
    imgs.forEach(img => {
        if (img.src.includes("botann")) {
            img.onclick = () => window.parent.location.search = "?占う";
        } else if (img.src.includes("button2")) {
            img.onclick = () => window.parent.location.search = "?ランキング";
        }
    });
    </script>
""", unsafe_allow_html=True)
