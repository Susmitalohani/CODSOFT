'''Contact Book that : store name, phone number, email, and address for each contact.'''
import re
# Declare contact book to be empty
CONTACT = []
def display_menu():
    '''displays action on contact book'''
    print('1. Add Contact')
    print('2. View Contact')
    print('3. Search Contact')
    print('4. Update Contact')
    print('5. Delete Contact')
    print('6. Exit')
    print()

def add_contact():
    '''Allows user to add contact to book'''
    while True:
        try:
            new_contact = []
            name = input('Enter name : ')
            number = input('Enter phone number : ')
            email = input('Enter email address : ')
            address = input('Enter shipping address : ')
            name_validation(name)
            number_validation(number)
            email_validation(email)
            new_contact.append(name)
            new_contact.append(number)
            new_contact.append(address)
            new_contact.append(email)
            CONTACT.append(new_contact)
            print('Record added successfully.')
            break
        except ValueError as err:
            print(f'error : {err}')

def view_contact():
    '''Allows user to view all contacts in book'''
    print('S.N.\t|\tName\t\t|\tNumber\t\t\t|\taddress\t\t|\temail')
    count = 1
    for each_contact in CONTACT:
        print(f'{count}.',end='\t|\t')
        for field in each_contact:
            print(f'{field}',end='\t\t|\t')
        count += 1
        print()
def search_contact():
    '''Allows user to add contact to book'''
    search_by = search_option()
    if search_by == 'name':
        try:
            search_name = input('Enter name to search : ')
            not_found = True
            for record in CONTACT:
                if record[0] == search_name:
                    print_record(record)
                    not_found = False
                    break
            if not_found:
                print('Record not found.')
        except ValueError as err:
            print(f'error : {err}')
    else: #search by == number
        try:
            search_number = input('Enter contact number to search : ')
            number_validation(search_number)
            not_found = True
            for record in CONTACT:
                if record[1] == search_number:
                    print_record(record)
                    not_found = False
                    break
            if not_found:
                print('Record not found.')
        except ValueError as err:
            print(f'error : {err}')

def update_contact():
    '''Allows user to update contact details in book'''
    try:
        update_number = input('Enter number to edit contact details : ')
        number_validation(update_number)
        not_found = True
        for record in CONTACT:
            if record[1] == update_number:
                print_record(record)
                remove_contact(record[1])
                add_contact()
                not_found = False
                print('Record Updated successfully.')
                break
        if not_found:
            print('No record with corresponding contact number')
    except ValueError as err:
        print(f'error : {err}')

def delete_contact():
    '''Allows user to delete contact details in book'''
    try:
        delete_number = input('Enter number to delete contact details :')
        number_validation(delete_number)
        not_found = True
        for record in CONTACT:
            if record[1] == delete_number:
                not_found = False
                print_record(record)
                while True:
                    delete_confirm = input('Once removed, cannot be recovered,\
                                           Are you sure to remove (Y|N) : ')
                    if delete_confirm.lower() == 'y':
                        remove_contact(record[1])
                        print('Record deleted successfully.')
                        break
                    if delete_confirm.lower() == 'n':
                        print('Record was not deleted.')
                        break
                    print('error : invalid input => Choose y or n')
        if not_found:
            print('Record not found.')
    except ValueError as err:
        print(f'error : {err}')

def remove_contact(remove_number):
    '''Removes contact details corresponding to number'''
    for index,record in enumerate(CONTACT):
        if record[1] == remove_number:
            del CONTACT[index]

def name_validation(check_string):
    '''Checks if given string contains special characters'''
    special_char = "!@#$%^&*()_:;',.<>/?"
    for char in check_string:
        if char in special_char:
            raise ValueError('Name contains special characters')
    if check_string.isdigit():
        raise ValueError('Name contains integers')
    if check_string=="":
        raise ValueError('Name cannot be empty.')

def number_validation(check_number):
    '''Checks if given number is correct format'''
    if not check_number.isdigit():
        raise ValueError('Contact number cannot contain character other than integers.')
    if len(check_number) != 10:
        raise ValueError('Invalid length of contact number')

def email_validation(check_email):
    '''Checks if given email is correct form'''
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    correct = re.match(pattern, check_email)
    if not correct:
        raise ValueError('Invalid email format.')

def search_option():
    '''Prompts user to input what to search by'''
    while True:
        choice = input('Search by 1. Name or 2. Contact Number (1 or 2) : ')
        if choice.lower() == '1':
            return 'name'
        if choice.lower() == '2':
            return 'number'
        print('error : invalid input => Please choose 1 or 2.')

def print_record(record):
    '''prints selected record list'''
    print('Record found')
    print(f'Name => {record[0]}')
    print(f'Contact Number => {record[1]}')
    print(f'Address => {record[2]}')
    print(f'Email => {record[3]}')
    print()

def main():
    '''Assembles all other funcitons'''
    while True:
        display_menu()
        try:
            menu_option = int(input('Choose an option: '))
            if menu_option not in range(1,7):
                raise ValueError
            if menu_option == 1:
                add_contact()
            elif menu_option == 2:
                view_contact()
            elif menu_option == 3:
                search_contact()
            elif menu_option == 4:
                update_contact()
            elif menu_option == 5:
                delete_contact()
            else:
                break
            print()
        except ValueError:
            print('Please enter a valid integer option (1-5).')

print('---Welcome to Contact Book Directory---')
main()