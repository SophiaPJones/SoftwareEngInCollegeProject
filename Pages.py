#!/usr/bin/env python3
"""This file defines all of the pages in the application, as well as the functionality
which that page depends on.
A page typically has a parent, which is a reference to the parent page,
    a title, which is a string that defines what the page is called.
    login_required which determined whether a valid login is required to view the page,
    state, which is a State object. This is initialized when the program launches.
A page also tends to have an onLoad function which runs when the page is loaded.
"""

from State import *
from User import *
from Util import *
from Job import *
import random


class Page:
    """ An base class off of which all other pages are built off of.
    """

    def __init__(self, title="", login_required=True, state=State(), parent=None):
        self.state = state
        if (parent == None):
            self.parent = self.state.root
        else:
            self.parent = parent
        self.children = {}
        self.title = title
        self.login_required = login_required
        self.split_star = "*"*30
        self.split_tilde = "~"*30

    def onLoad(self):
        clear_console()

    def print_content(self):
        pass

    def __str__(self):
        return f"Not implemented :)"

    def set_parent(self, new_parent):
        self.parent = new_parent

    def print_menu(self):
        print(f"{self.split_star}")
        print("Select a page to navigate to:\n")
        parent = "Exit InCollege" if self.parent is None else self.parent.title
        print(f"\t0.) {parent}")
        for i, page in enumerate(list(self.children.keys())):
            if self.children[page].login_required and self.state.current_user != None:
                print(f"\t{i+1}.) {page}")
            elif not self.children[page].login_required:
                print(f"\t{i+1}.) {page}")
        print("\n")

    def page_select(self):
        selection = input(
            "Type the page you'd like to navigate to. (Number or exact name): ")
        if (selection == "0"):  # Change page to parent page
            if (self.state.current_page == self.state.root):
                self.state.application_active = False
            else:
                self.state.current_page = self.parent
            return
        selection_clean = selection.strip()
        if (selection_clean in self.children):
            self.state.current_page = self.children[selection_clean]
        elif (selection_clean.isnumeric()
              # number is in correct range
              and (int(selection_clean) >= 0) and (int(selection_clean) <= len(self.children))
              and not (self.children[list(self.children)[int(selection_clean)-1]].login_required and self.state.current_user == None)):  # login check if referencing login_required page
            self.state.current_page = self.children[list(
                self.children)[int(selection_clean)-1]]
        else:
            print("\nInvalid page selection! Please try again.\n")
            self.input_to_continue()
            clear_console()
            self.navigate()

    def input_to_continue(self):
        input(
            f"\n\t{self.split_star}\n\n\t* Press anything to continue *\n\n\t{self.split_star}")


class Home(Page):
    """ The home page is the main page of the application. All other pages can
    be reached from this page. It's effectively the root of the application, and
    it is represented in the application state as such.
    """

    def onLoad(self):
        clear_console()
        self.print_content()
        self.navigate()
        pass

    def navigate(self):
        self.print_menu()
        self.page_select()

    def print_content(self):
        welcome_message = "Welcome to inCollege!" if self.state.current_user == None else f"Welcome to inCollege, {self.state.current_user.username}!"
        print(f"{self.split_star}\n\n{welcome_message}\n\n{self.split_tilde}")
        if (self.state.success_stories != {}):
            user, story = random.choice(
                list(self.state.success_stories.items()))
            print(f"Hear one of our user's success stories!: {story}")
        else:
            print(f"Hear one of our user's success stories!: \n\t\t'inCollege helped me get the skills I needed to succeed,\n\t\tand set me up with a network of contacts that helped\n\t\tme find a great job!' -- Sylvia K.")


