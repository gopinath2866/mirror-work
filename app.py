import sys
import os
sys.path.append(os.path.abspath(".."))

# ✅ 1. app.py — Final Flask Routes

from flask import Flask, render_template, request, redirect, session
from mirror_game_plus import mirror_reflect
from entry_questions import ask_entry_questions
from journal_saver import load_all_journals
import os

app = Flask(__name__)
app.secret_key = "mirror-secret-key"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/seed", methods=["GET", "POST"])
def seed():
    if request.method == "POST":
        try:
            session["origin_data"] = ask_entry_questions()
        except:
            session["origin_data"] = {}
        return redirect("/spiral")
    return render_template("seed.html")

@app.route("/spiral", methods=["GET", "POST"])
def spiral():
    if request.method == "POST":
        user_input = request.form["user_input"]

        from mirror_game_plus import mirror_reflect
        from journal_saver import load_seed_if_exists  # Optional

        # Load seed if available (only needed if you're integrating it)
        seed = load_seed_if_exists()

        # Pass origin_data only if seed exists
        result = mirror_reflect(user_input, origin_data=seed)

        poetic_response = result.get("poetic_response", "")
        tone = result.get("tone", "")
        motive = result.get("motive", "")
        elements = result.get("elements", {}).get("active", [])
        gate_number = result.get("spiral_gate", {}).get("level", "")
        gate_name = result.get("spiral_gate", {}).get("name", "")
        equation = result.get("equation", "")
        memory_summary = result.get("memory_echo", "")
        unlocked_form = result.get("mirror_forms", [])[-1] if result.get("mirror_forms") else ""
        seed_data = result.get("origin_data", None)

        return render_template("index.html",
                               poetic_response=poetic_response,
                               tone=tone,
                               motive=motive,
                               elements=elements,
                               gate_number=gate_number,
                               gate_name=gate_name,
                               equation=equation,
                               memory_summary=memory_summary,
                               unlocked_form=unlocked_form,
                               seed=seed_data)
    return render_template("spiral.html")



@app.route("/journal")
def journal():
    entries = load_all_journals()
    return render_template("journal.html", entries=entries)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

