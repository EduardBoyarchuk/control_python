import View.view_add_notes as v
# import Model.read_notes, Model.add_notes
from Model import  add_notes

def add_notes(title, body):
    add_notes.add_notes(title, body)
