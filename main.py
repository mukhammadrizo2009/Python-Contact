from sys import exit
from printer import print_menu
from contact import add_contact, show_all_contact
from contact import search_contact
from contact import delete_contact
from contact import update_contact

def main():
    contacts: list[dict] = [
        {"first_name": 'ali', 'last_name': 'valiyev', 'phone': '3241234123', "group": 'other'}
    ]
    
    while True:
        print_menu()

        choice = input("Menu tanlang: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            show_all_contact(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            update_contact(contacts)
        else:
            exit(0)

if __name__ == "__main__":
    main()
