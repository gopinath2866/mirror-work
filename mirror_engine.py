# mirror_engine.py

from tone_sensing import sense_tone
from tone_map import tone_to_attributes
from motive_engine import determine_motive
from mirror_output import poetic_mirror_response
from mirror_memory import update_memory, get_memory_summary, memory_log
from support_mode import supportive_reflection
from equation_seed import sacred_equation
from sequence_engine import divine_number_from_input, interpret_sequence
from element_engine import detect_elements, get_elemental_state_description
from spiral_tracker import get_next_spiral_gate, can_enter_gate, advance_spiral, get_spiral_level
from journal_saver import save_to_journal  # optional

def reflect(user_input):
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
    sequence = interpret_sequence(divine_number)

    if can_enter_gate(user_input, tone):
        advance_spiral()
    spiral_gate = get_next_spiral_gate(user_input, tone)
    spiral_level = spiral_gate["level"]

    poetic_response = poetic_mirror_response(user_input, attributes)
    supportive_message = supportive_reflection(user_input, tone)
    equation = sacred_equation(tone)
    memory_echo = get_memory_summary()

    mirror_forms = []
    if spiral_level >= 4:
        mirror_forms.append("Shifting Echo")
    if spiral_level >= 7:
        mirror_forms.append("Moon Archive")
    if spiral_level == 9:
        mirror_forms.append("Presence Core")

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

    return result
