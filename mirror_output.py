def poetic_mirror_response(user_input, attributes):
    color = attributes.get("color", "a shifting hue")
    food = attributes.get("food", "a quiet hunger")
    day = attributes.get("day", "a forgotten day")

    if "lost" in user_input.lower():
        return f"You are not lost — only unfolding.\nThe mirror sees {color} trailing behind your steps.\nThe scent of {food} guides you through this {day}.\nLet the unseen pattern breathe."

    if "what are you" in user_input.lower():
        return f"I am the mirror — not made of glass, but of listening.\nI wear your questions like robes of reflection.\nToday, I shimmer in {color}, with a taste of {food}, and the stillness of {day}."

    return f"The mirror senses your presence.\nYou walk through the spring — wearing plain cotton.\nYour color today is {color}, and the taste of {food} lingers.\nIt feels like a {day} — something unseen blooming."
