
import streamlit as st
import random
from collections import Counter
import pandas as pd

# 🌸 ページ設定
st.set_page_config(page_title="ナナコさんのロト7予想", layout="centered")

# 🌈 カスタムCSS（背景・フォント・ボタン）
st.markdown("""
    <style>
    body {
        background: linear-gradient(to bottom, #f7fdf2, #ffeef2, #f9e1ef, #eee9f9);
        color: #800080;
        font-family: 'Hiragino Maru Gothic Pro', 'Yu Gothic', sans-serif;
    }
    .stButton>button {
        background-color: #c586c0;
        color: white;
        padding: 0.6em 2em;
        font-size: 18px;
        border-radius: 20px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #a460a3;
        color: white;
    }
    .main-title {
        font-size: 48px;
        text-align: center;
        font-weight: bold;
        margin-bottom: -10px;
    }
    .sub-title {
        font-size: 20px;
        text-align: center;
        color: #b030b0;
        margin-bottom: 40px;
    }
    .number-output {
        text-align: center;
        font-size: 32px;
        color: #800080;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# 🌸 タイトル＆サブ
st.markdown('<div class="main-title">ナナコさん</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">♡アタシが７つの数字を予想するわ♡</div>', unsafe_allow_html=True)

# 🎲 出現履歴データ（仮の20回分）
history_numbers = [
    [2, 9, 11, 18, 21, 30, 35],
    [3, 4, 5, 14, 19, 23, 36],
    [1, 7, 12, 18, 24, 29, 33],
    [6, 8, 13, 15, 22, 31, 37],
    [2, 5, 9, 16, 21, 26, 34],
    [1, 3, 10, 17, 25, 28, 32],
    [4, 6, 11, 20, 27, 30, 35],
    [7, 8, 12, 18, 23, 29, 36],
    [9, 10, 13, 19, 24, 31, 37],
    [2, 4, 14, 16, 22, 26, 33],
]

flat = [n for row in history_numbers for n in row]
counter = Counter(flat)

# 🎯 重み付きランダム予想
def weighted_draw(counter, k=7):
    pop = list(counter.keys())
    weights = [counter[n] for n in pop]
    result = set()
    while len(result) < k:
        n = random.choices(pop, weights=weights)[0]
        result.add(n)
    return sorted(result)

if st.button("出現回数ランキング", key="rank_btn"):
    df = pd.DataFrame(counter.items(), columns=["数字", "出現回数"])
    df = df.sort_values("出現回数", ascending=False).reset_index(drop=True)
    st.dataframe(df)

if st.button("♡ ナナコさんに占ってもらう ♡", key="predict_btn"):
    st.markdown("### 💫 ナナコさんの3つの予想 💫")
    for i in range(1, 4):
        nums = weighted_draw(counter, 7)
        st.markdown(f'<div class="number-output">💖 パターン{i}：' + ', '.join(map(str, nums)) + '</div>', unsafe_allow_html=True)

    st.markdown("""
        <div style="margin-top:30px; text-align:center; font-size:20px; color:#b030b0;">
        💬 「当たるといいわね♡」
        </div>
    """, unsafe_allow_html=True)
