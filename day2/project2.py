contacts = []


def Home():
    name = input("Enter Name : ")
    number = input("Enter number : ")
    contacts.append((name, number))

    def save_contact():
        with open("contactlist.txt", "a") as file:   
            file.write(f"| {name} {number}\n")

    save_contact()


def read_contacts():
    try:
        with open("contactlist.txt", "r") as file:  
            data = file.read()
            print("\nSaved Contacts")
            print(data)
    except FileNotFoundError:
        print("No contacts found yet!")


def delete_contact():
    name_to_delete = input("Enter the name you want to delete : ")

    try:
        with open("contactlist.txt", "r") as file:   
            lines = file.readlines()

        found = False
        new_data = []

        for line in lines:
            parts = line.strip().split(" ")
            if len(parts) >= 3:
                name = parts[1]
                if name.lower() != name_to_delete.lower():
                    new_data.append(line)
                else:
                    found = True

        if found:
            with open("contactlist.txt", "w") as file:   
                file.writelines(new_data)
            print("Contact Deleted Successfully!")
        else:
            print("Contact Not Found!")

    except FileNotFoundError:
        print("contactlist.txt not found!")



while True:
    print("\nContact Systems")
    print(" 01. Add \n 02. Read \n 03. Delete \n 04. Exit ")

    opt = input("Select the options : ")

    if opt == '1':
        Home()
    elif opt == '2':
        read_contacts()
    elif opt == '3':
        delete_contact()
    elif opt == '4':
        print("Exiting...")
        break
    else:
        print("please choose the correct option..")

