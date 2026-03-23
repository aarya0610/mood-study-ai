from camera import detect_mood
import streamlit as st
from mood import get_mood
from recommendation import get_recommendation

st.title("🧠 Mood-Based Study & Music AI")

st.write("Enter your current mood 👇")
if st.button("📸 Detect Mood from Camera"):
    mood = detect_mood()
    result = get_recommendation(mood)

    st.subheader("📸 Camera Result:")
    st.write("Detected Mood:", mood)
    st.write("📚 Study:", result["study"])
    st.write("🎧 Music:", result["music"])
    st.markdown(f"[🎧 Play Music]({result['link']})")

user_input = st.text_input("Your Mood:")

if st.button("Get Suggestion"):
    mood = get_mood(user_input)
    result = get_recommendation(mood)

    st.subheader("🎯 Results:")
    st.write("Detected Mood:", mood)
    st.write("📚 Study Suggestion:", result["study"])
    st.write("🎧 Music Suggestion:", result["music"])

    st.markdown(f"[🎧 Play Music]({result['link']})")