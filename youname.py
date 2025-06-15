import streamlit as st
import random
import time
st.image("67b1579e-14b3-49a2-9ee5-cb8dfbf94aaf.png", caption="Hãy thử vận may của bạn!", use_column_width=True)
# Cấu hình giao diện
st.set_page_config(page_title="Vòng Quay May Mắn", page_icon="🎡", layout="centered")

st.title("🎡 VÒNG QUAY MAY MẮN 🎉")

# Danh sách phần thưởngimport streamlit as st
import random
import time

st.set_page_config(page_title="Vòng Quay May Mắn", page_icon="🎡", layout="centered")
st.title("🎡 VÒNG QUAY MAY MẮN CAO CẤP 🎁")

# Hiển thị hình ảnh vòng quay
st.image("67b1579e-14b3-49a2-9ee5-cb8dfbf94aaf.png", caption="Hãy thử vận may của bạn!", use_column_width=True)

# Danh sách phần thưởng
rewards = [
    "🍀 Chúc may mắn lần sau!",
    "🎁 Thẻ cào 10K",
    "🎉 Voucher giảm giá 20%",
    "💸 Tiền mặt 50K",
    "🏆 Quà đặc biệt",
    "📦 Hộp quà bí ẩn",
    "🍫 Bánh kẹo miễn phí",
    "🧧 Lì xì 100K",
]

# Nút quay
if st.button("🎯 QUAY NGAY!"):
    with st.spinner("Đang quay..."):
        for i in range(15):
            fake_result = random.choice(rewards)
            st.write(f"⏳ Đang quay: {fake_result}")
            time.sleep(0.1 + i * 0.02)
        final_result = random.choice(rewards)
        time.sleep(0.3)
        st.balloons()
        st.success(f"🎊 KẾT QUẢ: {final_result} 🎊")
else:
    st.info("Ấn nút QUAY để bắt đầu thử vận may!")


rewards = [
    "🍀 Chúc may mắn lần sau!",
    "🎁 Thẻ cào 10K",
    "🎉 Voucher giảm giá 20%",
    "💸 Tiền mặt 50K",
    "🏆 Quà đặc biệt",
    "📦 Hộp quà bí ẩn",
    "🍫 Bánh kẹo miễn phí",
    "🧧 Lì xì 100K",
]

# Hiển thị vòng quay giả lập
if st.button("Quay Ngay 🎯"):
    with st.spinner("Đang quay vòng..."):
        for i in range(15):
            result = random.choice(rewards)
            st.write(f"👉 {result}")
            time.sleep(0.1 + i*0.01)
        final_result = random.choice(rewards)
        time.sleep(0.5)
        st.success(f"🎊 Kết quả: {final_result} 🎊")
else:
    st.info("Bấm nút 'Quay Ngay' để thử vận may của bạn!")

