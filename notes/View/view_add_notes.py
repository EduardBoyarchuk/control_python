#from notes.Presenter.add_notes import add_notes
from notes.Model.add_notes import add_notes


def view_add_notes():
    title = input("Введите заголовок заметки")
    body = input("Введите суть заметки")
    add_notes(title, body)
