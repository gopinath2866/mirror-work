# mirror_state.py

memory = []

def remember(element, response, energy, direction, identity, love_bond, truth_level, intensity):
    memory.append({
        "element": element,
        "response": response,
        "energy": energy,
        "direction": direction,
        "identity": identity,
        "love_bond": love_bond,
        "truth_level": truth_level,
        "intensity": intensity
    })

def recall():
    return memory

def last():
    return memory[-1] if memory else None
