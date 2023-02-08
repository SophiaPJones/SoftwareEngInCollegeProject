from State import *
from User import *


def test_saving_account():
    newState = State()

    newState.account_file_name = "accounts.csv"
    newState.users["UserName1"] = User("Username1", "Password1!")
    assert newState.save_accounts() == True


def test_saving_over_five_accounts():
    newState = State()

    newState.account_file_name = "accounts.csv"
    newState.users["UserName1"] = User("Username1", "Password1!")
    newState.users["UserName2"] = User("Username2", "Password1!")
    newState.users["UserName3"] = User("Username3", "Password1!")
    newState.users["UserName4"] = User("Username4", "Password1!")
    newState.users["UserName5"] = User("Username5", "Password1!")
    newState.users["UserName6"] = User("Username6", "Password1!")
    newState.save_accounts()
    assert newState.save_accounts() == False
