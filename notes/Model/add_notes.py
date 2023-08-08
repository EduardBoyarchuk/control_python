from datetime import datetime

import  Model.read_notes
import  Model.save_notes

def add_notes(title, body):
    notes = Model.read_notes.read_notes()
    note_id = len(notes) + 1
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_note = [str(note_id), title, body, timestamp]
    notes.append(new_note)
    Model.save_notes.save_notes(notes)
