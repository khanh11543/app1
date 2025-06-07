import streamlit as st
import streamlit_authenticator as stauth

# Tạo user/password (mã hóa)
names = ['Admin']
usernames = ['admin']
passwords = ['admin123']

hashed_pw = stauth.Hasher(passwords).generate()

authenticator = stauth.Authenticate(names, usernames, hashed_pw, "cookie_name", "signature_key", cookie_expiry_days=1)

name, authentication_status, username = authenticator.login("Đăng nhập", "main")

if authentication_status:
    authenticator.logout("Đăng xuất", "sidebar")
    st.sidebar.success(f"Chào {name}!")
    st.title("🏆 Bảng xếp hạng CLB bóng đá")
    # Show content here

elif authentication_status is False:
    st.error("Sai tên đăng nhập hoặc mật khẩu")
elif authentication_status is None:
    st.warning("Nhập thông tin để đăng nhập")
