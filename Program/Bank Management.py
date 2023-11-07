import os
import time
from datetime import date
from playsound import playsound
import turtle


# creating a class customer and creating necessary variables/attributes
class customer:
    name = str
    dob = str
    phone_no = str
    password = str
    confirm_password = str
    account_no = str
    date_of_account_creation = date.today()
    account_type = str
    username = str

    # this function collects all the data from user
    def set_data(self):

        print("Enter your name :")
        playsound("Enter your name.mp3")
        self.name = input()

        print("Enter your date of birth :")
        playsound("Enter your date of birth.mp3")
        self.dob = input()

        print("Enter your phone number :")
        playsound("Enter your phone number.mp3")
        self.phone_no = input()

        # this function is for checking the length of phone no and re enter if invalid
        if len(self.phone_no) != 10:
            while len(self.phone_no) != 10:

                print(" please enter a valid  phone no of 10 digits:\n")
                playsound("please enter a valid  phone no of 10 digits.mp3")
                self.phone_no = input()

        print('''Please specify the type of account you want to open :
        1. Saving account
        2. Current account''')
        playsound("Please specify the type of account you want to open.mp3")

        # temporary variable used to store the choice of user for account creation
        temp = input()

        while True:
            if temp == "1":
                self.account_type = "saving"
                print("Your account type has been set to saving account")
                break

            elif temp == "2":
                self.account_type = "current"
                print("Your account type has been set to current account")
                break

            else:
                print("please choose valid option")
                playsound("please choose valid option.mp3")

        self.username = input(f"""Please choose a unique username for you :
        (NOTE : 1. username should not contain white spaces
                2. It should not contain only numbers || use of alphanumeric username is allowed\n""")

        # checking if the username is available and valid
        while check_username(self.username):
            self.username = input()

        # getting values from user
        print("Enter your password")
        playsound("Enter your password.mp3")
        self.password = input()

        print("Renter your password to confirm")
        playsound("Renter your password to confirm.mp3")
        self.confirm_password = input()

        # checking the validity of confirm_password
        if self.password != self.confirm_password or len(self.password) < 6:
            while self.password != self.confirm_password or len(self.password) < 6:
                if len(self.password) < 6:
                    print("password requirement is minimum 6 characters ")

                else:
                    print("Your both the passwords do not match please try again !!!\n")

                print("Enter your confirm_password")
                playsound("Enter your password.mp3")
                self.password = input()

                print("Renter your password to confirm\n")
                playsound("Renter your password to confirm.mp3")
                self.confirm_password = input()

        self.create_account()

    # this fnction stores all the details of the user in "customer details" file
    def create_account(self):

        customer_details_file = open("customer details", "a")
        customer_balance = open("customer total balance", "a")

        self.account_no = generate_account_no()

        # The account will be stored in 3 index and password in 4 index
        # name = 0
        # date of birth = 1
        # phone no = 2
        # account number = 3
        # password = 4
        # acc creation date = 5
        # account type = 6
        # username = 7


        customer_details_file.write(
            f"{self.name}@{self.dob}@{self.phone_no}@{self.account_no}@{self.password}@{self.date_of_account_creation}@{self.account_type}@{self.username}@\n")
        customer_balance.write(f"{self.account_no}@{self.username}@{0}@\n")

        print("Your account has been created successfully and your account no is :", self.account_no)
        playsound("Your account has been created succesfully.mp3")
        customer_details_file.close()


def generate_account_no():
    customer_data = open("customer details")
    account_no = 1
    while customer_data.readline() != "":
        account_no += 1

    customer_data.close()
    return account_no


def check_username(username):
    file = open("customer details")
    file_string = file.readline()

    if username.isnumeric():
        return True

    while file_string != "":

        file_list = file_string.split("@")
        if file_list[7] == username:
            file.close()

            print("username has been already used please try with another username")
            playsound("username has been already used please try with another username.mp3")
            return True
        file_string = file.readline()

    file.close()
    return False


