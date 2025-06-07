import streamlit as st
import random

# ------------------------------
# CSS tùy chỉnh cho giao diện
st.markdown("""
    <style>
        .title {
            font-size: 40px;
            font-weight: bold;
            color: #4CAF50;
            text-align: center;
            margin-bottom: 20px;
        }
        .guess-box {
            background-color: #f0f0f0;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 2px 2px 10px #ccc;
        }
        .result {
            font-size: 20px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# ------------------------------
# Tạo trạng thái ban đầu
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.tries = 0
    st.session_state.game_over = False

# ------------------------------
# Tiêu đề đẹp
st.markdown('<div class="title">🎮 Trò chơi Đoán Số</div>', unsafe_allow_html=True)
st.markdown('<div class="guess-box">', unsafe_allow_html=True)

# ------------------------------
if not st.session_state.game_over:
    st.write("Tôi đã chọn một số bí mật từ **1 đến 100**. Hãy thử đoán nhé! 🎯")
    guess = st.number_input("🔢 Nhập số của bạn:", min_value=1, max_value=100, step=1)

    if st.button("🚀 Đoán"):
        st.session_state.tries += 1
        if guess < st.session_state.secret_number:
            st.warning("📉 Số bạn đoán **nhỏ hơn** số bí mật!")
        elif guess > st.session_state.secret_number:
            st.warning("📈 Số bạn đoán **lớn hơn** số bí mật!")
        else:
            st.success(f"🎉 Tuyệt vời! Bạn đã đoán đúng sau {st.session_state.tries} lần!")
            st.session_state.game_over = True
else:
    st.balloons()
    st.success("🎊 Trò chơi kết thúc!")
    if st.button("🔄 Chơi lại"):
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.tries = 0
        st.session_state.game_over = False
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
