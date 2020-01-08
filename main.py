import csv
import sys

Contacts = {}


class Contact:
    def __init__(self, Name, Phone, Email, Occupation):
        self.Name = Name
        self.Phone = Phone
        self.Email = Email
        self.Occupation = Occupation

    def __str__(self):
        return 'Name: ' + self.Name + '\n' + 'Phone: ' + str(
            self.Phone) + '\n' + 'Email: ' + self.Email + '\n' + 'Occupation: ' + self.Occupation + '\n'


def PrintContacts():
    if Contacts:
        for Name in Contacts:
            print(Contacts[Name])
    else:
        print('Contact list is empty\n')


def AddContact():
    print('Name?')
    name_str = sys.stdin.readline().strip()

    print('Phone?')
    phone_str = sys.stdin.readline().strip()
    try:
        phone_int = int(phone_str)
    except ValueError:
        print('Invalid phone number')
        return

    print('Email?')
    email_str = sys.stdin.readline().strip()

    print('occupation?')
    occ_str = sys.stdin.readline().strip()

    Contacts[name_str] = Contact(name_str, phone_int, email_str, occ_str)


def FindContact():
    if Contacts:
        print('Name of contact?')
        input_str = sys.stdin.readline().strip().casefold()

        if input_str in Contacts:
            print(Contacts[input_str])
            return Contacts[input_str]
        else:
            print('Contact not found\n')

    else:
        print('Contact list is empty\n')


def SaveContacts():
    if Contacts:
        print('Name of new file?\n')
        filename = sys.stdin.readline().strip().casefold()
        try:
            with open(filename, 'w', newline='') as csvfile:
                for Name in Contacts:
                    writer = csv.writer(csvfile)
                    writer.writerow([Name, Contacts[Name].Phone, Contacts[Name].Email, Contacts[Name].Occupation])

            # with open(filename, 'w') as fp:
            #     for Name in Contacts:
            #         fp.write(Name + ',' + str(Contacts[Name].Phone) + ',' + Contacts[Name].Email + ',' + Contacts[
            #             Name].Occupation + '\n')

        except FileNotFoundError:
            print("Saving file failed\n")
    else:
        print('Contact list is empty\n')


def LoadContacts():
    print('Name of file to load?')
    filename = sys.stdin.readline().strip().casefold()
    load_count = 0

    try:
        global Contacts
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                Contacts[row[0]] = Contact(row[0], int(row[1]), row[2], row[3])
                load_count += 1
            print('Number of contacts loaded: {}\n'.format(load_count))

        # with open(filename) as fp:
        #     line = fp.readline()
        #     while line:
        #         line = line.split(',')
        #         Contacts[line[0]] = Contact(line[0], int(line[1]), line[2], line[3])
        #         line = fp.readline()
        #         load_count += 1
        # print('Number of contacts loaded: {}\n'.format(load_count))

    except FileNotFoundError:
        print("File not found\n")


def DeleteContact():
    res = FindContact()

    if not res:
        return
    else:
        name = res.Name
        del Contacts[name]
        print(name + ' was deleted\n')


def DeleteAllContacts():
    if Contacts:
        Contacts.clear()
        print('All contacts deleted\n')
    else:
        print('Contact list is empty\n')


def EditContact():
    # Backing up the old contact
    contact_edit = FindContact()
    old_name = contact_edit.Name

    # If not found, exit
    if not contact_edit:
        return

    # Else do the editing
    else:
        # Nested functions -- just for editing!!
        def EditName():
            print('New name?')
            new_name = sys.stdin.readline().strip()
            contact_edit.Name = new_name
            # Change the key to new name
            Contacts[new_name] = contact_edit
            del Contacts[old_name]

        def EditPhone():
            print('New phone?')
            new_phone = sys.stdin.readline().strip()
            try:
                new_phone_int = int(new_phone)
            except ValueError:
                print('Invalid phone number')
                return
            contact_edit.Phone = new_phone_int

        def EditEmail():
            print('New email?')
            new_email = sys.stdin.readline().strip()
            contact_edit.Email = new_email

        def EditOccupation():
            print('New occupation?')
            new_occ = sys.stdin.readline().strip()
            contact_edit.Occupation = new_occ

        EditCommands = {
            'name': EditName,
            'phone': EditPhone,
            'email': EditEmail,
            'occupation': EditOccupation
        }

        print('\nEdit what?')
        edit_command = sys.stdin.readline().strip().casefold()

        if edit_command in EditCommands:
            EditCommands[edit_command]()

        else:
            print('Invalid edit command\n')


# Do not add () at the end of the function names!!!!
CommandList = {
    'print': PrintContacts,
    'add': AddContact,
    'edit': EditContact,
    'find': FindContact,
    'save': SaveContacts,
    'load': LoadContacts,
    'delete': DeleteContact,
    'delete-all': DeleteAllContacts,
    'quit': quit
}

CommandDescr = {
    'print': 'Print all contacts on screen',
    'add': 'Add new contact',
    'edit': 'Edit existing contact',
    'find': 'Find contact by name',
    'save': 'Save contact list to CSV',
    'load': 'Load contact list from CSV',
    'delete': 'Delete a contact',
    'delete-all': 'Delete all contacts',
    'quit': 'Quit program'
}


def UserInterface():
    while True:
        print('Command list:')
        for command in CommandList:
            print(command + ': ' + CommandDescr[command])

        print('\nCommand? ')
        command = sys.stdin.readline().strip().casefold()

        if command in CommandList:
            CommandList[command]()

        else:
            print('Invalid command\n')


UserInterface()
