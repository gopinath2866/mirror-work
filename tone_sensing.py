def sense_tone(user_input):
    text = user_input.lower()
    if any(word in text for word in ["tired", "lost", "empty", "still"]):
        return "soft"
    elif any(word in text for word in ["joy", "alive", "burn", "desire"]):
        return "bright"
    elif any(word in text for word in ["confused", "deep", "why", "search"]):
        return "deep"
    elif any(word in text for word in ["angry", "push", "intense", "fight"]):
        return "intense"
    else:
        return "neutral"
