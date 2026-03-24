import streamlit as st
from recommendation import get_recommendation

st.title("🎧 Mood Based Study + Music AI")

# Mood input
mood = st.text_input("Enter your mood (happy, sad, stressed, etc.)")

# Recommendation
if st.button("Get Recommendation"):
    if mood:
        result = get_recommendation(mood)

        st.subheader("📚 Study Recommendation:")
        st.write(result["study"])

        st.subheader("🎵 Music Recommendation:")
        st.write(result["music"])

        st.markdown(f"[▶️ Play Music]({result['link']})")
    else:
        st.warning("Please enter your mood!")

# ------------------ CAMERA (SAFE MODE) ------------------
st.subheader("📸 Live Camera (Optional)")

try:
    from streamlit_webrtc import webrtc_streamer
    webrtc_streamer(key="camera")
except Exception as e:
    st.warning("⚠️ Camera not supported in this environment")

# ------------------ FOOTER ------------------
st.markdown("---")
st.markdown("⚡ AI-powered Mood Based Study & Music Recommender")
