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
import Util

class Page:
    """ An base class off of which all other pages are built off of.
    """
    def __init__(self, title="", login_required = True, state=State(), parent=None):
        self.parent = parent
        self.state = state
        self.children = {}
        self.title = title
        self.login_required = login_required
        self.split_star = "*"*30
        self.split_tilde = "~"*30
    def onLoad(self):
        pass
    def print_content(self):
        pass
    def __str__(self):
        return f"Not implemented :)"
    def set_parent(self, new_parent):
        self.parent = new_parent

class Home(Page):
    """ The home page is the main page of the application. All other pages can
    be reached from this page. It's effectively the root of the application, and
    it is represented in the application state as such.
    """
    def onLoad(self):
        self.print_content()
        self.navigate()
        pass
    def navigate(self):
        print(f"{self.split_star}")
        print("Select a page to navigate to:\n")
        for page in list(self.children.keys()):
            if self.children[page].login_required and self.state.current_user != None: print(f"\t> {page}")
            elif not self.children[page].login_required:
                print(f"\t> {page}")
        print("\n")
        selection = input("Type the page you'd like to navigate to. Enter nothing to exit inCollege: ")
        if(selection == ""):
            self.state.application_active = False
            return
        selection_clean = selection.strip()
        if(selection_clean in self.children):
            self.state.current_page = self.children[selection_clean]
        else:
            print("Invalid page selection! Please try again.")
            self.navigate()

    def print_content(self):
        welcome_message = "Welcome to inCollege!" if self.state.current_user == None else f"Welcome to inCollege, {self.state.current_user.username}!"
        print(f"{self.split_star}\n\n{welcome_message}\n\n{self.split_tilde}")

class Login(Page):
    def print_content(self):
        print(f"{self.split_tilde}\nPlease log in by entering your username and password.",
              f"\nAlternatively, type 'Create New Account' to navigate to the Create Account screen.",
              f"\nOtherwise, type nothing when prompted and you will return to the home page.:")
    def onLoad(self):
        self.print_content()
        username = input("\n\tUsername: ")
        password = input("\tPassword: ")
        cna = "Create New Account"
        if(username == cna or password == cna):
            self.state.current_page = self.state.root.children["Create Account"]
        elif(username == "" or password == ""):
            self.state.current_page = self.state.root
        else:
            if username in self.state.users:
                if self.state.users[username].password == password:
                    print(f"Successfully logged in as {username}!")
                    self.state.current_user = self.state.users[username]
                    self.state.current_page = self.state.current_page = self.state.root
                else:
                    print("Invalid username/password, please try again")
                    self.onLoad()
            else:
                print("Invalid username/password, please try again")
                self.onLoad()
        pass

class CreateAccount(Page):

    def onLoad(self):
        self.print_content()
        username = input("Enter the new account's username: ")
        if(username == ""):
            self.state.current_page = self.state.root
            return
        password = input("Enter the new account's password: ")
        if username in self.state.users:
            print("That username is already taken! Try again.")
        else:
            passwordValid = Util.validate_password(password)
            if passwordValid:
                if len(self.state.users) >= Util.MAXIMUM_USER_COUNT:
                    print("All permitted accounts have been created, please come back later.\n")
                    self.state.current_page = self.state.root
                else:
                    self.state.users[username] = User(username, password)
                    self.state.save_accounts()
            else:
                print("Invalid password. The password must be between 8 and 12 characters (inclusive) and must contain:\n\t* At least 1 capital letter\n\t* At least 1 special character.\n\t* At least 1 digit.\nPlease try again.")
                self.onLoad()

    def print_content(self):
        print(f"{self.split_tilde}\nCreate an account by providing a username and password when prompted!\n",
              f"Type nothing when prompted to return to the home page.\n")

class JobSearch(Page):
    def print_content(self):
        print(f"{self.split_tilde}\n Under construction.\n")
        input()
    def onLoad(self):
        self.print_content()
        self.state.current_page = self.state.root

class FindUser(Page):
    def print_content(self):
        print(f"{self.split_tilde}\n Under construction.\n")
        input()
    def onLoad(self):
        self.print_content()
        self.state.current_page = self.state.root

class LearnSkills(Page):
    def print_content(self):
        print(f"\n{self.split_star}\n",
              f"Time to learn some skills, {self.state.current_user.username}!\n",
              f"Select from one of the options below:\n")
        for option in list(self.children.keys()):
            print(f"> {option}")
        print('\n')
    def onLoad(self):
        self.print_content()
        selection = input("Type your selection here. Type nothing to return to the home page.: ")
        if selection == "":
            self.state.current_page = self.state.root
            return
        if selection in self.children:
            self.state.current_page = self.children[selection]
        else:
            print("Invalid selection! Try again.")
            self.onLoad()

class LearnPython(Page):
    def print_content(self):
        print(f"{self.split_tilde}\n Under construction.\n")
        input()
    def onLoad(self):
        self.print_content()
        self.state.current_page = self.state.root

class LearnCPP(Page):
    def print_content(self):
        print(f"{self.split_tilde}\n Under construction.\n")
        input()
    def onLoad(self):
        self.print_content()
        self.state.current_page = self.state.root

class LearnResumeBuilding(Page):
    def print_content(self):
        print(f"{self.split_tilde}\n Under construction.\n")
        input()
    def onLoad(self):
        self.print_content()
        self.state.current_page = self.state.root

class LearnInterviews(Page):
    def print_content(self):
        print(f"{self.split_tilde}\n Under construction.\n")
        input()
    def onLoad(self):
        self.print_content()
        self.state.current_page = self.state.root

class LearnPenetrationTesting(Page):
    def print_content(self):
        print(f"{self.split_tilde}\n Under construction.\n")
        input()
    def onLoad(self):
        self.print_content()
        self.state.current_page = self.state.root
