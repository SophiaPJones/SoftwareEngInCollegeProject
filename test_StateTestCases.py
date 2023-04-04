from unittest import TestCase
import pytest
from os import *
import io
from Pages import *
from State import *
from User import *
from Util import *
from Job import *


@pytest.fixture(scope="function")
def inout(request, monkeypatch, capsys):
    request.cls.monkeypatch = monkeypatch
    request.cls.capsys = capsys


@pytest.mark.usefixtures("inout")
class StateTestCases(TestCase):
    def test_saving_account(self):
        newState = State()
        try:
            os.remove('accountsTest.csv')
        except:
            pass

        newState.account_file_name = "accountsTest.csv"
        newState.friends_file_name = 'friendsTest.csv'
        newState.users["UserName1"] = User(
            "first", "second", "Username1", "Password1!")
        assert newState.save_accounts() == True
        os.remove('accountsTest.csv')

    def test_saving_over_five_accounts(self):
        newState = State()

        try:
            os.remove('accountsTest.csv')
        except:
            pass

        newState.account_file_name = "accountsTest.csv"
        newState.users["UserName1"] = User(
            "first", "second", "Username1", "Password1!")
        newState.users["UserName2"] = User(
            "first", "second", "Username2", "Password1!")
        newState.users["UserName3"] = User(
            "first", "second", "Username3", "Password1!")
        newState.users["UserName4"] = User(
            "first", "second", "Username4", "Password1!")
        newState.users["UserName5"] = User(
            "first", "second", "Username5", "Password1!")
        newState.users["UserName6"] = User(
            "first", "second", "Username6", "Password1!")
        newState.save_accounts()
        assert newState.save_accounts() == True
        os.remove('accountsTest.csv')

    def test_saving_over_ten_accounts(self):
        newState = State()
        try:
            os.remove('accountsTest.csv')
        except:
            pass
        newState.account_file_name = "accountsTest.csv"
        newState.users["UserName1"] = User(
            "first", "second", "Username1", "Password1!")
        newState.users["UserName2"] = User(
            "first", "second", "Username2", "Password1!")
        newState.users["UserName3"] = User(
            "first", "second", "Username3", "Password1!")
        newState.users["UserName4"] = User(
            "first", "second", "Username4", "Password1!")
        newState.users["UserName5"] = User(
            "first", "second", "Username5", "Password1!")
        newState.users["UserName6"] = User(
            "first", "second", "Username6", "Password1!")
        newState.users["UserName7"] = User(
            "first", "second", "Username7", "Password1!")
        newState.users["UserName8"] = User(
            "first", "second", "Username8", "Password1!")
        newState.users["UserName9"] = User(
            "first", "second", "Username9", "Password1!")
        newState.users["UserName10"] = User(
            "first", "second", "Username10", "Password1!")
        newState.users["UserName11"] = User(
            "first", "second", "Username11", "Password1!")
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
        user = User("first", "second", "Username1", "Password1!")
        assert user.password == "Password1!"
        assert user.password != "Password1"

    def test_change_password(self):
        user = User("first", "second", "Username1", "Password1!")
        user.change_password("Password12@@")
        assert user.password == "Password12@@"

    def test_user_list(self):
        user = User("first", "second", "Username1", "Password1!")
        assert user.list() == ["first", "second", "Username1", "Password1!",
                               "", True, True, True, 0, "", "", "", "", "", "", "", ""]

    def test_user_success_story(self):
        user = User("first", "second", "Username1", "Password1!")
        user.set_success_story("Testing out this functionality")
        assert user.success_story == "Testing out this functionality"

    def test_job_creation(self):
        job = Job("python dev", "backend dev",
                  "Apple", "USA", "$100000", "typies")
        assert job.title == "python dev"
        assert job.description == "backend dev"
        assert job.employer == "Apple"
        assert job.location == "USA"
        assert job.salary == "$100000"
        assert job.poster == "typies"

    def test_change_langauge(self):
        user = User("first", "second", "Username1", "Password1!")
        user.change_language(0)
        assert user.language == 0

    def test_search(self):
        newState = State()
        searchPage = SearchStudents(state=newState)
        newState.users["user1"] = User('Sophia', 'Jones', 'sophie', 'password1',
                                       major='Computer Science', university='University of South Florida')
        newState.current_user = newState.users["user1"]
        newState.users["user2"] = User('John', 'Dinkleburg', 'dinkster', 'password2',
                                       major='Interpretive Dance', university='University of Central Florida')
        newState.users["user3"] = User('Bruce', 'Wayne', 'notbatman', 'password3',
                                       major='Business Administration', university='Florida Gulf Coast University')
        newState.users["user4"] = User('Peppino', 'Pizza', 'pizzafiend', 'password4',
                                       major='Culinary Arts', university='School of Hard Knocks')
        newState.users["user5"] = User('Bevin', 'Barker', 'angryimpala', 'password5',
                                       major='Music Theory', university='University of South Florida')
        assert searchPage.is_exists(
            lastname='Wayne') == newState.users["user3"]
        assert searchPage.is_exists(lastname="Jones") == None
        assert searchPage.is_exists(lastname='Hoeke') == None
        assert searchPage.is_exists(
            university='Florida Gulf Coast University') == newState.users["user3"]
        assert searchPage.is_exists(university='Harvard University') == None
        assert searchPage.is_exists(
            major='Culinary Arts') == newState.users["user4"]
        assert searchPage.is_exists(major="Mechanical Engineering") == None

    def test_friend_requests(self):
        self.monkeypatch.setattr('sys.stdin', io.StringIO('\n'))
        newState = State()
        newState.friends_file_name = 'friendsTest.csv'
        searchPage = SearchStudents(state=newState)
        friendsPage = Friends(state=newState)
        newState.users["sophie"] = User('Sophia', 'Jones', 'sophie', 'password1',
                                        major='Computer Science', university='University of South Florida')
        newState.current_user = newState.users["sophie"]
        newState.users["dinkster"] = User('John', 'Dinkleburg', 'dinkster', 'password2',
                                          major='Interpretive Dance', university='University of Central Florida')
        searchPage.send_request(newState.users["dinkster"].username)
        output = self.capsys.readouterr()
        # test that both users have the pending requests.
        assert newState.users["dinkster"].username in newState.current_user.sent_requests
        assert newState.current_user.username in newState.users["dinkster"].pending_requests

        # test accept_friend_request
        newState.current_user = newState.users["dinkster"]
        friendsPage.accept_request("sophie")
        output = self.capsys.readouterr()
        assert "sophie" in newState.current_user.friends
        assert "dinkster" in newState.users["sophie"].friends

        # test remove_friend
        friendsPage.remove_friend("sophie")
        output = self.capsys.readouterr()
        assert not ("sophie" in newState.current_user.friends)
        assert not ("dinkster" in newState.users["sophie"].friends)

        # test decline request
        searchPage.send_request(newState.users["sophie"].username)

        newState.current_user = newState.users["sophie"]
        friendsPage.decline_request("dinkster")
        output = self.capsys.readouterr()
        assert not ("dinkster" in newState.current_user.friends)
        assert not ("sophie" in newState.users["dinkster"].friends)
        assert not (
            newState.users["dinkster"].username in newState.current_user.sent_requests)
        assert not (
            newState.current_user.username in newState.users["dinkster"].pending_requests)

    def test_job_experience(self):
        job = Job("Product Dev. Intern", "Make stuff",
                  "Starbucks", "Florida", 60000, "typies")
        assert job.title == "Product Dev. Intern"
        assert job.description == "Make stuff"
        assert job.employer == "Starbucks"
        assert job.location == "Florida"
        assert job.salary == 60000
        assert job.poster == "typies"

    def test_user_list(self):
        user = User("Ty", "Piesco", "typies", "Password1!", "I am big success", True, True, True, 0, "Computer science", "University of South Florida",
                    "Student", "This is the about", "This is the experience", "This is the Education", "2020", "2024")
        assert user.first_name == "Ty"
        assert user.last_name == "Piesco"
        assert user.username == "typies"
        assert user.password == "Password1!"
        assert user.success_story == "I am big success"
        assert user.major == "Computer Science"  # Checks formatting
        assert user.university == "University Of South Florida"  # Checks formatting
        assert user.title == "Student"
        assert user.about == "This is the about"
        assert user.experience == "This is the experience"
        assert user.education == "This is the Education"
        assert user.university_start_year == "2020"
        assert user.university_end_year == "2024"

    def test_apply_for_job(self):
        newState = State()
        user1 = User("Ty", "Piesco", "typies", "Password1!", "I am big success", True, True, True, 0, "Computer science", "University of South Florida",
                     "Student", "This is the about", "This is the experience", "This is the Education1", "2019", "2023")
        user2 = User("First", "Last", "flast", "Password2!", "I am bigger success", True, True, True, 0, "Biology", "University of South Florida",
                     "Student", "This is the about", "This is the experience", "This is the Education2", "2020", "2024")
        job = Job("Job 1", "Description 1", "Employer 1",
                  "Location 1", "60000", user1.username)
        assert job.applications == {}  # Job has no applicants
        newState.current_user = user2
        newState.jobs = [job]
        newState.job_file_name = 'jobFileTest.csv'
        jobSearchPage = JobSearch(state=newState)
        jobSearchPage.jobs_to_display = [job]
        self.monkeypatch.setattr(
            'sys.stdin', io.StringIO('01/01/1991\n02/01/1991\nBecause I rock\n\n0\n'))  # stdin
        jobSearchPage.apply(0)
        assert job.applications != {}  # Job has a applicant

    def test_update_job_info(self):
        newState = State()
        user1 = User("Ty", "Piesco", "typies", "Password1!", "I am big success", True, True, True, 0, "Computer science", "University of South Florida",
                     "Student", "This is the about", "This is the experience", "This is the Education1", "2019", "2023")
        job = Job("Old Job Title", "Old Description", "Old Employer",
                  "Old Location", "60000", user1.username)
        newState.current_user = user1
        newState.jobs = [job]
        newState.job_file_name = 'jobFileTest.csv'
        manageJobsPage = ManageJobs(state=newState)
        manageJobsPage.user_jobs = [job]

        assert job.title == "Old Job Title"
        assert job.description == "Old Description"
        assert job.employer == "Old Employer"
        assert job.location == "Old Location"
        assert job.salary == "60000"
        self.monkeypatch.setattr(
            'sys.stdin', io.StringIO('1\nNew Job Title\n2\nNew Employer\n3\nNew Location\n4\nNew Description\n5\n70000\n'))
        manageJobsPage.update_job_info(0)
        manageJobsPage.update_job_info(0)
        manageJobsPage.update_job_info(0)
        manageJobsPage.update_job_info(0)
        manageJobsPage.update_job_info(0)
        assert job.title == "New Job Title"
        assert job.description == "New Description"
        assert job.employer == "New Employer"
        assert job.location == "New Location"
        assert job.salary == "70000"

    def test_apply_for_own_job(self):
        newState = State()
        user1 = User("Ty", "Piesco", "typies", "Password1!", "I am big success", True, True, True, 0, "Computer science", "University of South Florida",
                     "Student", "This is the about", "This is the experience", "This is the Education1", "2019", "2023")
        job = Job("Job 2", "Description 1", "Employer 1",
                  "Location 1", "60000", user1.username, {})
        assert job.applications == {}  # Job has no applicants
        newState.current_user = user1
        newState.jobs = [job]
        newState.job_file_name = 'jobFileTest.csv'
        jobSearchPage = JobSearch(state=newState)
        jobSearchPage.jobs_to_display = [job]
        self.monkeypatch.setattr(
            'sys.stdin', io.StringIO('01/01/1991\n02/01/1991\nBecause I rock\n\n0\n'))  # stdin
        jobSearchPage.apply(0)
        assert job.applications == {}  # Job has a applicant

    def test_apply_for_job_twice(self):
        newState = State()
        user1 = User("Ty", "Piesco", "typies", "Password1!", "I am big success", True, True, True, 0, "Computer science", "University of South Florida",
                     "Student", "This is the about", "This is the experience", "This is the Education1", "2019", "2023")
        user2 = User("First", "Last", "flast", "Password2!", "I am bigger success", True, True, True, 0, "Biology", "University of South Florida",
                     "Student", "This is the about", "This is the experience", "This is the Education2", "2020", "2024")
        job = Job("Job 1", "Description 1", "Employer 1",
                  "Location 1", "60000", user1.username, {})
        assert job.applications == {}  # Job has no applicants
        newState.current_user = user2
        newState.jobs = [job]
        newState.job_file_name = 'jobFileTest.csv'
        jobSearchPage = JobSearch(state=newState)
        jobSearchPage.jobs_to_display = [job]
        self.monkeypatch.setattr(
            'sys.stdin', io.StringIO('01/01/1991\n02/01/1991\nBecause I rock\n\n0\n1\n\n0\n'))  # stdin
        jobSearchPage.apply(0)
        assert len(job.applications) == 1  # Job has a applicant
        jobSearchPage.apply(0)
        assert len(job.applications) == 1  # Applying twice did not work

    def test_rescind_application(self):
        newState = State()
        user1 = User("Ty", "Piesco", "typies", "Password1!", "I am big success", True, True, True, 0, "Computer science", "University of South Florida",
                     "Student", "This is the about", "This is the experience", "This is the Education1", "2019", "2023")
        user2 = User("First", "Last", "flast", "Password2!", "I am bigger success", True, True, True, 0, "Biology", "University of South Florida",
                     "Student", "This is the about", "This is the experience", "This is the Education2", "2020", "2024")
        job = Job("Job 1", "Description 1", "Employer 1",
                  "Location 1", "60000", user1.username, {})
        assert job.applications == {}  # Job has no applicants
        newState.current_user = user2
        newState.jobs = [job]
        newState.job_file_name = 'jobFileTest.csv'
        jobSearchPage = JobSearch(state=newState)
        jobSearchPage.jobs_to_display = [job]
        self.monkeypatch.setattr(
            'sys.stdin', io.StringIO('01/01/1991\n02/01/1991\nBecause I rock\n\n0\n0\n\n0\n'))  # stdin
        jobSearchPage.apply(0)
        assert len(job.applications) == 1  # Job has a applicant
        jobSearchPage.apply(0)
        assert len(job.applications) == 0  # Applying twice did not work

    def test_creating_account(self):
        newState = State()
        newState.account_file_name = 'accounts.csv'
        user = User("Ty", "Piesco", "typies", "Password1!", "I am big success", True, True, True, 0, "Computer science",
                    "University of South Florida",
                    "Student", "This is the about", "This is the experience", "This is the Education", "2020", "2024")

        createAccountPage = CreateAccount(state=newState)
        self.monkeypatch.setattr(
            'sys.stdin', io.StringIO('Alex\nHathway\nalexhathway\nCS\nMIT\ny\nABCabc123!\n\n'))  # stdin
        createAccountPage.create_new_account()
        assert newState.users["alexhathway"].user_tier == "plus"

    def test_send_message_standard(self):
        newState = State()
        newState.message_file_name = 'messages.csv'
        newState.users["UserName1"] = User(
            "first", "second", "Username1", "Password1!")
        newState.users["UserName2"] = User(
            "first", "second", "Username2", "Password1!")
        newState.users["UserName2"].friends.append("UserName1")
        newState.current_user = newState.users["UserName2"]
        self.monkeypatch.setattr(
            'sys.stdin', io.StringIO('UserName1\nHello World\n\n'))  # stdin
        sendMessagePage = SendMessage(state=newState)
        sendMessagePage.send_message()
        assert len(newState.messages) > 0

    def test_send_message_plus(self):
        newState = State()
        newState.message_file_name = 'messages.csv'
        newState.users["UserName1"] = User(
            "first", "second", "Username1", "Password1!")
        newState.users["UserName2"] = User(
            "first", "second", "Username2", "Password1!")
        newState.users["UserName2"].user_tier = "plus"
        newState.current_user = newState.users["UserName2"]
        self.monkeypatch.setattr(
            'sys.stdin', io.StringIO('UserName1\nHello World\n\n'))  # stdin
        sendMessagePage = SendMessage(state=newState)
        sendMessagePage.send_message()
        assert len(newState.messages) > 0

    def test_fail_send_message_non_friend_standard(self):
        newState = State()
        newState.message_file_name = 'messages.csv'
        newState.users["UserName1"] = User(
            "first", "second", "Username1", "Password1!")
        newState.users["UserName2"] = User(
            "first", "second", "Username2", "Password1!")
        newState.current_user = newState.users["UserName2"]
        self.monkeypatch.setattr(
            'sys.stdin', io.StringIO('UserName1\nHello World\n\n'))  # stdin
        sendMessagePage = SendMessage(state=newState)
        sendMessagePage.send_message()
        assert len(newState.messages) == 0

    def test_receive_message(self):
        newState = State()
        newState.message_file_name = 'messages.csv'
        newState.users["UserName1"] = User(
            "first", "second", "UserName1", "Password1!")
        newState.users["UserName2"] = User(
            "first", "second", "Username2", "Password1!")
        newState.users["UserName2"].user_tier = "plus"
        newState.current_user = newState.users["UserName2"]
        self.monkeypatch.setattr(
            'sys.stdin', io.StringIO('UserName1\nHello World\n\n'))  # stdin
        sendMessagePage = SendMessage(state=newState)
        sendMessagePage.send_message()

        newState.current_user = newState.users["UserName1"]
        inboxPage = Inbox(state=newState)
        inboxPage.load_messages()
        assert len(inboxPage.loaded_messages) > 0

    def test_keep_inbox_message(self):
        newState = State()
        newState.message_file_name = 'messages.csv'
        newState.users["UserName1"] = User(
            "first", "second", "UserName1", "Password1!")
        newState.users["UserName2"] = User(
            "first", "second", "Username2", "Password1!")
        newState.users["UserName2"].user_tier = "plus"
        newState.current_user = newState.users["UserName2"]
        self.monkeypatch.setattr(
            'sys.stdin', io.StringIO('UserName1\nHello World\n\n'))  # stdin
        sendMessagePage = SendMessage(state=newState)
        sendMessagePage.send_message()

        newState.current_user = newState.users["UserName1"]
        inboxPage = Inbox(state=newState)
        inboxPage.load_messages()
        assert len(inboxPage.loaded_messages) > 0

        self.monkeypatch.setattr(
            'sys.stdin', io.StringIO('1\n1\nkeep\n\n'))  # stdin

        assert len(inboxPage.loaded_messages) > 0

    def test_delete_inbox_message(self):
        newState = State()
        newState.message_file_name = 'messages.csv'
        newState.users["UserName1"] = User(
            "first", "second", "UserName1", "Password1!")
        newState.users["UserName2"] = User(
            "first", "second", "Username2", "Password1!")
        newState.users["UserName2"].user_tier = "plus"
        newState.current_user = newState.users["UserName2"]
        self.monkeypatch.setattr(
            'sys.stdin', io.StringIO('UserName1\nHello World\n\n\n'))  # stdin
        sendMessagePage = SendMessage(state=newState)
        sendMessagePage.send_message()

        newState.current_user = newState.users["UserName1"]
        inboxPage = Inbox(state=newState)
        inboxPage.load_messages()
        assert len(inboxPage.loaded_messages) > 0

        self.monkeypatch.setattr(
            'sys.stdin', io.StringIO('1\n1\ndelete\n\n'))  # stdin

        assert len(newState.messages) == 1

    def test_reply_inbox_message(self):
        newState = State()
        newState.message_file_name = 'messages.csv'
        newState.users["UserName1"] = User(
            "first", "second", "UserName1", "Password1!")
        newState.users["UserName2"] = User(
            "first", "second", "Username2", "Password1!")
        newState.users["UserName2"].user_tier = "plus"
        newState.current_user = newState.users["UserName2"]
        self.monkeypatch.setattr(
            'sys.stdin', io.StringIO('UserName1\nHello World\n\n\n'))  # stdin
        sendMessagePage = SendMessage(state=newState)
        sendMessagePage.send_message()

        newState.current_user = newState.users["UserName1"]
        inboxPage = Inbox(state=newState)
        inboxPage.load_messages()
        assert len(inboxPage.loaded_messages) > 0

        self.monkeypatch.setattr(
            'sys.stdin', io.StringIO('1\n1\nreply\nHello Back\n\n'))  # stdin
        assert len(newState.messages) == 1

    def test_saved_jobs(self):
        newState = State()
        newState.account_file_name = 'testAccounts.csv'
        newState.users["UserName1"] = User("first","second","UserName1","Password1!")
        newState.current_user = newState.users["UserName1"]
        newState.jobs.append(Job("Cool Job","Cool Job!","Cool employer",
                                 "cool location","cool salary", "coollad",
                                 {},"cool id"))
        jobSearchPage = JobSearch(title="cool",login_required=False,state=newState,parent=None)
        jobSearchPage.jobs_to_display = newState.jobs.copy()
        jobSearchPage.save_job(0)
        assert newState.current_user.saved_jobs == ["cool id"]
        jobSearchPage.unsave_job(0)
        assert newState.current_user.saved_jobs == []
        pass
