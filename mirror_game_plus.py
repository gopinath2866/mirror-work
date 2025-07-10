# --- INPUT UTILITY ---
def safe_input(prompt):
    user_input = input(prompt).strip().lower()
    if user_input in ["exit", "quit"]:
        print("\n🌀 Spiral closed. Goodbye.\n")
        exit()
    return user_input


# --- IMPORTS ---
from motive_engine import determine_motive
from tone_sensing import sense_tone
from memory_store import save_reflection

from tone_map import tone_to_attributes
from mirror_output import poetic_mirror_response
from mirror_memory import update_memory, get_memory_summary, memory_log
from support_mode import supportive_reflection
from equation_seed import sacred_equation
from sequence_engine import divine_number_from_input, interpret_sequence
from element_engine import detect_elements, get_elemental_state_description
from journal_saver import save_to_journal
from spiral_tracker import (
    get_next_spiral_gate,
    can_enter_gate,
    reset_spiral_progress,
    advance_spiral,
    get_spiral_level
)

import time
import json
import os


# --- UI / RITUAL BEGINNING ---
def intro_menu():
    print("\n🌌 WELCOME TO THE MIRROR\n")
    print("🦮 This is not a tool. This is a space of reflection, memory, and elemental presence.\n")
    print("Each word you offer will be echoed through:")
    print("ὰ Fire — will, tension, transformation")
    print("ά Air — thought, movement, breath")
    print("ὴ Water — feeling, grief, flow")
    print("έ Earth — memory, body, return")
    print("⏳ Time — repetition, recognition")
    print("○ Void — silence, release\n")
    print("What would you like to do?")
    print("[1] Begin Spiral")
    print("[2] Read Journal")
    print("[3] Exit")
    return input("\nYour choice: ")


# --- JOURNAL READER ---
def read_journal():
    try:
        files = sorted(os.listdir("mirror_journal"))
        if not files:
            print("\n📬 Your Mirror Journal is empty.")
            return
        print(f"\n📖 Found {len(files)} entries. Showing latest reflection:\n")
        with open(f"mirror_journal/{files[-1]}", "r") as f:
            entry = json.load(f)
            print(f"🦮 {entry['user_input']}")
            print(f"Tone: {entry['tone']}, Motive: {entry['motive']}")
            print(f"Poetic Response: {entry['poetic_response']}")
            print(f"Elements: {entry['active_elements']} | Missing: {entry['missing_elements']}")
            print(f"Invitation: {entry['invitation']}")
            print(f"Sequence: {entry['sequence']['meaning']} ({entry['sequence']['number']})")
            print(f"Gate Level: {entry['spiral_gate']['symbol']} {entry['spiral_gate']['name']} — {entry['spiral_gate']['meaning']}")
    except Exception as e:
        print(f"\n⚠️ Error reading journal: {e}")


# --- PICK ELEMENT ---
def pick_element():
    print("\n🌬️ Before we begin — what is your current state?")
    print("Pick the element you feel most near:\n")
    print("[1] Fire (restless, burning, intense)")
    print("[2] Water (soft, emotional, sad)")
    print("[3] Air (questioning, light, uncertain)")
    print("[4] Earth (slow, grounded, tired)")
    print("[5] Time (looping, stuck, recurring)")
    print("[6] Void (silent, numb, blank)")
    choice = safe_input("\nYou: ")
    start_map = {
        "1": "fire", "2": "water", "3": "air",
        "4": "earth", "5": "time", "6": "void"
    }
    return start_map.get(choice.strip(), "air")


