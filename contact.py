from printer import print_status, print_all_contact

def add_contact(contacts: list[dict]):
    first_name = input("first name: ").isalpha()
    last_name = input("last name: ").isalpha()
    phone = input("phone: ").isdigit()
    group = input("group (family, friend, work, other): ").isalpha()

    contacts.append({
        "first_name": first_name,
        "last_name": last_name,
        "phone": phone,
        "group": group,
    })

    print_status('success')

def show_all_contact(contacts: list[dict]):

    if contacts:
        print_all_contact(contacts)
    else:
        print_status('error')

def search_contact():
    name = input("Ismni kiriting!: ").isalpha()
    last = input("Familiyani kiriting!: ").isalpha()
    
    result = map(
        lambda contacts: add_contact['first_name'] == name and add_contact['last_name'] == last,
        add_contact()
    )
    return result

def delete_contact():
    pass

def update_contact():
    pass


