import streamlit as st
from recommendation import get_recommendation
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import av

# ------------------ CAMERA CLASS ------------------
class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        return img

# ------------------ UI ------------------
st.title("🎧 Mood Based Study + Music AI")

# Mood input
mood = st.text_input("Enter your mood (happy, sad, stressed, etc.)")

# Recommendation button
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

# ------------------ CAMERA SECTION ------------------
st.subheader("📸 Live Camera")

webrtc_streamer(
    key="camera",
    video_transformer_factory=VideoTransformer
)

# ------------------ FOOTER ------------------
st.markdown("---")
st.markdown("⚡ AI-powered Mood Based Study & Music Recommender")