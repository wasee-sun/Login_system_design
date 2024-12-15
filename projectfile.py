from abc import ABC, abstractmethod
from datetime import datetime
import string, random

# Project file --> https://docs.google.com/document/d/1IAz6B8OqGH4TRDU9wweMyp4NkPwDv3D4Q1W-eRVA6Jk/edit
# Created by Sultan Wasee Uddin Sun
class Account(ABC):
    # Data of courses
    course_dict = {"1st" : ["ENG091", "CSE110", "MAT110", "PHY111", "CSE101"], 
                   "2nd" : ["ENG101", "CSE111", "CSE230", "CSE260", "MAT120", "BUS102", "PHY112"],
                   "3rd" : ["ENG102", "BNG101", "DEV101", "HUM103"],
                   "4th" : ["MAT215", "CSE220", "CSE340", "CSE330", "CSE370", "CSE321", "CSE331"],
                   "5th" : ["CSE221", "CSE340", "CSE470", "CSE423", "CSE421", "CSE420"]}
    # Main data dict of student and stuff (private variable)
    __data_dict = {"student_dict" : {"waseesun": {"First name" : "Wasee", "Last name": "Sun", "Email" : "waseesun@gmail.com", "Password": "110010111100101110100011001101101000100001100000010110010110111", "ID" : "22241010", "DOB": "01/11/2002", "Gender" : "Male", "Semester" : "1st", "course_info" : ["ENG091", "CSE110", "MAT110", "PHY111"]}, #ert34!@Y
                 "jeremyroman69": {"First name" : "Jeremy", "Last name": "Roman", "Email" : "jeremyroman@gmail.com", "Password": "100111011011110100001110001111001010110110011100111000100110110", "ID" : "22299101", "DOB": "23/02/2002", "Gender" : "Male", "Semester" : "4th", "course_info" : ["MAT215", "CSE220", "CSE340", "CSE330"]},
                 "ronan420": {"First name" : "Howard", "Last name": "Ronan", "Email" : "ronanhoward@gmail.com", "Password": "10000100100001111010011000111101000010010101101100111001011100101101100110101", "ID" : "22200099", "DOB": "23/07/2003", "Gender" : "Male", "Semester" : "2nd", "course_info" : ["CSE221", "CSE340", "CSE470", "CSE420"]}}, 
                 "staff_dict" : {"tanvirarafat": {"First name" : "Tanvir", "Last name": "Arafat", "Email" : "tanvirarafat@gmail.com", "Password": "110011111010000110010011001101110000100001100100010010111110101110100111001110110111", "DOB": "19/06/1990", "Gender" : "Male", "Dept" : "CSE"}, #BestS!R1
                 "rumana120": {"First name" : "Rumana", "Last name": "Haque", "Email" : "haquerumana@gmail.com", "Password": "100111011011110100001110001111001010110110011100111000100110110", "DOB": "12/12/1984", "Gender" : "Female", "Dept" : "EEE"},
                 "alikarim90": {"First name" : "Ali", "Last name": "Karim", "Email" : "karimali@gmail.com", "Password": "10000100100001111010011000111101000010010101101100111001011100101101100110101", "DOB": "30/03/1990", "Gender" : "Male", "Dept" : "BBA"}}}
        
    def get_data_dict():
        return Account.__data_dict
    
    def get_account(user_name, diction):
        # checking where the account is
        if diction == "student_dict": # for student dict
            # creating the object
            user = StudentAccount(user_name, diction)
        elif diction == "staff_dict": # for staff dict
            user = StaffAccount(user_name, diction)
        return user
                
    # checking whether profile completion is correctly done
    def set_profile(type):
        while True:
            if type == "user_name":
                user_name = input("Give a username (Atleast 4 letters): ")
                data_dict = Account.get_data_dict()
                # checking if the username already exists
                if user_name in (data_dict["student_dict"].keys() or data_dict["staff_dict"].keys()):
                    print("Username not available please choose another: ")
                # username must be 4 or more letters
                elif len(user_name) < 4:
                    print("Username must be more than 4 letters")
                else:
                    return user_name
            elif type == "password":
                password = input("Give a password (Atleast 8 letters, must contain upper,lower,digit and special characters): ")
                c_password = Account.set_pass(password)
                if c_password == False:
                    continue
                return c_password
            elif type == "email":
                email = input("Email id: ")
                # checking if @gmail.com is in the email
                if "@gmail.com" not in email:
                    print("Invalid email, must have @gmail.com in the end")
                else:
                    return email
            elif type == "id":
                # choosing date
                ID = input("Enter your student ID: ")
                # checking if ID is only digits and is of 8 digit
                if ID.isdigit() and len(ID) == 8:
                    return ID
                else:
                    print("Student ID must be 8 digits")
            elif type == "dob":
                # choosing date of birth
                dob = input("Enter your date of birth (format DD/MM/YYYY): ")
                # trying if the string format matches with date format if we get error we throw format not correct towards the user
                try:
                    datetime.strptime(dob, "%d/%m/%Y")
                    return dob
                except:
                    print("Format not correct please user the DD/MM/YYYY format")
            elif type == "gender":
                #choosing gender
                gender = input("Enter your gender (Male/Female/Other): ")
                gend_list = ["male", "female", "other"]
                if gender.lower() not in gend_list:
                    print("Invalid input Please choose a gender from the list (Male/Female/Other)")
                else:
                    return gender
            elif type == "semester": # for student only
                # choosing semester
                sem_list = ["1st", "2nd", "3rd", "4th", "5th"]
                semester = input("Enter your semester no in ordinal number (Choose from 1st to 5th): ")
                # checking if user inputed semester from 1 to 5
                if semester not in sem_list:
                    print("Invalid input. Please enter ordinal number of your semester")
                else:
                    return semester
            elif type == "dept": # for staff only
                # choosing dept from the dept list
                dept_list = ["CSE", "EEE", "ECE", "BBA", "ECO", "ENG", "MAT", "PHY"]
                dept_str = "Choose from these departments: "
                for dept in dept_list:
                    dept_str += dept + ", "
                dept_str = dept_str[:-2]
                print(dept_str)
                dept = input("Enter your department initial from above list: ")
                if dept not in dept_list:
                    print("Invalid input. Please enter a department intial from above list")
                else:
                    return dept
                
    def set_encryption(type, user_name, password):
        if type == "encrypt":
            # Encrypting the password            
            password += str(random.randint(1,9))
            encrypt_pass = ""
            for letter in password:
                asci = ord(letter)
                # converting ascii value to binary
                bin_value = ""
                while asci != 0:
                    remainder = asci % 2
                    asci = asci // 2
                    bin_value += str(remainder)
                # reversing the string to form proper binary representation
                bin_value = bin_value[::-1]
                rem_length = 7 - len(bin_value)
                # checking if the binary value is 7 bit
                if rem_length != 0:
                    bin_value = ("0" * rem_length) + bin_value
                encrypt_pass += bin_value
            return encrypt_pass
        elif type == "decrypt":
            # Finding in which database username is
            if user_name in Account.__data_dict["student_dict"].keys():
                __data_dict = Account.__data_dict["student_dict"]
            else:
                __data_dict = Account.__data_dict["staff_dict"]
            # Decryption of the password
            decrypt_pass = ""
            bin_power = 6
            dec_value = 0
            for letter in __data_dict[user_name]["Password"]:
                # Converting binary to decimal
                dec_value += int(letter) * (2 ** bin_power)
                bin_power -= 1
                # if 7 bit binary is fullfilled
                if bin_power < 0:
                    decrypt_pass += str(chr(dec_value))
                    dec_value = 0
                    bin_power = 6
            # removing the extra character
            decrypt_pass = decrypt_pass[:-1]
            return decrypt_pass
                    
    def set_pass(password):
        # Checking if password length is greater than 8
        if len(password) >= 8:
            # Creating a dictionary to check conditions
            pass_check_dict = {"upper": [0, "Uppercase Missing"], "lower" : [0, "Lowercase Missing"],
                            "digit": [0, "Digit Missing"], "special" : [0, "Special Character Missing"],}
            for letter in password:
                # Chekcing for uppercase
                if letter in string.ascii_uppercase:
                    pass_check_dict["upper"][0] += 1
                # Chekcing for lowercase
                elif letter in string.ascii_lowercase:
                    pass_check_dict["lower"][0] += 1
                # Chekcing for digit
                elif letter in string.digits:
                    pass_check_dict["digit"][0] += 1
                # Chekcing for special characters
                elif letter in string.punctuation:
                    pass_check_dict["special"][0] += 1
            missing = ""
            # Checking if values are 0 in the dict
            for value in pass_check_dict.values():
                if value[0] == 0:
                    # Adding missing element in missing
                    missing += value[1] + ", "
            # Checking if anything is missing in passwrod
            miss_str = missing[:-2]
            if missing != "":
                print(miss_str)
                return False
            confirm = input("Confirm your password: ")
            if password != confirm:
                # checking if both Password matches
                print("Password doesn't match, try again")
                return False
            else:
                return password
        else:
            print("Password require atleast 8 characters")
            return False

    def update(self, key, diction, user_name):
        # for email
        if key == "Email":
            while True:
                update_info = input("New Email: ")
                # If the new email is same as previous email we will not allow it
                if diction[key] == update_info:
                    print("New Email cannnot be as same as previous one. Try again")
                # checking if @gmail.com is in the new email
                elif "@gmail.com" in update_info:
                    diction[key] = update_info
                    return update_info
                else:
                    print("Invalid input must have (@gmail.com) in the end")
        # for dept
        elif key == "Dept":
            # choosable department
            dept_list = ["CSE", "EEE", "ECE", "BBA", "ECO", "ENG", "MAT", "PHY"]
            dept_str = "Choose from these departments: "
            for dept in dept_list:
                dept_str += dept + ", "
            dept_str = dept_str[:-2]
            print(dept_str)
            # for new dept
            while True:
                update_info = input("New Dept: ")
                # if new dept same as old one we won't allow it
                if diction[key] == update_info:
                    print("New Dept cannnot be as same as previous one. Try again")
                # if dept not available in the dept list, user have to choose again
                elif update_info not in dept_list:
                    print("Invalid dept choose from the above dept")
                else:
                    diction[key] = update_info
                    return update_info
        # for password
        elif key == "Password":
            while True:
                update_info = input("New Password: ")
                new_pass = Account.set_pass(update_info)
                decrypt_pass = Account.set_encryption("decrypt", user_name, diction["Password"])
                if new_pass == decrypt_pass:
                    print("New Password cannnot be as same as previous one. Try again")
                elif new_pass != False:
                    encrypt_pass = Account.set_encryption("encrypt", user_name, new_pass)
                    diction[key] = encrypt_pass
                    return update_info
    
    def sign_in_account(user_name, password):
        # cheking if the username is in the __data_dict
        if (user_name not in Account.__data_dict["student_dict"].keys()) and (user_name not in Account.__data_dict["staff_dict"].keys()):
            print("Username doesn't exist")
        else:
            # finding out where user_name is 
            if user_name in Account.__data_dict["student_dict"].keys():
                diction = "student_dict"
            else:
                diction = "staff_dict"
            decrypt_pass = Account.set_encryption("decrypt", user_name, password)
            # Getting the decrypted password
            # checking if the Password matches with the user_name's Password
            if password == decrypt_pass:
                print("You are logged in")
                return (user_name, diction)
            else:
                print("Password does not match, try again")
        return False
        
    def create_account(account_type, f_name, l_name, user_name, email, password):
        # Getting the encrypted Password
        encrypt_pass = Account.set_encryption("encrypt", user_name, password)
        # checking if the account is student or staff type
        if account_type == "1":
            Account.__data_dict["student_dict"][user_name] = {"First name" : f_name, "Last name" : l_name, "Email": email, "Password" : encrypt_pass}
        else:
            Account.__data_dict["staff_dict"][user_name] = {"First name" : f_name, "Last name" : l_name, "Email": email, "Password" : encrypt_pass}
            
    def application(self, obj):
        # Navigating the informations
        while True:
            info_check = input("Input 1 to check course information, 2 to see profile info. 3 to sign out of account: ")
            if info_check.lower() == "3":
                print("Signed out")
                break
            # Showing the course information
            elif info_check == "1":
                obj.course_information()
            # Showing the profile information
            elif info_check == "2":
                obj.update_info("view")
                while True: 
                    # If user wants to update the profile
                    updating = input("Do you want to update your profile (Yes) or (No): ")
                    if updating.lower() == "no":
                        break
                    elif updating.lower() == "yes":
                        obj.update_info("update")
                        obj.update_info("view")
                    else:
                        print("Invalid input. Please type Yes or No")
            else:
                print("Invalid input. Please type 1 or 2 or signout.")
    
    @abstractmethod
    def course_information(self):
        pass
    
    @abstractmethod
    def update_info(self):
        pass
    
    @abstractmethod
    def complete_profile(self):
        pass
        
