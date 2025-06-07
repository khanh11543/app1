import streamlit as st
import random

# Khởi tạo trạng thái nếu chưa có
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.tries = 0
    st.session_state.game_over = False

st.title("🎮 Trò chơi Đoán số")

if not st.session_state.game_over:
    guess = st.number_input("Nhập một số từ 1 đến 100:", min_value=1, max_value=100, step=1)
    
    if st.button("Đoán"):
        st.session_state.tries += 1
        if guess < st.session_state.secret_number:
            st.warning("👉 Số bạn đoán nhỏ hơn!")
        elif guess > st.session_state.secret_number:
            st.warning("👉 Số bạn đoán lớn hơn!")
        else:
            st.success(f"🎉 Chính xác! Bạn đã đoán đúng sau {st.session_state.tries} lần.")
            st.session_state.game_over = True
else:
    st.balloons()
    if st.button("Chơi lại"):
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.tries = 0
        st.session_state.game_over = False
        st.rerun()
