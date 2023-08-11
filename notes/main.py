import View.work_with_the_user as View
from notes.Model.working_with_files import edit_note, delete_note

def print_hi():
    print(f'Hi, Я рад Вас приветствовать, приступаем:')
    print()


def menu():
    while True:
        print('1. Добавить заметку')
        print('2. Просмотр заметок')
        print('3. Редактирование заметок')
        print('4. Удаление заметки')
        print('0. Выход')

        choice = input("Выберите действие  :   ")
        print()

        if choice == '1':
            View.create_notes()
        elif choice == '2':
            View.list_all_notes()
        elif choice == '3':
            edit_note()
        elif choice == '4':
            delete_note()
        elif choice == '0':
            print("До встречи")
            break
        else:
            print("Неверный выбор.")


if __name__ == '__main__':
    print_hi()
    menu()