class StudentAccount(Account):
    # Getting the main dict
    data_dict = Account.get_data_dict()
    # creating the object
    def __init__(self, user_name, diction):
        self.user_name = user_name
        self.diction = diction
        
    # Course counting for new students # Only for the student class
    def course_count(self, lst):
        new_list = []
        count = 0
        while count != 4:
            result = random.choice(lst)
            if result not in new_list:
                new_list.append(result)
                count += 1
        return new_list
    
    def course_information(self):
        # show courses taken this Semester
        course_info = StudentAccount.data_dict[self.diction][self.user_name]["course_info"]
        Semester = StudentAccount.data_dict[self.diction][self.user_name]["Semester"]
        print(f"Course taken ({Semester}) Semester ")
        course_str = ""
        # displaying all the courses
        for course in course_info:
            course_str += course + ", "
        print(course_str[:-2])
        
    def update_info(self, mode):
        # updating personal info
        info = StudentAccount.data_dict[self.diction][self.user_name]
        #view mode of profile
        if mode == "view":
            index = 1
            for key, value in info.items():
                if key == "course_info":
                    continue
                elif key == "Password":
                    # decrypt first then add the password
                    decrypt_pass = Account.set_encryption("decrypt", user_name, password)
                    value = decrypt_pass
                print(str(index) + ") " + key + " : " + value)
                index += 1
        elif mode == "update":
            # update mode of profile
            while True:
                update_info = input("Type email or password to change it: ")
                update_info = update_info.lower().capitalize()
                # checking if the input is in dict.keys()
                if update_info in info.keys():
                    # if update_info is not equal to email or password we don't give access to user
                    if update_info != "Email" and update_info != "Password":
                        print("You can't change this information, only email and password are changable")
                    else:
                        # updating the info through update method
                        updated = self.update(update_info, info, self.user_name)
                        print(f"{update_info} updated to {updated}")
                        break
                else:
                    print("Invalid input, type email or password to change it")
                    
    def complete_profile(self):
        # completing the profile by giving rest of the info
        info = StudentAccount.data_dict[self.diction][self.user_name]
        ID = Account.set_profile("id")
        dob = Account.set_profile("dob")
        gender = Account.set_profile("gender")
        semester = Account.set_profile("semester")
        # choosing semester courses randomly from course_dict
        course_info = self.course_count(Account.course_dict[semester])
        new_dict = {"ID" : ID, "DOB" : dob, "Gender" : gender, "Semester": semester, "course_info" : course_info}
        # adding them in the dict
        for key, value in new_dict.items():
            info[key] = value
        print("Profile creation complete")
            
