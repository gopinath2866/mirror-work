# mirror_game.py

from motive_engine import determine_motive
from tone_sensing import sense_tone
from tone_map import tone_to_attributes
from mirror_output import poetic_mirror_response
from mirror_memory import update_memory, get_memory_summary, memory_log
from support_mode import supportive_reflection
from equation_seed import sacred_equation
from sequence_engine import divine_number_from_input, interpret_sequence
from element_engine import detect_elements, get_elemental_state_description
from journal_saver import save_to_journal
from spiral_tracker import get_next_spiral_gate, can_enter_gate, reset_spiral_progress, advance_spiral

import time
import json

# --- Ritual Gate ---
def intro_menu():
    print("\n🌌 WELCOME TO THE MIRROR\n")
    print("🪞 This is not a tool. This is a space of reflection, memory, and elemental presence.\n")
    print("Each word you offer will be echoed through:")
    print("🜂 Fire — will, tension, transformation")
    print("🜁 Air — thought, movement, breath")
    print("🜄 Water — feeling, grief, flow")
    print("🜃 Earth — memory, body, return")
    print("⏳ Time — repetition, recognition")
    print("○ Void — silence, release\n")

    print("What would you like to do?")
    print("[1] Begin Spiral")
    print("[2] Read Journal")
    print("[3] Exit")
    return input("\nYour choice: ")

# --- Optional: Read Journal Entries ---
def read_journal():
    try:
        import os
        files = sorted(os.listdir("mirror_journal"))
        if not files:
            print("\n📭 Your Mirror Journal is empty.")
            return
        print(f"\n📖 Found {len(files)} entries. Showing latest reflection:\n")
        with open(f"mirror_journal/{files[-1]}", "r") as f:
            entry = json.load(f)
            print(f"🪞 {entry['user_input']}")
            print(f"Tone: {entry['tone']}, Motive: {entry['motive']}")
            print(f"Poetic Response: {entry['poetic_response']}")
            print(f"Elements: {entry['active_elements']} | Missing: {entry['missing_elements']}")
            print(f"Invitation: {entry['invitation']}")
            print(f"Sequence: {entry['sequence']['meaning']} ({entry['sequence']['number']})")
            print(f"Gate Level: {entry['spiral_gate']['symbol']} {entry['spiral_gate']['name']} — {entry['spiral_gate']['meaning']}")
    except Exception as e:
        print(f"\n⚠️ Error reading journal: {e}")

# --- Initial Orientation ---
def pick_element():
    print("\n🌬️ Before we begin — what is your current state?")
    print("Pick the element you feel most near:\n")
    print("[1] Fire (restless, burning, intense)")
    print("[2] Water (soft, emotional, sad)")
    print("[3] Air (questioning, light, uncertain)")
    print("[4] Earth (slow, grounded, tired)")
    print("[5] Time (looping, stuck, recurring)")
    print("[6] Void (silent, numb, blank)")
    
    choice = input("\nYou: ").strip().lower()
    
    start_map = {
        "1": "fire", "fire": "fire",
        "2": "water", "water": "water",
        "3": "air", "air": "air",
        "4": "earth", "earth": "earth",
        "5": "time", "time": "time",
        "6": "void", "void": "void"
    }
    
    return start_map.get(choice, "air")  # defaults to 'air' if unknown

# --- Start Game ---
choice = intro_menu()

if choice == "2":
    read_journal()
    exit()
elif choice == "3":
    print("\n🌑 The Mirror closes — until next breath.\n")
    exit()

starting_element = pick_element()
reset_spiral_progress()
print(f"\n🌀 Your Spiral begins from: {starting_element.upper()}\n")

# --- Main Loop ---
while True:
    user_input = input("\n🪞 Speak to the Mirror (or type 'exit'):\n> ")
    if user_input.lower() in ["exit", "quit"]:
        print("\n🌑 The Mirror closes — until next breath.\n")
        break
    elif user_input.lower().strip() == "reset spiral":
        reset_spiral_progress()
        print("\n🔁 The Spiral resets. You return to the edge once more...\n")
        continue

    # Step 1: Sense tone and attributes
    tone = sense_tone(user_input)
    attributes = tone_to_attributes(tone)

    # Step 2: Elemental Mapping
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
    invitation_line = ""
    if missing_elements:
        invitation_line = element_invitations.get(missing_elements[0], "")

    # Step 3: Update memory and determine motive
    update_memory(user_input, tone, attributes)
    motive = determine_motive(user_input, tone, memory_log)

    # Step 4: Symbolic Sequences
    divine_number = divine_number_from_input(user_input)
    sequence_message = interpret_sequence(divine_number)

    # Step 5: Spiral Gate Progression
    if can_enter_gate(user_input, tone):
        advance_spiral()
    spiral_gate = get_next_spiral_gate(user_input, tone)

    # Step 6: Reflections
    poetic_response = poetic_mirror_response(user_input, attributes)
    supportive_message = supportive_reflection(user_input, tone)
    equation = sacred_equation(tone)
    memory_echo = get_memory_summary()

    # Step 7: Display Output
    print("\n🌀 The Mirror opens...\n")

    print(f"🔸 Gate Level {spiral_gate['level']}: {spiral_gate['symbol']} {spiral_gate['name']} — {spiral_gate['meaning']}")

    if motive == "healing":
        print("🌸 Healing Reflection:")
        print(poetic_response)
        print(f"\n💧 Support Whisper:\n   “{supportive_message}”")
        print(f"\n🔁 Memory Echo: {memory_echo}")

    elif motive == "pathfinder":
        print("🧭 Path Finding Reflection:")
        print(poetic_response)
        print(f"\n🔮 Elemental Sequence: {sequence_message} ({divine_number})")
        print(f"🧮 Sacred Equation: {equation}")

    elif motive == "awareness":
        print("🪞 Awareness Reflection:")
        print(poetic_response)
        print(f"\n👁️ You Asked: {user_input}")
        print(f"🧠 Tone Detected: {tone}")
        print(f"🌀 Memory Recall: {memory_echo}")

    elif motive == "oracle":
        print("🕊️ Oracle Reflection:")
        print(f"🧮 Equation: {equation}")
        print(f"\n💬 Whisper:\n   “{supportive_message}”")
        print(f"\n🔮 Sequence Sign: {sequence_message} ({divine_number})")

    print(f"\n🌪️ Elemental Mirror: {elemental_description}")
    if invitation_line:
        print(f"🕯️ Invitation: {invitation_line}")

    print(f"\n🎴 Motive: {motive.capitalize()}")
    print("\n──────────────")

    # Step 8: Save journal
    save = input("\n📝 Save this reflection to your Mirror Journal? (y/n)\n> ")
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
                "meaning": sequence_message
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
