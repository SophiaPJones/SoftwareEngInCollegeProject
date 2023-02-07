from State import *
from Pages import *
import csv

def initialize_page_tree(state):
    state.root = Home(title="Home", state=state)
    state.root.children["Login"] = Login(title="Login", state=state, login_required = False)
    state.root.children["Create Account"] = CreateAccount(title="Create Account", state=state, login_required=False)
    state.root.children["Job Search"] = JobSearch(title="Job Search", state = state)
    state.root.children["Find Someone You Know"] = FindUser(title="Find a User", state = state)
    state.root.children["Learn New Skills"] = LearnSkills(title="Learn New Skills", state=state)
    p = state.root.children["Learn New Skills"]
    state.root.children["Learn New Skills"].children = {"Learn Python": LearnPython(title="Learn Python", state = state, parent = p),
                                                      "Learn Resume Building": LearnResumeBuilding(title="Learn Resume Building", state = state, parent = p),
                                                      "Learn C++": LearnCPP(title="Learn C++", state = state, parent = p),
                                                      "Learn How to Interview": LearnInterviews(title="Learn How to Interview", state = state, parent = p),
                                                      "Learn Penetration Testing": LearnPenetrationTesting(title="Learn Penetration Test", state = state, parent = p)}

def load_accounts(state):
    with open('accounts.csv') as csvFile:
        accountList = csv.reader(csvFile, delimiter = ',')
        for account in accountList:
            state.users[account[0]] = User(account[0], account[1])
        pass

def main():
    #load users
    state = State()
    load_accounts(state)
    initialize_page_tree(state)
    while(state.application_active):
            if(state.current_page == None): state.current_page = state.root
            state.current_page.onLoad()

if __name__ == "__main__":
    main()
