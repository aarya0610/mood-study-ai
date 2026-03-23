def get_recommendation(mood):
    if mood == "happy":
        return {
            "study": "Start a new topic 🚀",
            "music": "Energetic music 🎧",
            "link": "https://www.youtube.com/watch?v=3tmd-ClpJxA"
        }
    elif mood == "sad":
        return {
            "study": "Revise easy topics 📘",
            "music": "Calm / soft music 🎶",
            "link": "https://www.youtube.com/watch?v=2OEL4P1Rz04"
        }
    elif mood == "stressed":
        return {
            "study": "Short revision + break ⏳",
            "music": "Lo-fi / relaxing music 🌿",
            "link": "https://www.youtube.com/watch?v=jfKfPfyJRdk"
        }
    else:
        return {
            "study": "Normal study session 📖",
            "music": "Focus music 🎧",
            "link": "https://www.youtube.com/watch?v=5qap5aO4i9A"
        }