class ManageAccount(Page):
    def onLoad(self):
        clear_console()
        self.print_content()
        self.menu()

    def print_content(self):
        print(f"Manage your InCollege Account!\n{self.split_star}")
        print(
            f"\tUsername: {self.state.current_user.username}\n{self.split_tilde}")

    def menu(self):
        print("Select an option to change on your account or return home:\n")
        print(f"\t0. Return Home")
        print(
            f"\t1. Update First Name (Currently: {self.state.current_user.first_name})")
        print(
            f"\t2. Update Last Name (Currently: {self.state.current_user.last_name})")
        print(f"\t3. Update Password")
        print(
            f"\t4. Add your success story!\nCurrently your success story is: {self.state.current_user.success_story}")
        selection = input(
            "Type your preferred option or enter corresponding number: ")
        selection = "".join(selection.split()).lower()
        if (selection == "updatefirstname" or
            selection == "firstname" or
            selection == "first" or
            selection == "1" or
                selection == "1."):
            self.change_first_name()
        elif (selection == "updatelastname" or
              selection == "lastname" or
              selection == "last" or
              selection == "2" or
              selection == "2."):
            self.change_last_name()
        elif (selection == "updatepassword" or
              selection == "password" or
              selection == "3" or
              selection == "3."):
            self.change_password()
        elif (selection == "addyoursuccessstory" or
              selection == "addsuccessstory" or
              selection == "successstory" or
              selection == "success" or
              selection == "story" or
              selection == "mysuccessstory" or
              selection == "addmysuccessstory" or
              selection == "4." or
              selection == "4"):
            self.change_success_story()
        elif (selection == "home" or
              selection == "0" or
              selection == "0." or
              selection == "returnhome" or
              selection == "return"):
            self.state.current_page = self.parent

    def change_first_name(self):
        new_first_name = input("\nEnter new first name: ")
        while (new_first_name == ""):
            new_first_name = input("\nEnter new first name:")
        self.state.current_user.first_name = new_first_name
        if (self.state.save_accounts() == True):
            print("\nFirst name changed Successfully")
            self.input_to_continue()

    def change_last_name(self):
        new_last_name = input("\nEnter new last name: ")
        while (new_last_name == ""):
            new_last_name = input("\nEnter new last name:")
        self.state.current_user.last_name = new_last_name
        if (self.state.save_accounts() == True):
            print("\nLast name changed Successfully")
            self.input_to_continue()

    def change_password(self):
        new_password = input("\nEnter new password: ")
        passwordValid = Util.validate_password(new_password)
        while (not passwordValid):
            print("Invalid password. The password must be between 8 and 12 characters (inclusive) and must contain:\n\t* At least 1 capital letter\n\t* At least 1 special character.\n\t* At least 1 digit.\nPlease try again.\n")
            new_password = input("\nEnter new password: ")
            passwordValid = Util.validate_password(new_password)
        if passwordValid:
            self.state.current_user.password = new_password
            if (self.state.save_accounts() == True):
                print("\nPassword changed Successfully")
                self.input_to_continue()
        if (self.state.save_accounts() == True):
            print("\nPassword changed Successfully")
            self.input_to_continue()

    def change_success_story(self):
        new_success_story = ""
        user_story_in = input(
            "Enter new success story (type nothing and press enter to stop): ")
        while user_story_in != "":
            new_success_story += user_story_in + "\n"
            user_story_in = input("\t> ")
        self.state.current_user.success_story = new_success_story
        if (self.state.save_accounts() == True):
            print("\nSuccess story changed Successfully")
            self.input_to_continue()
        self.state.load_success_stories()


class PostJob(Page):
    def onLoad(self):
        clear_console()
        self.print_content()
        title = input("\tEnter job title: ")
        if (title == ""):
            self.state.current_page = self.parent
            return
        description = input("\tEnter a brief description: ")
        if (description == ""):
            self.state.current_page = self.parent
            return
        employer = input("\tEnter the employer organization: ")
        if (employer == ""):
            self.state.current_page = self.parent
            return
        location = input("\tEnter the job location: ")
        if (location == ""):
            self.state.current_page = self.parent
            return
        salary = input("\tEnter the salary: ")
        if (salary == ""):
            self.state.current_page = self.parent
            return
        new_job = Job(title, description, employer, location, salary)
        self.state.jobs.append(new_job)
        if (not self.state.save_jobs()):
            self.state.jobs.pop()
        self.state.current_page = self.parent

    def print_content(self):
        print(
            f"Post a job opportunity for inCollege users to apply to! Enter nothing on any of the options to cancel and return home.\n{self.split_star}\n")
        pass


