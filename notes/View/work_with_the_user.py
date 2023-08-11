
from datetime import datetime
from notes.Model.working_with_files import read_notes, add_notes
notes = list()

def create_notes():
    title = input("Введите заголовок заметки: ")
    body = input("Введите суть заметки: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    notes.append([str(len(read_notes()) + 1), title, body, timestamp])

    add_notes(notes)



def list_all_notes():
    notes = read_notes()
    if not notes:
        print("Список заметок пуст.")
    else:
        print("Список заметок:")
        for note in notes:
            print(f"ID: {note[0]}, Заголовок: {note[1]}, Дата: {note[3]}, Суть заметки: {note[2]}")
