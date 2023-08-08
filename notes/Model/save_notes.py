import csv
from Model import read_notes
# from read_notes import read_notes,NOTES_FILE
NOTES_FILE = "notes.csv"
def save_notes(notes):
    with open(NOTES_FILE, "w", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(notes)
