import view.view_add_notes as v
import model.read_notes, model.add_notes


def add_notes(title, body):
    model.add_notes.add_notes(title, body)
