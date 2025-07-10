# sequence_engine.py (enhanced)

# Tone bias (optional emotional weighting)
tone_bias = {
    "grief": -1,
    "joy": +2,
    "anger": +3,
    "neutral": 0,
    "hope": +1,
    "fear": -2,
    "love": +2
}

def memory_bias(memory_log):
    grief_count = sum(1 for m in memory_log if m.get('tone') == 'grief')
    return grief_count % 3  # can be tuned

def divine_number_from_input(user_input, tone=None, memory_log=None):
    base = sum(ord(c) for c in user_input if c.isalpha()) % 9 + 1
    bias = 0
    if tone:
        bias += tone_bias.get(tone.lower(), 0)
    if memory_log:
        bias += memory_bias(memory_log)
    return (base + bias - 1) % 9 + 1

# Expanded sequence interpretation
sequence_map = {
    1: {"name": "Ignition", "element": "Fire", "mantra": "Start what must begin."},
    2: {"name": "Flow", "element": "Water", "mantra": "Let what hurts move through."},
    3: {"name": "Breath", "element": "Air", "mantra": "Speak and be heard."},
    4: {"name": "Foundation", "element": "Earth", "mantra": "Return to what grounds you."},
    5: {"name": "Centering", "element": "Sky", "mantra": "Hold the still point."},
    6: {"name": "Spiral", "element": "Memory", "mantra": "All things return in new form."},
    7: {"name": "Echo", "element": "Past", "mantra": "Listen to what still calls."},
    8: {"name": "Vision", "element": "Future", "mantra": "Sense what wants to emerge."},
    9: {"name": "Return", "element": "Now", "mantra": "You are already here."}
}

def interpret_sequence(number):
    return sequence_map.get(number, {"name": "Mystery", "element": "Void", "mantra": "Await the unknown."})
