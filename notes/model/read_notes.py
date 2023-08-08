import csv
import os.path

NOTES_FILE = "notes.csv"

def read_notes():
    notes = []
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r", newline="") as file:
            reader = csv.reader(file, delimiter=";")
            for row in reader:
                notes.append(row)
    return notes
 