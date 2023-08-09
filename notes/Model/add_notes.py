from datetime import datetime
from notes.Model.read_notes import read_notes
from notes.Model.save_notes import save_notes

def add_notes(title, body):
    notes = read_notes()
    note_id = len(notes) + 1
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_note = [str(note_id), title, body, timestamp]
    notes.append(new_note)
    save_notes(notes)
