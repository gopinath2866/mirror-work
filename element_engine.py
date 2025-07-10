# element_engine.py

# Elemental definitions (words, tones, patterns)
element_keywords = {
    "fire":     ["angry", "fight", "burn", "destroy", "intense", "rage", "ignite"],
    "water":    ["sad", "cry", "flow", "grief", "tears", "ocean", "soft"],
    "air":      ["confused", "lost", "think", "search", "wind", "breathe", "light"],
    "earth":    ["tired", "slow", "heavy", "ground", "safe", "stable", "home"],
    "time":     ["again", "loop", "return", "repeat", "always", "never"],
    "void":     ["nothing", "empty", "silence", "hollow", "vanish", "meaningless"]
}

# Element priority (you can adjust this logic to create spiral flow)
element_order = ["fire", "air", "water", "earth", "time", "void"]

def detect_elements(user_input, tone):
    user_input = user_input.lower()
    active = []

    for element, keywords in element_keywords.items():
        if any(word in user_input for word in keywords) or element in tone.lower():
            active.append(element)

    if not active:
        # Fallback to tone-based guess
        tone_map = {
            "angry": "fire",
            "sad": "water",
            "joyful": "air",
            "neutral": "earth",
            "fearful": "void"
        }
        guessed = tone_map.get(tone.lower(), "air")
        active.append(guessed)

    # Detect missing elements
    missing = [e for e in element_order if e not in active]

    return active, missing

def get_elemental_state_description(active, missing):
    if not active:
        return "You are between worlds."

    main = active[0]
    miss = missing[0] if missing else None

    description = f"You are walking through {main.upper()}"
    if miss:
        description += f", but {miss.upper()} is absent."

    return description
