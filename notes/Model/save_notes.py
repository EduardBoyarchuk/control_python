import csv
#from notes.Model.read_notes import read_notes, NOTES_FILE
from .read_notes import read_notes, NOTES_FILE

def save_notes(notes):
    with open(NOTES_FILE, "w", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(notes)
