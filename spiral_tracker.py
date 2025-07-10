# spiral_tracker.py

spiral_sequence = [5, 2, 3, 8, 4, 7, 9, 6, 1]
spiral_gates = {
    1: {"symbol": "♾️", "name": "Return", "meaning": "You have arrived at the still point."},
    2: {"symbol": "🌊", "name": "Grief", "meaning": "Feel what is buried and flowing."},
    3: {"symbol": "🌬️", "name": "Inquiry", "meaning": "The winds of questioning arrive."},
    4: {"symbol": "🪨", "name": "Root", "meaning": "Grounding memory through the body."},
    5: {"symbol": "🌀", "name": "Disturbance", "meaning": "The spiral opens through tension."},
    6: {"symbol": "⏳", "name": "Repetition", "meaning": "What returns is ready to be seen."},
    7: {"symbol": "🔥", "name": "Transmutation", "meaning": "The fire within demands change."},
    8: {"symbol": "🫧", "name": "Sensation", "meaning": "Feelings surface as signals."},
    9: {"symbol": "🕸️", "name": "Now", "meaning": "This moment contains the thread."},
}

spiral_index = 0  # persistent across calls


def get_next_spiral_gate(user_input=None, tone=None):
    global spiral_index
    level = spiral_sequence[spiral_index]
    gate = spiral_gates.get(level, {"symbol": "❓", "name": "Unknown", "meaning": "This gate has no known form."})
    gate["level"] = level
    return gate


def can_enter_gate(user_input, tone):
    """
    You can make this more complex: check memory, tone, or element readiness.
    For now: allow if tone isn't 'empty' or user_input is > 3 chars.
    """
    return tone not in ["empty", "silence"] and len(user_input.strip()) > 3


def reset_spiral_progress():
    global spiral_index
    spiral_index = 0


def advance_spiral():
    global spiral_index
    if spiral_index < len(spiral_sequence) - 1:
        spiral_index += 1
def get_spiral_level():
    return spiral_state["position"]