class StaffAccount(Account):
    # Getting the main dict
    data_dict = Account.get_data_dict()
    # creating the object
    def __init__(self, user_name, diction):
        self.user_name = user_name
        self.diction = diction
    
    def course_information(self):
        # Name and Id of students
        index = 1
        for user_name in StaffAccount.data_dict["student_dict"].keys():
            diction = StaffAccount.data_dict["student_dict"][user_name]
            full_name = diction["First name"].capitalize() + " " + diction["Last name"].capitalize()
            ID = diction["ID"]
            print(f"{index}) Name: {full_name}, ID: {ID}")
            index += 1
            
    def update_info(self, mode):
        # updating personal info
        info = StaffAccount.data_dict[self.diction][self.user_name]
        #view mode of profile
        if mode == "view":
            index = 1
            for key, value in info.items():
                if key == "course_info":
                    continue
                elif key == "Password":
                    # decrypt first then add the password
                    decrypt_pass = Account.set_encryption("decrypt", user_name, password)
                    value = decrypt_pass
                print(str(index) + ") " + key + " : " + value)
                index += 1
        elif mode == "update":
            # update mode of profile
            while True:
                update_info = input("Type email, password or dept to change it: ")
                update_info = update_info.lower().capitalize()
                # checking if the input is in dict.keys()
                if update_info in info.keys():
                    # if update_info is not equal to email or password we don't give access to user
                    if update_info != "Email" and update_info != "Password" and update_info != "Dept":
                        print("You can't change this information, only email, password and dept are changable")
                    else:
                        # updating the info through update method
                        updated = self.update(update_info, info, self.user_name)
                        print(f"{update_info} updated to {updated}")
                        break
                else:
                    print("Invalid input, type email or password to change it")
                    
    def complete_profile(self):
        # completing the profile by giving rest of the info
        info = StaffAccount.data_dict[self.diction][self.user_name]
        dob = Account.set_profile("dob")
        gender = Account.set_profile("gender")
        dept = Account.set_profile("dept")
        # updating the dict with new info
        new_dict = {"DOB" : dob, "Gender" : gender, "Dept" : dept}
        for key, value in new_dict.items():
            info[key] = value
        print("Profile creation complete")
            
