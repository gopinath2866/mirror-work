# journal_saver.py
import json
import os
from datetime import datetime

def save_to_journal(entry, journal_dir="mirror_journal"):
    os.makedirs(journal_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{journal_dir}/reflection_{timestamp}.json"

    with open(filename, "w") as f:
        json.dump(entry, f, indent=4)

    return filename

# Example usage:
# save_to_journal({"user_input": "I feel lost", "tone": "sad"})
import os
import json

def load_all_journals():
    journal_dir = "mirror_journal"
    entries = []
    if not os.path.exists(journal_dir):
        return entries

    files = sorted(os.listdir(journal_dir))
    for file in files:
        if file.endswith(".json"):
            with open(os.path.join(journal_dir, file), "r") as f:
                try:
                    entry = json.load(f)
                    entries.append(entry)
                except Exception as e:
                    print(f"⚠️ Error loading journal entry: {file} — {e}")
    return entries
