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
    state.root.children["Why join InCollege? (Video)"] = WhyJoinInCollege(
        title="Why join InCollege?", state=state, login_required=False)
    state.root.children["Login"] = Login(
        title="Login", state=state, login_required=False)
    state.root.children["Create Account"] = CreateAccount(
        title="Create Account", state=state, login_required=False)
    state.root.children["My Account Settings"] = ManageAccount(title = "ManageAccount", state = state, login_required=True)
    state.root.children["Job Search"] = JobSearch(
        title="Job Search", state=state, login_required=False, parent=state.root)
    state.root.children["Find Someone Who Can Help!"] = FindUser(
        title="Find a User", state=state, login_required = False)
    state.root.children["Learn New Skills"] = LearnSkills(
        title="Learn New Skills", state=state, parent=state.root)
    p = state.root.children["Learn New Skills"]
    state.root.children["Learn New Skills"].children = {"Learn Python": LearnPython(title="Learn Python", state=state, parent=p),
                                                        "Learn Resume Building": LearnResumeBuilding(title="Learn Resume Building", state=state, parent=p),
                                                        "Learn C++": LearnCPP(title="Learn C++", state=state, parent=p),
                                                        "Learn How to Interview": LearnInterviews(title="Learn How to Interview", state=state, parent=p),
                                                        "Learn Penetration Testing": LearnPenetrationTesting(title="Learn Penetration Test", state=state, parent=p)}

    p = state.root.children["Job Search"]
    p.children = {"Post a Job": PostJob(title="Post a Job", state=state, parent=p)}


def main():
    # load users
    state = State()
    state.account_file_name = 'accounts.csv'
    state.job_file_name = 'jobs.csv'
    state.load_accounts()
    state.load_success_stories()
    state.load_jobs()
    initialize_page_tree(state)
    while (state.application_active):
        if (state.current_page == None):
            state.current_page = state.root
        state.current_page.onLoad()


if __name__ == "__main__":
    main()