class FindUser(Page):
    def onLoad(self):
        clear_console()
        self.print_content()
        first_name = input("\tEnter a first name: ")
        last_name = input("\tEnter a last name: ")
        contacts = [val for key, val in self.state.users.items() if (
            val.first_name == first_name and val.last_name == last_name)]
        if contacts != []:
            print(f"\nThey are a part of the inCollege system!")
            if (self.state.current_user == None):
                print(
                    f"\nYou can log in or create an account to contact them! Select your option below:\n")
                print(f"\t0. Return Home")
                print(f"\t1. Log In")
                print(f"\t2. Create Account")
                selection = input(
                    "\nEnter the number corresponding to your selection or type the option you want: ")
                selection = "".join(selection.split()).lower()
                if (selection == "0."
                    or selection == "0"
                    or selection == "returnhome"
                    or selection == "return"
                        or selection == "home"):
                    self.state.current_page = self.parent
                elif (selection == "1."
                      or selection == "1"
                      or selection == "login"):
                    self.state.current_page = self.state.root.children["Login"]
                elif (selection == "2."
                      or selection == "2"
                      or selection == "createaccount"):
                    self.state.current_page = self.state.root.children["Create Account"]
        else:
            print(f"\nThey are not yet part of the inCollege system!")
            self.input_to_continue()
            self.state.current_page = self.state.current_page.parent

    def print_content(self):
        print(
            f"\nFind someone who can help! Search for a user by first and last name below.\n {self.split_tilde}")


class Login(Page):
    def print_content(self):
        print(f"{self.split_tilde}\nPlease log in by entering your username and password.",
              f"\nAlternatively, type 'Create New Account' to navigate to the Create Account screen.",
              f"\nOtherwise, type nothing when prompted and you will return to the home page.:")

    def navigate(self):
        self.print_menu()

    def onLoad(self):
        clear_console()
        self.print_content()
        username = input("\n\tUsername: ")
        password = input("\tPassword: ")
        cna = "Create New Account"
        if (username == cna or password == cna):
            self.state.current_page = self.state.root.children["Create Account"]
        elif (username == "" or password == ""):
            self.state.current_page = self.state.root
        else:
            if username in self.state.users:
                if self.state.users[username].password == password:
                    print(f"Successfully logged in as {username}!")
                    self.state.current_user = self.state.users[username]
                    self.state.current_page = self.state.current_page = self.state.root
                else:
                    print("Invalid username/password, please try again")
                    self.input_to_continue()
                    self.onLoad()
            else:
                print("Invalid username/password, please try again")
                self.input_to_continue()
                self.onLoad()
        pass


class CreateAccount(Page):

    def onLoad(self):
        clear_console()
        self.print_content()
        self.create_new_account()

    def print_content(self):
        print(f"{self.split_tilde}\nCreate an account by providing a username and password when prompted!\n",
              f"Type nothing when prompted to return to the home page.\n")

    def create_new_account(self):
        first_name = input("Enter first name: ")
        if (first_name == ""):
            self.state.current_page = self.state.root
            return
        last_name = input("Enter last name: ")
        username = input("Enter the new account's username: ")
        if username in self.state.users:
            print("That username is already taken! Try again.\n")
            self.input_to_continue()
        else:
            password = input("Enter the new account's password: ")
            passwordValid = Util.validate_password(password)
            if passwordValid:
                if len(self.state.users) >= Util.MAXIMUM_USER_COUNT:
                    print(
                        "All permitted accounts have been created, please come back later.\n")
                    self.input_to_continue()
                    self.state.current_page = self.state.root
                else:
                    self.state.users[username] = User(
                        first_name, last_name, username, password)
                    if (self.state.save_accounts() == True):
                        print("\nAccount Created Successfully")
                        self.input_to_continue()

            else:
                print("Invalid password. The password must be between 8 and 12 characters (inclusive) and must contain:\n\t* At least 1 capital letter\n\t* At least 1 special character.\n\t* At least 1 digit.\nPlease try again.\n")
                self.input_to_continue()
                self.onLoad()


