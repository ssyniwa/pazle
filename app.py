import streamlit as st
import numpy as np

st.title("ライツアウト in Streamlit")

# 1. 盤面サイズの設定
SIZE = 3

# 2. ゲーム状態の初期化 (初回実行時のみ)
if 'grid' not in st.session_state:
    # 全て消灯(False)状態で初期化（本来はランダム配置が望ましい）
    st.session_state.grid = np.zeros((SIZE, SIZE), dtype=bool)

def flip_tile(r, c):
    """ 指定したマスとその上下左右を反転させる関数 """
    for dr, dc in [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < SIZE and 0 <= nc < SIZE:
            st.session_state.grid[nr, nc] = not st.session_state.grid[nr, nc]

# 3. 画面描画
st.write("全てのタイルを消灯（グレー）にしてください！")

# グリッド状にボタンを配置
for r in range(SIZE):
    cols = st.columns(SIZE)
    for c in range(SIZE):
        # 状態に応じてラベルと色を変える（簡易的に絵文字を使用）
        label = "🟡" if st.session_state.grid[r, c] else "⚫"
        # ボタンが押されたら状態を反転
        cols[c].button(label, key=f"{r}-{c}", on_click=flip_tile, args=(r, c))

# 4. クリア判定
if not st.session_state.grid.any():
    st.success("クリア！おめでとうございます！")
    if st.button("リセット"):
        st.session_state.grid = np.random.choice([True, False], size=(SIZE, SIZE))
        st.rerun()