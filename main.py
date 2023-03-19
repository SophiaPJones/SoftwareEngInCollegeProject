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
    state.root.children["Job Search/Management"] = Jobs(
        title="Job Search", state=state, login_required=False, parent=state.root)
    state.root.children["Find Someone Who Can Help!"] = FindUser(
        title="Find a User", state=state, login_required=False)

    p = state.root.children["Job Search/Management"]
    p.children = {"Post a Job": PostJob(
        title="Post a Job", state=state, parent=p),
                  "Manage Your Job Postings": ManageJobs(
                      title="Manage your Jobs", state=state, parent=p
                  ),
                  "Search for Job/Internship": JobSearch(
                      title = "Search for a Job/Internship", state=state, parent=p
                  )}

    state.root.children['Useful Links'] = UsefulLinks(
        title="Useful Links", state=state, parent=state.root, login_required=False)

    p = state.root.children['Useful Links']

    state.root.children["Useful Links"].children = {
        "General": General(title='General Links', state=state, parent=p, login_required=False),
        "Browse InCollege": BrowseInCollege(title='Browse InCollege', state=state, parent=p, login_required=False),
        "Business Solutions": BusinessSolutions(title='Business Solutions', state=state, parent=p, login_required=False),
        "Directories": Directories(title='Directories', state=state, parent=p, login_required=False)
    }

    state.root.children['InCollege Important Links'] = InCollegeImportantLinks(
        title="InCollege Important Links", state=state, parent=state.root, login_required=False)

    p = state.root.children['InCollege Important Links']

    state.root.children['InCollege Important Links'].children = {
        "A Copyright Notice": CopyRightNotice(title='A Copyright Notice', state=state, parent=p, login_required=False),
        "About": About(title='About', state=state, parent=p, login_required=False),
        "Accessibility": Accessibility(title='Accessibility', state=state, parent=p, login_required=False),
        "User Agreement": UserAgreement(title='User Agreement', state=state, parent=p, login_required=False),
        "Privacy Policy": PrivacyPolicy(title='Privacy Policy', state=state, parent=p, login_required=False),
        "Cookie Policy": CookiePolicy(title='Cookie Policy', state=state, parent=p, login_required=False),
        'Copyright Policy': CopyrightPolicy(title='Copyright Policy', state=state, parent=p, login_required=False),
        'Brand Policy': BrandPolicy(title='Brand Policy', state=state, parent=p, login_required=False),
        'Guest Controls': [],  # Temporary
        'Languages': Language(title='Languages', state=state, parent=p, login_required=True)

    }       

    # Replace temporary value for Guest Controls
    state.root.children['InCollege Important Links'].children["Guest Controls"] = (GuestControls(
        title='Guest Controls', state=state, parent=state.root.children['InCollege Important Links'].children["Privacy Policy"], login_required=False))

    # Make Privacy Policy have same "Guest Controls" as Important Links
    state.root.children['InCollege Important Links'].children["Privacy Policy"].children = {
        "Guest Controls": state.root.children['InCollege Important Links'].children["Guest Controls"]
    }

    p = state.root.children["Useful Links"].children["General"]

    state.root.children["Useful Links"].children['General'].children = {
        "Sign Up": CreateAccount(title='General Links', state=state, parent=p, login_required=False),
        "Help Center": HelpCenter(title='Browse InCollege', state=state, parent=p, login_required=False),
        "About": About(title='Business Solutions', state=state, parent=p, login_required=False),
        "Press": Press(title='Directories', state=state, parent=p, login_required=False),
        "Blog": Blog(title='Directories', state=state, parent=p, login_required=False),
        "Careers": Careers(title='Directories', state=state, parent=p, login_required=False),
        "Developers": Developers(title='Directories', state=state, parent=p, login_required=False)
    }

    state.root.children["Learn New Skills"] = LearnSkills(
        title="Learn New Skills", state=state, parent=state.root)
    p = state.root.children["Learn New Skills"]
    state.root.children["Learn New Skills"].children = {"Learn Python": LearnPython(title="Learn Python", state=state, parent=p),
                                                        "Learn Resume Building": LearnResumeBuilding(title="Learn Resume Building", state=state, parent=p),
                                                        "Learn C++": LearnCPP(title="Learn C++", state=state, parent=p),
                                                        "Learn How to Interview": LearnInterviews(title="Learn How to Interview", state=state, parent=p),
                                                        "Learn Penetration Testing": LearnPenetrationTesting(title="Learn Penetration Test", state=state, parent=p)}

    state.root.children["Manage Profile"] = ManageProfile(
        title="Manage Profile", state=state, login_required=True)
    p = state.root.children["Manage Profile"]
    p.children = {"Change Profile Name": ChangeProfileName(title = 'Change Profile Name', state=state, parent=p, login_required = True),
                  "Change Password": ChangePassword(title="Change Password", state=state,parent=p,login_required=True),
                  "Change Title": ChangeTitle(title="Change Title", state=state, parent=p, login_required = True),
                  "Change Success Story": ChangeSuccessStory(title="Change Success Story", state=state, parent=p, login_required=True),
                  "Change Education Information": ChangeEducationInfo(title="Change Education Info", state=state, parent=p, login_required=True),
                  "Change About Me": ChangeAboutMe(title="Change About Me", state=state, parent=p, login_required=True),
                  "Change Experience Summary": ChangeExperienceSummary(title="Change Experience Summary", state=state, parent=p, login_required=True),
                  "Change Experience History": ChangeExperienceInfo(title="Change Experience History", state=state, parent=p, login_required = True)}

    # add one more for searchStudent
    # that has 3 children, one for each search type
    # bby last name, by university, by major    
    state.root.children["Search Students"] = SearchStudents(
        title="Search Students", state=state, login_required=True)

    state.root.children["Show my network"] = Friends(
        title="Friends", state=state, login_required=True)
    

    
    
    



    # add one more for searchStudent
    # that has 3 children, one for each search type
    # by last name, by university, by major
    state.root.children["Search Students"] = SearchStudents(
        title="Search Students", state=state, login_required=True)

    state.root.children["Show my network"] = Friends(
        title="Friends", state=state, login_required=True)

def main():
    # load users
    state = State()
    state.account_file_name = 'accounts.csv'
    state.job_file_name = 'jobs.csv'
    state.friends_file_name = 'friends.csv'
    state.experience_file_name = 'experience.csv'

    state.load_accounts()
    state.load_success_stories()
    state.load_jobs()
    state.load_friends()
    state.load_experience()
    initialize_page_tree(state)
    while (state.application_active):
        if (state.current_page == None):
            state.current_page = state.root
        state.current_page.onLoad()
    
    state.save_accounts()


if __name__ == "__main__":
    main()