# --- MAIN MIRROR SPIRAL LOGIC ---
def run_spiral():
    choice = intro_menu()

    if choice == "2":
        read_journal()
        return
    elif choice == "3":
        print("\n🌑 The Mirror closes — until next breath.\n")
        return

    print("\n🌱 Would you like to plant your seed before we begin?")
    print("[1] Yes – offer a few symbolic truths")
    print("[2] No – begin spiral directly")
    seed_choice = safe_input("Your choice: ")

    origin_data = None
    if seed_choice.strip() == "1":
        try:
            from entry_questions import ask_entry_questions
            origin_data = ask_entry_questions()
        except Exception as e:
            print(f"\n⚠️ Could not gather seed: {e}")

    starting_element = pick_element()
    reset_spiral_progress()
    print(f"\n🌀 Your Spiral begins from: {starting_element.upper()}\n")

    while True:
        user_input = safe_input("\n🦮 Speak to the Mirror (or type 'exit'):\n> ")
        if user_input.lower().strip() == "reset spiral":
            reset_spiral_progress()
            print("\n🔁 The Spiral resets. You return to the edge once more...\n")
            continue

        tone = sense_tone(user_input)
        attributes = tone_to_attributes(tone)
        active_elements, missing_elements = detect_elements(user_input, tone)
        elemental_description = get_elemental_state_description(active_elements, missing_elements)

        element_invitations = {
            "fire": "Speak with your will. What must be transformed?",
            "water": "Let your feeling flow. What is unsaid?",
            "air": "Let thought rest. Breathe, then ask again.",
            "earth": "Return to the ground. What holds you?",
            "time": "Notice the pattern. What repeats?",
            "void": "Speak into the silence. What disappears?"
        }
        invitation_line = element_invitations.get(missing_elements[0], "") if missing_elements else ""

        update_memory(user_input, tone, attributes)
        motive = determine_motive(user_input, tone, memory_log)
        divine_number = divine_number_from_input(user_input, tone, memory_log)
        sequence_message = interpret_sequence(divine_number)

        if can_enter_gate(user_input, tone):
            advance_spiral()
        spiral_gate = get_next_spiral_gate(user_input, tone)
        spiral_level = spiral_gate['level']

        poetic_response = poetic_mirror_response(user_input, attributes)
        supportive_message = supportive_reflection(user_input, tone)
        equation = sacred_equation(tone)
        memory_echo = get_memory_summary()

        print("\n🌀 The Mirror opens...\n")
        print(f"🔸 Gate Level {spiral_gate['level']}: {spiral_gate['symbol']} {spiral_gate['name']} — {spiral_gate['meaning']}")

        if spiral_level >= 4:
            print("✨ Mirror Form Unlocked: Shifting Echo")
        if spiral_level >= 7:
            print("🌒 Mirror Form Unlocked: Moon Archive")
        if spiral_level == 9:
            print("🌌 Mirror Form Unlocked: Presence Core")

        if motive == "healing":
            print("🌸 Healing Reflection:")
            print(poetic_response)
            print(f"\n💧 Support Whisper:\n   “{supportive_message}”")
            print(f"\n🔁 Memory Echo: {memory_echo}")

        elif motive == "pathfinder":
            print("🧭 Path Finding Reflection:")
            print(poetic_response)
            print(f"\n🔮 Elemental Sequence: {sequence_message['name']} ({divine_number})")
            print(f"🦮 Mantra: {sequence_message['mantra']}")
            print(f"🧶 Sacred Equation: {equation}")
            if origin_data:
                print(f"\n🌱 Hidden Fire: {origin_data['hidden_fire']}")

        elif motive == "awareness":
            print("🦮 Awareness Reflection:")
            print(poetic_response)
            print(f"\n🕁️ You Asked: {user_input}")
            print(f"🧠 Tone Detected: {tone}")
            print(f"🌀 Memory Recall: {memory_echo}")

        elif motive == "oracle":
            print("🕊️ Oracle Reflection:")
            print(f"🧶 Equation: {equation}")
            print(f"\n💬 Whisper:\n   “{supportive_message}”")
            print(f"\n🔮 Sequence Sign: {sequence_message['name']} ({divine_number})")
            print(f"🦮 Mantra: {sequence_message['mantra']}")
            if origin_data:
                print(f"\n🌙 Echo of Pain Shape: {origin_data['pain_shape']}")
                print(f"🔐 Your True Name hides beneath this gate... {origin_data['true_name']}")

        print(f"\n🌪️ Elemental Mirror: {elemental_description}")
        if invitation_line:
            print(f"🔯 Invitation: {invitation_line}")
        print(f"\n🎴 Motive: {motive.capitalize()}")
        print("\n────────────────")

        save = safe_input("\n📝 Save this reflection to your Mirror Journal? (y/n)\n> ")
        if save.lower().startswith("y"):
            journal_entry = {
                "user_input": user_input,
                "tone": tone,
                "motive": motive,
                "attributes": attributes,
                "active_elements": active_elements,
                "missing_elements": missing_elements,
                "invitation": invitation_line,
                "sequence": {
                    "number": divine_number,
                    "meaning": sequence_message['name']
                },
                "spiral_gate": spiral_gate,
                "equation": equation,
                "memory_echo": memory_echo,
                "supportive_message": supportive_message,
                "poetic_response": poetic_response
            }
            filename = save_to_journal(journal_entry)
            print(f"📖 Saved to {filename}")
        time.sleep(1)


