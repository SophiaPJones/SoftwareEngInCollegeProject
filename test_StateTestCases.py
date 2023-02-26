from unittest import TestCase
from State import *
from User import *
from Util import *
from Job import *

class StateTestCases(TestCase):
    def test_saving_account(self):
        newState = State()

        newState.account_file_name = "accounts.csv"
        newState.users["UserName1"] = User("first","second","Username1", "Password1!")
        assert newState.save_accounts() == True

    def test_saving_over_five_accounts(self):
        newState = State()

        newState.account_file_name = "accounts.csv"
        newState.users["UserName1"] = User("first","second","Username1", "Password1!")
        newState.users["UserName2"] = User("first","second","Username2", "Password1!")
        newState.users["UserName3"] = User("first","second","Username3", "Password1!")
        newState.users["UserName4"] = User("first","second","Username4", "Password1!")
        newState.users["UserName5"] = User("first","second","Username5", "Password1!")
        newState.users["UserName6"] = User("first","second","Username6", "Password1!")
        newState.save_accounts()
        assert newState.save_accounts() == False
    
    def test_contains_capital_letter(self):
        assert contains_capital_letter('Squeaky1!') == True
        assert contains_capital_letter('squEaky1!') == True
        assert contains_capital_letter('squeaky1!') == False

    def test_contains_small_letter(self):
        assert contains_capital_letter('squeaky1!') == False
        assert contains_capital_letter('squaey1!') == False


    def test_contains_number(self):
        assert contains_number('Squeaky0!') == True
        assert contains_number('Squ1eaky!') == True
        assert contains_number('Sque2aky!') == True
        assert contains_number('Sq3ueaky!') == True
        assert contains_number('S4queaky!') == True
        assert contains_number('5Squeaky!') == True
        assert contains_number('Squeak6y!') == True
        assert contains_number('Sq7ueaky!') == True
        assert contains_number('Squeaky8!') == True
        assert contains_number('Squeak9y!') == True
        assert contains_number('Squeaky!') == False


    def test_contains_special_character(self):
        assert contains_special_character('Squeaky1!') == True
        assert contains_special_character('Sq@ueaky1') == True
        assert contains_special_character('Sq#ueaky1') == True
        assert contains_special_character('Squeak$y1') == True
        assert contains_special_character('S%queaky1') == True
        assert contains_special_character('Squeak^y1') == True
        assert contains_special_character('&Squeaky1') == True
        assert contains_special_character('Squea*ky1') == True
        assert contains_special_character('S(queaky1') == True
        assert contains_special_character('Squeaky1') == False


    def test_validate_password(self):
        assert validate_password('Squeaky1!') == True
        assert validate_password('squeaky2!') == False
        assert validate_password('Squeaky!') == False
        assert validate_password('Squeaky3') == False


    def test_user_password(self):
        user = User("first","second","Username1", "Password1!")
        assert user.password == "Password1!"
        assert user.password != "Password1"

    def test_change_password(self):
        user = User("first","second","Username1", "Password1!")
        user.change_password("Password12@@")
        assert user.password == "Password12@@"

    def test_user_list(self):
        user = User("first","second","Username1", "Password1!")
        assert user.list() == ["first","second","Username1","Password1!","",True,True,True,0]

    def test_user_success_story(self):
        user = User("first","second","Username1", "Password1!")
        user.set_success_story("Testing out this functionality")
        assert user.success_story == "Testing out this functionality"

    def test_job_creation(self):
        job = Job("python dev", "backend dev", "Apple", "USA", "$100000")
        assert job.title == "python dev"
        assert job.description == "backend dev"
        assert job.employer == "Apple"
        assert job.location == "USA"
        assert job.salary == "$100000"
    
    def test_change_langauge(self):
        user = User("first","second","Username1", "Password1!")
        user.change_language(0)
        assert user.language == 0