class JobSearch(Page):
    def print_content(self):
        print(f"Search for or post a job/internship!\n{self.split_star}")
        print(f"\n Under Construction (Only Job Posting implemented)\n")

    def onLoad(self):
        clear_console()
        self.print_content()
        self.print_menu()
        self.page_select()


class LearnSkills(Page):
    def print_content(self):
        print(f"\n{self.split_star}\n",
              f"Time to learn some skills, {self.state.current_user.username}!\n",
              f"Select from one of the options below:\n")
        print('\n')

    def onLoad(self):
        clear_console()
        self.print_content()
        self.navigate()
        pass

    def navigate(self):
        self.print_menu()
        self.page_select()


class LearnPython(Page):
    def print_content(self):
        print(f"{self.split_tilde}\n Under construction.\n")

    def onLoad(self):
        clear_console()
        self.print_content()
        self.state.current_page = self.parent


class LearnCPP(Page):
    def print_content(self):
        print(f"{self.split_tilde}\n Under construction.\n")

    def onLoad(self):
        clear_console()
        self.print_content()
        self.state.current_page = self.parent


class LearnResumeBuilding(Page):
    def print_content(self):
        print(f"{self.split_tilde}\n Under construction.\n")

    def onLoad(self):
        clear_console()
        self.print_content()
        self.state.current_page = self.parent


class LearnInterviews(Page):
    def print_content(self):
        print(f"{self.split_tilde}\n Under construction.\n")

    def onLoad(self):
        clear_console()
        self.print_content()
        self.state.current_page = self.parent


class LearnPenetrationTesting(Page):
    def print_content(self):
        print(f"{self.split_tilde}\n Under construction.\n")

    def onLoad(self):
        clear_console()
        self.print_content()
        self.state.current_page = self.parent


class WhyJoinInCollege(Page):
    def print_content(self):
        print(
            f"\t{self.split_star}\n\t{self.split_tilde}\n\t    Video is now Playing    \n\t{self.split_tilde}\n\t{self.split_star}\n")
        self.input_to_continue()

    def onLoad(self):
        clear_console()
        self.print_content()
        self.state.current_page = self.parent


class UsefulLinks(Page):
    def print_content(self):
        print(f"\n{self.split_star}\n",
              f"All use Useful Links for you!\n",
              f"Select from one of the options below:\n")
        print('\n')

    def onLoad(self):
        clear_console()
        self.print_content()
        self.navigate()
        pass

    def navigate(self):
        self.print_menu()
        self.page_select()


class General(Page):
    def print_content(self):
        print(f"\n{self.split_star}\n",
              f"All General Information for you!\n",
              f"Select from one of the options below:\n")
        self.print_menu()
        print('\n')

    def onLoad(self):
        clear_console()
        self.print_content()
        self.navigate()
        pass

    def navigate(self):
        self.print_menu()
        self.page_select()


class BusinessSolutions(Page):
    def print_content(self):
        print(f"{self.split_tilde}\n Under construction.\n")

    def onLoad(self):
        clear_console()
        self.print_content()
        self.navigate()
        pass

    def navigate(self):
        self.print_menu()
        self.page_select()


