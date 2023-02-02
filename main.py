from State import *
from Pages import *

def initialize_page_tree(state):
    state.root = Home(title="Home", state=state)
    state.root.children["Login"] = Login(title="Login", state=state, login_required = False)
    state.root.children["Create Account"] = CreateAccount(title="Create Account", state=state, login_required=False)
    state.root.children["Job Search"] = JobSearch(title="Job Search", state = state)
    state.root.children["Find Someone You Know"] = FindUser(title="Find a User", state = state)
    state.root.children["Learn New Skills"] = LearnSkills(title="Learn New Skills", state=state)
    state.root.children["Learn New Skills"].skills = {"Learn Python": LearnPython(title="Learn Python", state = state),
                                                      "Learn Resume Building": LearnResumeBuilding(title="Learn Resume Building", state = state),
                                                      "Learn C++": LearnCPP(title="Learn C++", state = state),
                                                      "Learn How to Interview": LearnInterviews(title="Learn How to Interview", state = state),
                                                      "Learn Penetration Testing": LearnPenetrationTesting(title="Learn Penetration Test", state = state)}
def main():
    #load users
    state = State()
    initialize_page_tree(state)
    while(state.application_active):
            if(state.current_page == None): state.current_page = state.root
            state.current_page.onLoad()

if __name__ == "__main__":
    main()
