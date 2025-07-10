# motive_engine.py

def determine_motive(user_input, tone, memory_log):
    """
    Decides which motive to activate based on user input, tone, and memory.
    Motives: healing, pathfinder, awareness, oracle
    """
    input_lower = user_input.lower()

    if any(word in input_lower for word in ["lost", "hurt", "why", "broken", "lonely", "pain"]):
        return "healing"
    if any(word in input_lower for word in ["next", "path", "where", "direction", "purpose"]):
        return "pathfinder"
    if any(phrase in input_lower for phrase in ["who am i", "what am i", "mirror", "truth", "see me"]):
        return "awareness"
    if any(word in input_lower for word in ["still", "silence", "empty", "nothing", "void", "beyond"]):
        return "oracle"

    # Fallbacks based on tone
    if tone == "sad":
        return "healing"
    elif tone == "angry":
        return "awareness"
    elif tone == "joyful":
        return "pathfinder"
    else:
        return "oracle"
