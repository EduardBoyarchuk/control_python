
import View.view_add_notes as v

def menu():
    with True:
        print('1. Добавить заметку')
        print('2. Просмотр заметок')
        print('3. Редактирование заметок')
        print('4. Удаление заметки')
        print('0. Выход')

        choice = input("Выберите действие")

        if choice == '1':
            v.view_add_notes()
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '0':
            pass