def check_login(username, password):
    user_details = open("customer details")
    user_details_string = user_details.readline()

    while user_details_string != "":
        user_details_list = user_details_string.split("@")

        if user_details_list[7] == username or user_details_list[3] == username:

            if user_details_list[4] == password:

                print("You are logged in.....")
                playsound("You are logged in.mp3")
                return True
            else:
                print("username doesnt exist First create a account an try again later")

        user_details_string = user_details.readline()

    user_details.close()

    print("Invalid password please try again")
    playsound("Invalid password please try again.mp3")

    return False


def see_customer_details(username, password):
    user_details = open("customer details")
    user_details_string = user_details.readline()

    while user_details_string != "":
        user_details_list = user_details_string.split("@")

        if user_details_list[7] == username or user_details_list[3] == username:
            print(f'''name : {user_details_list[0]}
date of birth : {user_details_list[1]}
phone no : {user_details_list[2]}
account number : {user_details_list[3]}
acc creation date : {user_details_list[5]}
account type : {user_details_list[6]}
''')
        user_details_string = user_details.readline()


def see_total_balance(username):
    user_details = open("customer total balance")
    user_details_string = user_details.readline()

    while user_details_string != "":
        user_details_list = user_details_string.split("@")

        if user_details_list[0] == username or user_details_list[1] == username:
            print(f"your total account balance is : {user_details_list[2]} rs ")

        user_details_string = user_details.readline()

    user_details.close()


def withdraw_deposits(username, amount, action):
    current_date = date.today()
    current_time = time.strftime("%H:%M:%S", time.localtime())

    withdraw_deposit = open("withdraw deposit records", "a")
    total_balance = open("customer total balance")
    raw_file = open("raw balance file", "a")

    total_balance_string = total_balance.readline()

    while total_balance_string != "":
        total_balance_list = total_balance_string.split("@")

        if total_balance_list[0] == username or total_balance_list[1] == username:

            if action == "w":
                new_total_balance = (float(total_balance_list[2])) - amount

            elif action == "d":
                new_total_balance = (float(total_balance_list[2])) + amount

            withdraw_deposit.write(f"{username}@{action}@{amount}@{current_date}@{current_time}@\n")
            total_balance_list[2] = str(new_total_balance)
            raw_file.write(f"{total_balance_list[0]}@{total_balance_list[1]}@{total_balance_list[2]}@\n")

        else:
            raw_file.write(total_balance_string)

        total_balance_string = total_balance.readline()

    withdraw_deposit.close()
    total_balance.close()
    raw_file.close()

    os.remove("customer total balance")
    os.renames("raw balance file", "customer total balance")


def update_details(field_to_be_updated, index_no):

    user_details = open("customer details")
    raw_file = open("raw file", "a")
    user_details_string = user_details.readline()

    if index_no == 4  :
        if not check_username(field_to_be_updated) :
            return

    while user_details_string != "":
        user_details_list = user_details_string.split("@")

        if user_details_list[3] == username or user_details_list[7] == username:
            user_details_list[index_no] = field_to_be_updated
            raw_file.write(
                f"{user_details_list[0]}@{user_details_list[1]}@{user_details_list[2]}@{user_details_list[3]}@{user_details_list[4]}@{user_details_list[5]}@{user_details_list[6]}@{user_details_list[7]}@\n")

        else:
            raw_file.write(user_details_string)

        user_details_string = user_details.readline()

        user_details.close()
        raw_file.close()

        os.remove("customer details")
        os.renames("raw file", "customer details")

        print("details Updated successfully")
        playsound("Transaction tune.mp3")
        playsound("Transaction successful.mp3")


def create_all_files():
    file1 = open("customer details", "a")
    file2 = open("customer total balance", "a")
    file3 = open("withdraw deposit records", "a")
    file4 = open("raw balance file", "a")

    file1.close()
    file2.close()
    file3.close()
    file4.close()

def show_animation() :

    a = turtle.Turtle()

    a.speed(0.23)
    turtle.bgcolor("black")
    a.width = 10

    for i in range(200) :
        a.color("cyan")
        a.circle(i)
        a.left(7)

    turtle.done()

# *******************************************************************************************************************************************************
# Starting of Main program

# show_animation()
print("Welcome to Bank Management")
playsound("Welcome to Bank Management.mp3")
create_all_files()

