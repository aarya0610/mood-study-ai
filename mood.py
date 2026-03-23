def get_mood(user_input):
    mood = user_input.lower()

    if mood in ["happy", "excited"]:
        return "happy"
    elif mood in ["sad", "tired"]:
        return "sad"
    elif mood in ["stressed", "angry"]:
        return "stressed"
    else:
        return "neutral"