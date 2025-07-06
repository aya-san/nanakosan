import streamlit as st
import random
import base64

# 背景画像設定
def set_background(image_file):
    with open(image_file, "rb") as f:
        data_url = base64.b64encode(f.read()).decode("utf-8")
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{data_url}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# 画像のbase64化
def get_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# メインアプリ
def main():
    st.set_page_config(page_title="ななこさん", layout="centered")
    set_background("nanako_haikei.png")

    # ロゴ画像（中央・大きめ）
    st.markdown(
        '<div style="text-align: center;">'
        f'<img src="data:image/png;base64,{get_base64("logo.png")}" width="300">'
        '</div>',
        unsafe_allow_html=True
    )

    # セリフ画像（中央・大きめ）
    st.markdown(
        '<div style="text-align: center;">'
        f'<img src="data:image/png;base64,{get_base64("serif.png")}" width="400">'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # 占うボタン
    if st.button("ななこさんに占ってもらう"):
        # 数字をランダムに7つ選ぶ（1〜37）
        lucky_numbers = sorted(random.sample(range(1, 38), 7))
        numbers_text = ", ".join(str(n) for n in lucky_numbers)

        # 数字表示
        st.markdown(
            f"<h3 style='text-align: center;'>ラッキー数字: {numbers_text}</h3>",
            unsafe_allow_html=True
        )

        # コメント読み込み
        try:
            with open("nanako_comment.txt", "r", encoding="utf-8") as f:
                comments = [line.strip().rstrip("。") for line in f if line.strip()]
            if comments:
                comment = random.choice(comments)
                st.markdown(
                    f"<p style='text-align: center; font-size: 18px; margin-top: 20px;'>{comment}</p>",
                    unsafe_allow_html=True
                )
        except FileNotFoundError:
            st.error("コメントファイル（nanako_comment.txt）が見つかりません。")

if __name__ == "__main__":
    main()
