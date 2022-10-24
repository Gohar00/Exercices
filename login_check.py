def get_content(fname):
    with open(fname) as f:
        return f.readlines()
def create_users_dict(ml):
    users_dict = {}
    for users in ml:
        name, passw = users.strip().split(":")
        users_dict[name] = passw
    return users_dict
def unique_username(users_dict):
    username = input("Enter your username please: ")
    while username in users_dict:
        print("Such username exists. Please enter a new one: ")
        username = input("Enter your username please: ")
    return username
def get_passw():
    print("The password should be:\n"
          ">= 8\n"
          "have 2 char of --> '@', '$', '#', '!'\n"
          "have 2 number\n")
    password = input("Enter your password: ")
    char = ['@', '$', '#', '!']
    count_alpha = 0
    count_number = 0
    while len(password) <= 8 or count_number != 2 or count_alpha != 2:
        count_alpha = 0
        count_number = 0
        print("The password should be:\n"
              ">= 8\n"
              "have 2 char of --> '@', '$', '#', '!'\n"
              "have 2 number\n")
        password = input("Enter your password: ")
        for i in password:
            if i.isdigit():
                count_number += 1
            elif i in char:
                count_alpha += 1
    else:
        confirm_password = input("Enter your password again: ")
        while confirm_password != password:
            print("Your passwords should be matched.")
            confirm_password = input("Enter your password again: ")
    return password
def register(users_dict,fname):
    username = unique_username(users_dict)
    password = get_passw()
    with open(fname,'a') as f:
        f.write(f'{username}:{password}\n')
    print("You have been successfully added.")
def ask_register(users_dict,fname):
    answ = input("Would you like to register? y/n: ")
    if answ.lower() == "y":
        register(users_dict,fname)
    else:
        print("ok,Bye!")
def main():
    fname = 'users.txt'
    user = get_content(fname)
    users_dict = create_users_dict(user)
    uname = input("Enter your username: ")
    if uname in users_dict:
        passw = input("Enter your password: ")
        if users_dict[uname] == passw:
            print(f'Hi {uname}')
        else:
            print("Your password is wrong!!!")
            ask_register(users_dict, fname)
    else:
        ask_register(users_dict, fname)
main()



