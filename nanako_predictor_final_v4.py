import streamlit as st
import pandas as pd
import random
import base64

# 背景画像設定
def set_background(image_file):
    with open(image_file, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{data}");
            background-size: cover;
        }}
        </style>
    """, unsafe_allow_html=True)

# ロゴ画像表示
def show_logo(image_file):
    st.image(image_file, use_column_width=True)

# ボタン画像でクリックを実装
def custom_button(image_path, key):
    with open(image_path, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    button_html = f"""
        <div style="text-align:center;">
            <img src="data:image/png;base64,{data}" style="cursor:pointer;" onclick="document.getElementById('{key}').click()">
        </div>
        <input type="submit" id="{key}" style="display:none;">
    """
    return st.markdown(button_html, unsafe_allow_html=True)

# ランダムコメント取得
def get_random_comment(file_path):
    with open(file_path, encoding='utf-8') as f:
        comments = f.readlines()
    return random.choice(comments).strip()

# 出現回数ランキングを計算
def calc_number_frequency(csv_path):
    df = pd.read_csv(csv_path)
    numbers = pd.Series(df.drop(columns=['日付'], errors='ignore').values.ravel())
    numbers = numbers[pd.to_numeric(numbers, errors='coerce').notnull()].astype(int)
    return numbers.value_counts().sort_values(ascending=False)

# 画面開始
set_background("haikei.jpeg")
show_logo("logo.png")

# タイトルとメッセージ
st.markdown("<h2 style='text-align:center;'>迷っているのね<br>ワタクシが数字を選んでさしあげましょう</h2>", unsafe_allow_html=True)

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