class BrowseInCollege(Page):
    def print_content(self):
        print(f"{self.split_tilde}\n Under construction.\n")

    def onLoad(self):
        clear_console()
        self.print_content()
        self.navigate()
        pass

    def navigate(self):
        self.print_menu()
        self.page_select()


class Directories(Page):
    def print_content(self):
        print(f"{self.split_tilde}\n Under construction.\n")

    def onLoad(self):
        clear_console()
        self.print_content()
        self.navigate()
        pass

    def navigate(self):
        self.print_menu()
        self.page_select()


class InCollegeImportantLinks(Page):
    def print_content(self):
        print(f"\n{self.split_star}\n",
              f"All use InCollege Important Links for you!\n",
              f"Select from one of the options below:\n")
        self.print_menu()
        print('\n')

    def onLoad(self):
        clear_console()
        self.print_content()
        self.navigate()
        pass

    def navigate(self):
        self.print_menu()
        self.page_select()


class CopyRightNotice(Page):
    def print_content(self):
        print(f"{self.split_tilde}\n This is Copyright Notice Page.\n")
        input()

    def onLoad(self):
        clear_console()
        self.print_content()
        self.navigate()
        pass

    def navigate(self):
        self.print_menu()
        self.page_select()


class About(Page):
    def print_content(self):
        print(f"{self.split_tilde}\n In College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide\n")

    def onLoad(self):
        clear_console()
        self.print_content()
        self.navigate()
        pass

    def navigate(self):
        self.print_menu()
        self.page_select()


class Accessibility(Page):
    def print_content(self):
        print(f"{self.split_tilde}\n This is Accessibility Page.\n")

    def onLoad(self):
        clear_console()
        self.print_content()
        self.navigate()
        pass

    def navigate(self):
        self.print_menu()
        self.page_select()


class UserAgreement(Page):
    def print_content(self):
        print(f"{self.split_tilde}\n This is User Agreement Page\n")

    def onLoad(self):
        clear_console()
        self.print_content()
        self.navigate()
        pass

    def navigate(self):
        self.print_menu()
        self.page_select()


class PrivacyPolicy(Page):
    def print_content(self):
        pass

    def onLoad(self):
        clear_console()
        self.print_content()
        self.navigate()
        pass

    def navigate(self):
        self.print_menu()
        self.page_select()


class GuestControls(Page):
    def print_content(self):
        print(f"{self.split_tilde}\n This is Privacy Policy Page.\n")

    def onLoad(self):
        clear_console()
        self.print_content()
        self.menu()
        pass

    def navigate(self):
        self.print_menu()
        self.page_select()

    def menu(self):
        print("Select an option to change on your account or return home:\n")
        print(f"\t0. Return Home")
        if (self.state.current_user):
            print(
                f"\t1. Change InCollege Email Permissions (Currently: {self.state.current_user.email_notifications})")
            print(
                f"\t2. Change SMS Permissions (Currently: {self.state.current_user.sms})")
            print(
                f"\t3. Change Targeted Advertising Permissions (Currently: {self.state.current_user.targeted_advertising})")
        selection = input(
            "Type your preferred option or enter corresponding number: ")
        selection = "".join(selection.split()).lower()
        if (selection == "email" or
            selection == "1" or
                selection == "1."):
            self.change_email_permission()
        elif (selection == "sms" or
                selection == "2" or
                selection == "2."):
            self.change_sms_permission()
        elif (selection == "ad" or
                selection == "3" or
                selection == "3."):
            self.change_ad_permission()
        elif (selection == "home" or
              selection == "0" or
              selection == "0." or
              selection == "returnhome" or
              selection == "return"):
            self.state.current_page = self.parent

    def change_email_permission(self):
        self.state.current_user.email_notifications = not self.state.current_user.email_notifications
        if (self.state.save_accounts() == True):
            print("\nPermission changed Successfully")
            self.input_to_continue()

    def change_sms_permission(self):
        self.state.current_user.sms = not self.state.current_user.sms
        if (self.state.save_accounts() == True):
            print("\nPermission changed Successfully")
            self.input_to_continue()

    def change_ad_permission(self):
        self.state.current_user.targeted_advertising = not self.state.current_user.targeted_advertising
        if (self.state.save_accounts() == True):
            print("\nPermission changed Successfully")
            self.input_to_continue()


