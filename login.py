import streamlit as st

# Informasi pengguna yang valid
def authent(username, password):
    import pandas as pd
    df_user = pd.read_csv('user.csv')
    if username == df_user['user'][0] and password ==str(df_user['password'][0]):
        return True
    return False

def login():
    st.title("Login Page")
    st.write("Silakan masuk menggunakan username dan password Anda.")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authent(username, password):
            st.session_state.login_status = True
            st.success("Login berhasil! dan klik tombol login sekali lagi untuk masuk utama")
            # Tandai status login sebagai berhasil
        else:
            st.error("Username atau password salah.")


if 'login_status' not in st.session_state:
    st.session_state.login_status = False

if  not st.session_state.login_status:
    login()
else:
    import video
    video.app()

            
# main()
