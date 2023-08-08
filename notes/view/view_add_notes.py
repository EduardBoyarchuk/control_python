import presenter.add_notes as p_add


def view_add_notes():
    title = input("Введите заголовок заметки")
    body = ("Введите суть заметки")
    p_add.add_notes(title, body)
