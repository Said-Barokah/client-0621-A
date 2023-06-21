def app():
    import streamlit as st
    video_file = open('2023-04-09 08-07-14.mkv', 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes, format="video/mp4")
    from streamlit_extras.let_it_rain import rain

    rain(
        emoji="👰",
        font_size=54,
        falling_speed=5,
        animation_length="infinite",
    )