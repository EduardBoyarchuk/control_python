from notes.View.view_add_notes import view_add_notes

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
def menu():
    while True:
        print('1. Добавить заметку')
        print('2. Просмотр заметок')
        print('3. Редактирование заметок')
        print('4. Удаление заметки')
        print('0. Выход')

        choice = input("Выберите действие")

        if choice == '1':
            view_add_notes()
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '0':
            print("До встречи")
            break


if __name__ == '__main__':
    print_hi("Hi,Hu")
    menu()

