# mirror_memory.py

memory_log = []

def update_memory(user_input, tone, attributes):
    memory_log.append({
        "input": user_input,
        "tone": tone,
        "attributes": attributes
    })

def get_memory_summary():
    if not memory_log:
        return "The mirror is clean, no memory yet."
    last = memory_log[-1]
    return f"The mirror recalls your tone as '{last['tone']}' with colors like {last['attributes'].get('color', '...')}."