class CookiePolicy(Page):
    def print_content(self):
        print(f"{self.split_tilde}\n This is Cookie Policy Page.\n")

    def onLoad(self):
        clear_console()
        self.print_content()
        self.navigate()
        pass

    def navigate(self):
        self.print_menu()
        self.page_select()


class CopyrightPolicy(Page):
    def print_content(self):
        print(f"{self.split_tilde}\n This is Copyright Policy Page\n")

    def onLoad(self):
        clear_console()
        self.print_content()
        self.navigate()
        pass

    def navigate(self):
        self.print_menu()
        self.page_select()


class BrandPolicy(Page):
    def print_content(self):
        print(f"{self.split_tilde}\n This is Brand Policy Page.\n")

    def onLoad(self):
        clear_console()
        self.print_content()
        self.navigate()
        pass

    def navigate(self):
        self.print_menu()
        self.page_select()


class Language(Page):
    def print_content(self):
        print(f"Manage your InCollege Account!\n{self.split_star}")
        print(
            f"\tUsername: {self.state.current_user.username}\n{self.split_tilde}")

    def onLoad(self):
        clear_console()
        self.print_content()
        self.menu()
        pass

    def navigate(self):
        self.print_menu()
        self.page_select()

    def menu(self):
        print("Select an option to change on your account or return home:\n")
        print(f"\t0. Return Home")
        print(
            f"\t1. Update Language (Currently: {self.state.current_user.language})")
        selection = input(
            "Type your preferred option or enter corresponding number: ")
        selection = "".join(selection.split()).lower()
        if (selection == "langauge" or
            selection == "1" or
                selection == "1."):
            self.change_language()
        elif (selection == "home" or
              selection == "0" or
              selection == "0." or
              selection == "returnhome" or
              selection == "return"):
            self.state.current_page = self.parent

    def change_language(self):
        new_language = input("\nEnter 0 for English, 1 for Spanish: ")
        while (new_language == ""):
            new_language = input("\nEnter 0 for English, 1 for Spanish: ")
        self.state.current_user.language = new_language
        if (self.state.save_accounts() == True):
            print("\nLanguage changed Successfully")
            self.input_to_continue()


class HelpCenter(Page):
    def print_content(self):
        print(f"{self.split_tilde}\n We're here to help\n")

    def onLoad(self):
        clear_console()
        self.print_content()
        self.navigate()
        pass

    def navigate(self):
        self.print_menu()
        self.page_select()


class Press(Page):
    def print_content(self):
        print(f"{self.split_tilde}\n In College Pressroom: Stay on top of the latest news, updates, and reports\n")

    def onLoad(self):
        clear_console()
        self.print_content()
        self.navigate()
        pass

    def navigate(self):
        self.print_menu()
        self.page_select()


class Blog(Page):
    def print_content(self):
        print(f"{self.split_tilde}\n Under construction.\n")

    def onLoad(self):
        clear_console()
        self.print_content()
        self.navigate()
        pass

    def navigate(self):
        self.print_menu()
        self.page_select()


class Careers(Page):
    def print_content(self):
        print(f"{self.split_tilde}\n Under construction.\n")

    def onLoad(self):
        clear_console()
        self.print_content()
        self.navigate()
        pass

    def navigate(self):
        self.print_menu()
        self.page_select()


class Developers(Page):
    def print_content(self):
        print(f"{self.split_tilde}\n Under construction.\n")

    def onLoad(self):
        clear_console()
        self.print_content()
        self.navigate()
        pass

    def navigate(self):
        self.print_menu()
        self.page_select()
