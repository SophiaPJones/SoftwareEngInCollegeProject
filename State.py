#!/usr/bin/env python3
import csv
import User
import Job
import Util

class State:
    def __init__(self):
        self.users = {}
        self.account_file_name = ''
        self.job_file_name = ''
        self.friends_file_name = ''
        self.current_user = None
        self.application_active = True
        self.current_page = None
        self.root = None
        self.jobs = []
        self.success_stories = {}

    def load_accounts(self):
        try:
            with open(self.account_file_name, encoding="utf8") as csvFile:
                lines = list(line for line in (l.strip() for l in csvFile) if line)  # skip blank lines
                accountList = csv.reader(lines, delimiter=',')
                for account in accountList:
                    self.users[account[2]] = User.User(
                        account[0],  # first name
                        account[1],  # last name
                        account[2],  # username
                        account[3],  # password
                        account[5],  # email permission
                        account[6],  # sms permission
                        account[7],  # targeted ad permission
                        account[8], # language
                        account[9], # major
                        account[10], # university
                        )  
                    account[4] = account[4].replace('\u2063', '\n')
                    account[4] = account[4].replace('\u2064', ',')
                    self.users[account[2]].set_success_story(account[4])  # success story
            self.load_friends()
        except:
            # No accounts file
            pass

    def save_accounts(self):
        if len(self.users) <= Util.MAXIMUM_USER_COUNT:
            with open(self.account_file_name, 'w', encoding="utf8") as target:
                writer = csv.writer(target)
                for account in list(self.users.keys()):
                    accountlist = self.users[account].list()

                    # replacing newlines and commas with uncommon alternative separator characters
                    accountlist[4] = accountlist[4].replace('\n', '\u2063')
                    accountlist[4] = accountlist[4].replace(',', '\u2064')

                    writer.writerow(accountlist)

            target.close()
            self.save_friends()
            return True
        else:
            print("All permitted accounts have been created, please come back later.\n")
            return False

    def save_jobs(self):
        if len(self.users) <= Util.MAXIMUM_JOB_COUNT:
            with open(self.job_file_name, 'w') as target:
                writer = csv.writer(target)
                for job in self.jobs:
                    job_list = job.list()
                    writer.writerow(job_list)
            target.close()
            return True
        else:
            print("All permitted jobs have been created, please come back later.\n")
            return False

    def load_jobs(self):
        try:
            with open(self.job_file_name) as csvFile:
                lines = list(line for line in (l.strip()
                             for l in csvFile) if line)  # skip blank lines
                job_list = csv.reader(lines, delimiter=',')
                for job in job_list:
                    self.jobs.append(Job.Job(
                        job[0],  # title
                        job[1],  # description
                        job[2],  # employer
                        job[3],  # location
                        job[4]  # salary
                    ))
                pass
        except:
            return
        

    def load_success_stories(self):
        if self.users != {}:
            self.success_stories = {key: val.success_story for key, val in self.users.items() if val.success_story != ""}

    # friends
    def save_friends(self):
        with open(self.friends_file_name, 'w') as target:
            writer = csv.writer(target)
            # user user2 status <pending, sent, friends>
            for user in self.users:
                # get the username
                username = self.users[user].username

                # now go through all the three lists, and add username, the one from the list and status
                for friends in self.users[user].friends:
                    writer.writerow([username, friends, "friends"])
                
                for sent in self.users[user].sent_requests:
                    writer.writerow([username, sent, "sent"])

                for pending in self.users[user].pending_requests:
                    writer.writerow([username, pending, "pending"])

        target.close()

    def load_friends(self):
        try:
            # open the file
            with open(self.friends_file_name, 'r') as csvFile:
                lines = list(line for line in (l.strip() for l in csvFile) if line)  # skip blank lines
                friend_list = csv.reader(lines, delimiter=',')
                for friend_ in friend_list:
                    # get the username
                    username = friend_[0]

                    # get the friend
                    friend = friend_[1]

                    # get the status
                    status = friend_[2]

                    # now add the friend to the correct list
                    if status == "friends":
                        self.users[username].friends.append(friend)
                    elif status == "sent":
                        print("sent")
                        self.users[username].sent_requests.append(friend)
                    elif status == "pending":
                        self.users[username].pending_requests.append(friend)
        except:
            return
        