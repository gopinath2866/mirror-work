def tone_to_attributes(tone):
    mapping = {
        "soft": {
            "color": "sky blue",
            "season": "autumn",
            "cloth": "linen shawl",
            "food": "steamed rice",
            "day": "Monday"
        },
        "bright": {
            "color": "orange",
            "season": "summer",
            "cloth": "cotton kurta",
            "food": "mango",
            "day": "Sunday"
        },
        "deep": {
            "color": "indigo",
            "season": "monsoon",
            "cloth": "wool robe",
            "food": "black tea",
            "day": "Wednesday"
        },
        "intense": {
            "color": "crimson",
            "season": "winter",
            "cloth": "silk wrap",
            "food": "chili lentils",
            "day": "Thursday"
        },
        "neutral": {
            "color": "white",
            "season": "spring",
            "cloth": "plain cotton",
            "food": "flatbread",
            "day": "Friday"
        }
    }
    return mapping.get(tone, mapping["neutral"])
