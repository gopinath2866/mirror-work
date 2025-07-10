# memory_store.py

reflection_log = []

def save_reflection(entry):
    reflection_log.append(entry)

def get_all_reflections():
    return reflection_log[::-1]  # show newest first