while True:

    temp = input("please press any key to continue\n")


    print(f'''Please select your choice 
        1. create a new customer account
        2. login to existing customer account
        NOTE : Enter "0" or "@" To Exit''')
    playsound("Please select your choice .mp3")

    choice = input()

    if choice == "1":

        customer1 = customer()
        customer1.set_data()

        del customer1

    elif choice == "2":

        print("Please enter your username or account no")
        playsound("Please enter your username or account no.mp3")
        username = input()

        print("Please enter your password")
        playsound("Enter your password.mp3")
        password = input()

        if check_login(username, password):

            temp = input("please press any key to continue")

            while True:

                print(f"""Please enter your choice :
                1. see you details"
                2. see total balance"
                3. withdraw money"
                4. deposit money"
                5. transfer money"
                6. change password"
                7. update details
      NOTE : Enter "0" or "@" To Exit""")
                playsound("Please select your choice .mp3")

                choice1 = input()

                if choice1 == "1":
                    see_customer_details(username, password)

                elif choice1 == "2":
                    see_total_balance(username)

                elif choice1 == "3":

                    current_date = date.today()
                    current_time = time.strftime("%H:%M:%S", time.localtime())

                    print("please enter your amount to be withdrawn :")
                    playsound("please enter your amount.mp3")
                    withdrwal_amount = float(input())
                    withdraw_deposits(username, withdrwal_amount, "w")

                    print(f"Transaction successful on "
                          f"date :{current_date} \t"
                          f"time :{current_time}")

                    playsound("Transaction tune.mp3")
                    playsound("Transaction successful.mp3")
                    see_total_balance(username)

                elif choice1 == "4":

                    current_date = date.today()
                    current_time = time.strftime("%H:%M:%S", time.localtime())

                    print("please enter your amount to be deposited :")
                    playsound("please enter your amount.mp3")
                    deposit_amount = float(input())
                    withdraw_deposits(username, deposit_amount, "d")

                    print(f"Transaction successful on "
                          f"date :{current_date} \t"
                          f"time :{current_time}")
                    playsound("Transaction tune.mp3")
                    playsound("Transaction successful.mp3")
                    see_total_balance(username)

                elif choice1 == "5":

                    current_date = date.today()
                    current_time = time.strftime("%H:%M:%S", time.localtime())
                    reveiver_account_no = input("please enter the account no of the receiver :\n")

                    print("Please enter the amount you want to transfer :")
                    playsound("please enter your amount.mp3")
                    transaction_amount = float(input())

                    print("please re enter your password to confirm trasaction ")
                    playsound("Renter your password to confirm.mp3")
                    transaction_password = input()

                    if transaction_password == password:
                        withdraw_deposits(username, transaction_amount, "w")
                        withdraw_deposits(reveiver_account_no, transaction_amount, "d")

                    playsound("Transaction successful.mp3")
                    print(f"Transaction successful on "
                          f"date :{current_date} \t"
                          f"time :{current_time}")
                    playsound("Transaction tune.mp3")
                    see_total_balance(username)

                elif choice1 == "6":

                    print("please re enter your password to confirm :")
                    playsound("Renter your password to confirm.mp3")
                    confirm_password = input()

                    if confirm_password == password:
                        update_details(password, 4)

                    else:
                        print("password mismatch")
                        playsound("Invalid password please try again.mp3")

                elif choice1 == "7":
                    print(f'''Please enter which details do you want to update 
1. name
2. date of birth
3. phone number
4. change username
NOTE : Enter "0" or "@" To Exit''')

                    choice2 = input()
                    index_no = int

                    if choice2 == "1":
                        index_no = 0

                    elif choice2 == "2":
                        index_no = 1

                    elif choice2 == "3":
                        index_no = 2

                    elif choice2 == "4":
                        index_no = 7

                    else:
                        print("please enter a valid choice")
                        playsound("please choose valid option.mp3")

                    updated_value = input("please enter the updated value :\n")
                    update_details(updated_value, index_no)

                elif choice1 == "0" or choice1 == "@":
                    break

                else:
                    print("please choose a valid option")
                    playsound("please choose valid option.mp3")

    elif choice == "0" or choice == "@":
        break

    else:
        print("please enter a valid choice")
        playsound("please choose valid option.mp3")