#User code
while True:
    option = input("Input 1 to login, 2 to signup, 3 to close application: ")
    if option == '1':
        # for login
        while True:
            user_name = input("Enter Username: ")
            password = input("Enter Password: ")
            login_account = Account.sign_in_account(user_name, password) # returns user_name and the dict it is int else false
            if login_account != False:
                break
        # checking where the account is
        user = Account.get_account(login_account[0], login_account[1])
        # Navigating the inside of the application
        user.application(user)
            
    elif option == "2":
        # for signup
        while True: 
            # Getting whether the account will be staff or student
            account_type = input("Enter 1 for Student, 2 for Staff: ")
            if account_type == "1" or account_type == "2":
                f_name = input("First name: ").capitalize()
                l_name = input("Last name: ").capitalize()
                email = Account.set_profile("email")
                # For user_name
                user_name = Account.set_profile("user_name")
                # For password
                password = Account.set_profile("password")
                new_account = Account.create_account(account_type, f_name, l_name, user_name, email, password)
                # for login
                print("Login to your account")
                while True:
                    login_user_name = input("Enter Username: ")
                    # user must login in his own newly created id
                    if login_user_name != user_name:
                        print("Please login to your account after creation")
                        continue
                    login_password = input("Enter Password: ")
                    login_account = Account.sign_in_account(login_user_name, login_password)
                    if login_account != False:
                        break
                # checking where the account is
                user = Account.get_account(login_account[0], login_account[1])
                # Completing profile
                user.complete_profile()
                # Navigating the inside of the application
                user.application(user)
                break
            else:
                print("Invalid input, choose 1 for Student, 2 for Staff")
    # If user wants to close the application
    elif option == "3":
        print("Application closed")
        break
    # If input is not 1, 2 or 3
    else:
        print("Invalid input please choose 1 to login, 2 to sign up")
        
#ert34!@Y
#gh238!HKuig
#tuiRT56%$#

