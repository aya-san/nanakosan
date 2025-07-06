import streamlit as st
import pandas as pd
import random
import base64

# --- 背景画像をセットする関数 ---
def set_background(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# --- ななこコメントをランダムに1つだけ表示 ---
def get_random_comment(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    comments = [c.strip() for c in text.split("。") if c.strip()]
    return random.choice(comments)

# --- ラッキー数字の生成関数 ---
def generate_numbers():
    return sorted(random.sample(range(1, 38), 7))

# --- メイン処理 ---
def main():
    set_background("nanako_haikei.png")

    st.markdown("<br>", unsafe_allow_html=True)

    # ロゴ画像
    st.image("logo.png", use_column_width=False, width=300)

    # セリフ画像
    st.image("serif.png", use_column_width=False, width=400)

    st.markdown("<br>", unsafe_allow_html=True)

    # ボタン画像を表示（上下に配置）
    col1, _ = st.columns([1, 1])
    with col1:
        if st.image("botann.png", use_column_width=False):
            # 占うボタンが押されたら
            numbers = generate_numbers()
            comment = get_random_comment("nanako_comment.txt")

            st.markdown("### 🎱 ラッキー数字: " + ", ".join(map(str, numbers)))
            st.markdown(f"#### {comment}")

    st.markdown("<br>", unsafe_allow_html=True)

    col2, _ = st.columns([1, 1])
    with col2:
        if st.image("button2.png", use_column_width=False):
            # 出現頻度ランキング表示用処理（別途追加）
            st.markdown("### 出現数字ランキング（仮）")
            # データ処理が必要ならここで呼び出す

if __name__ == "__main__":
    main()
