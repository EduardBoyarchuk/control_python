import csv
import os

NOTES_FILE = "notes.csv"


def read_notes():
    notes = []
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r", newline="") as file:
            reader = csv.reader(file, delimiter=";")
            for row in reader:
                notes.append(row)
    return notes


def add_notes(notes):
    save_notes(notes)
    print("Заметка добавлена.")


def save_notes(notes):
    with open(NOTES_FILE, "w", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(notes)


def list_notes():
    notes = read_notes()
    if not notes:
        print("Список заметок пуст.")
    else:
        print("Список заметок:")
        for note in notes:
            print(f"ID: {note[0]}, Заголовок: {note[1]}, Дата: {note[3]}, Суть заметки: {note[2]}")


def edit_note():
    notes = read_notes()
    list_notes()
    note_id = int(input("Введите ID заметки для редактирования: "))
    if 1 <= note_id <= len(notes):
        new_title = input("Введите новый заголовок: ")
        new_body = input("Введите новую суть заметки: ")
        notes[note_id - 1][1] = new_title
        notes[note_id - 1][2] = new_body
        save_notes(notes)
        print("Заметка отредактирована.")
    else:
        print("Неверный ID заметки.")


def delete_note():
    notes = read_notes()
    list_notes()
    note_id = int(input("Введите ID заметки для удаления: "))
    if 1 <= note_id <= len(notes):
        del notes[note_id - 1]
        save_notes(notes)
        print("Заметка удалена.")
    else:
        print("Неверный ID заметки.")
