from State import *
from Pages import *
import csv

def initialize_page_tree(state):
    """
    Initialize the application pages within the state. Mutates the state.
    Parameters
    _____________________
    state: State
       an instance of a State object. Typically the application state, which there should be only 1 of.
    """
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



def main():
    #load users
    state = State()
    state.account_file_name = 'accounts.csv'
    state.load_accounts()
    initialize_page_tree(state)
    while(state.application_active):
            if(state.current_page == None): state.current_page = state.root
            state.current_page.onLoad()

if __name__ == "__main__":
    main()
