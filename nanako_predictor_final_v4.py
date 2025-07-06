import streamlit as st
import random
import base64

# 背景画像の設定
def set_background(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
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

# 数字をランダムに7つ生成
def generate_numbers():
    return sorted(random.sample(range(1, 38), 7))

# コメントをランダムに取得
def get_random_comment(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        comments = [line.strip() for line in f if line.strip()]
    return random.choice(comments)

# メイン画面
def main():
    set_background("haikei.png")

    st.markdown("<br>", unsafe_allow_html=True)

    # ロゴ中央配置（大きめ）
    st.markdown(
        """
        <div style="text-align:center;">
            <img src="data:image/png;base64,%s" width="300">
        </div>
        """ % base64.b64encode(open("logo.png", "rb").read()).decode(),
        unsafe_allow_html=True
    )

    # セリフ（小さめフォント）
    st.markdown(
        """
        <div style='text-align: center; font-size: 16px; margin-top: 10px;'>
            <p>迷っているのね</p>
            <p><strong>アタクシが数字を選んでさしあげましょう</strong></p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<hr>", unsafe_allow_html=True)

    # 占ってもらうボタン（画像ボタン）
    if st.button("♡ ななこさんに占ってもらう ♡"):
        numbers = generate_numbers()
        comment = get_random_comment("nanako_comment.txt")
        st.markdown(
            f"<div style='text-align: center; font-size: 24px; color: #d63384;'>{numbers}</div>",
            unsafe_allow_html=True
        )
        st.markdown(f"<p style='text-align:center; margin-top:20px;'>{comment}</p>", unsafe_allow_html=True)

    # 出現ランキングボタン（画像ボタン）
    if st.button("出現数字ランキング"):
        st.markdown("<h3 style='text-align: center;'>出現数字ランキング</h3>", unsafe_allow_html=True)
        st.markdown("（ランキング機能は別途追加可能です）")

if __name__ == "__main__":
    main()