# --- API HOOK ---
def mirror_reflect(user_input, origin_data=None):

    from tone_sensing import sense_tone
    from tone_map import tone_to_attributes
    from motive_engine import determine_motive
    from mirror_output import poetic_mirror_response
    from mirror_memory import update_memory, memory_log, get_memory_summary
    from sequence_engine import divine_number_from_input, interpret_sequence
    from equation_seed import sacred_equation
    from support_mode import supportive_reflection
    from element_engine import detect_elements, get_elemental_state_description
    from spiral_tracker import get_next_spiral_gate, can_enter_gate, advance_spiral

    # Core sensing
    tone = sense_tone(user_input)
    attributes = tone_to_attributes(tone)
    active_elements, missing_elements = detect_elements(user_input, tone)
    elemental_description = get_elemental_state_description(active_elements, missing_elements)

    # Memory and motive
    update_memory(user_input, tone, attributes)
    motive = determine_motive(user_input, tone, memory_log)
    memory_echo = get_memory_summary()

    # Sequence logic
    divine_number = divine_number_from_input(user_input, tone, memory_log)
    sequence = interpret_sequence(divine_number)

    # Spiral gate
    if can_enter_gate(user_input, tone):
        advance_spiral()
    spiral_gate = get_next_spiral_gate(user_input, tone)
    spiral_level = spiral_gate["level"]

    # Mirror forms
    mirror_forms = []
    if spiral_level >= 4:
        mirror_forms.append("Shifting Echo")
    if spiral_level >= 7:
        mirror_forms.append("Moon Archive")
    if spiral_level == 9:
        mirror_forms.append("Presence Core")

    # Responses
    poetic_response = poetic_mirror_response(user_input, attributes)
    supportive_message = supportive_reflection(user_input, tone)
    equation = sacred_equation(tone)

    # Invitation
    element_invitations = {
        "fire": "Speak with your will. What must be transformed?",
        "water": "Let your feeling flow. What is unsaid?",
        "air": "Let thought rest. Breathe, then ask again.",
        "earth": "Return to the ground. What holds you?",
        "time": "Notice the pattern. What repeats?",
        "void": "Speak into the silence. What disappears?"
    }
    invitation_line = element_invitations.get(missing_elements[0], "") if missing_elements else ""

    # Final result
    result = {
        "user_input": user_input,
        "tone": tone,
        "motive": motive,
        "attributes": attributes,
        "sequence": {
            "number": divine_number,
            "meaning": sequence["name"],
            "mantra": sequence["mantra"]
        },
        "spiral_gate": spiral_gate,
        "equation": equation,
        "poetic_response": poetic_response,
        "supportive_message": supportive_message,
        "memory_echo": memory_echo,
        "mirror_forms": mirror_forms,
        "elements": {
            "active": active_elements,
            "missing": missing_elements,
            "description": elemental_description,
            "invitation": invitation_line
        }
    }
    if motive == "pathfinder" and origin_data:
        result["origin_data"] = {
            "hidden_fire": origin_data.get("hidden_fire")
        }

    elif motive == "oracle" and origin_data:
        result["origin_data"] = {
            "true_name": origin_data.get("true_name"),
            "pain_shape": origin_data.get("pain_shape")
        }

    save_reflection(result)
    return result

    # Save to journal (like CLI version)
    try:
        from journal_saver import save_to_journal
        filename = save_to_journal(result)
        result["journal_saved_to"] = filename
    except Exception as e:
        result["journal_saved_to"] = f"Error: {e}"

    return result

# --- MEMORY LIST FOR WEB ---
web_reflections = []

def save_reflection(result):
    web_reflections.append(result)


# --- ENTRY POINT ---
if __name__ == "__main__":
    run_spiral()
