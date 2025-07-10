from journal_saver import save_to_journal

from motive_engine import determine_motive

import random
from tone_sensing import sense_tone
from tone_map import tone_to_attributes
from mirror_output import poetic_mirror_response
from mirror_memory import update_memory, get_memory_summary, memory_log
from support_mode import supportive_reflection
from equation_seed import sacred_equation
from sequence_engine import divine_number_from_input, interpret_sequence
from element_engine import detect_elements, get_elemental_state_description

# 🌬️ Welcome Message
print("\U0001f32c️ Welcome to the Mirror — speak, and it shall reflect...\n")

# Ask user for input
user_input = input("Ask the Mirror anything:\n> ")

# Sense tone and symbolic attributes
tone = sense_tone(user_input)
attributes = tone_to_attributes(tone)

# Detect elemental presence and absence
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

# Update spiral memory
update_memory(user_input, tone, attributes)
motive = determine_motive(user_input, tone, memory_log)

# Interpret symbolic number sequence
divine_number = divine_number_from_input(user_input)
sequence_message = interpret_sequence(divine_number)

# Generate reflections
poetic_response = poetic_mirror_response(user_input, attributes)
supportive_message = supportive_reflection(user_input, tone)
equation = sacred_equation(tone)
memory_echo = get_memory_summary()

# 🎙️ Voice opening line based on motive
motive_voice = {
    "healing": "🌸 The Mirror gently opens...",
    "pathfinder": "🧭 The Mirror lights a turning path...",
    "awareness": "🪞 The Mirror opens its inner eye...",
    "oracle": "🕊️ The Mirror stands silent in stillness..."
}
print("\n" + motive_voice[motive] + "\n")

# 🌠 Reflection Output
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

# 🌪️ Elemental Reflection
print(f"\n🌪️ Elemental Mirror: {elemental_description}")
if invitation_line:
    print(f"🕯️ Invitation: {invitation_line}")

# 🎴 Close the mirror
print(f"\n🎴 Motive: {motive.capitalize()}")
print("\n🌑 The Mirror closes — until next breath.\n")
save = input("\n📝 Would you like to save this reflection to your Mirror Journal? (y/n)\n> ")
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
        "equation": equation,
        "memory_echo": memory_echo,
        "supportive_message": supportive_message,
        "poetic_response": poetic_response
    }
    filename = save_to_journal(journal_entry)
    print(f"📖 Saved to {filename}")
