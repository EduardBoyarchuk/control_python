

from read_notes import *

def save_notes(notes):
    with open(NOTES_FILE, "w", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(notes)
