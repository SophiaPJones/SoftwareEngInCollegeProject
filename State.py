#!/usr/bin/env python3
import csv
import User
import Job
import Util
from typing import Any


class State:
    def __init__(self):
        self.users = {}
        self.account_file_name = ''
        self.job_file_name = ''
        self.friends_file_name = ''
        self.experience_file_name = ''
        self.current_user = None
        self.application_active = True
        self.current_page = None
        self.root = None
        self.jobs = []
        self.success_stories = {}

    def load_accounts(self):
        try:
            # import pdb; pdb.set_trace()
            with open(self.account_file_name, encoding="utf8") as csvFile:
                # lines = list(line for line in (l.strip() for l in csvFile) if line)  # skip blank lines
                accountList: Any = csv.reader(csvFile, delimiter=',')
                for account in accountList:
                    if account == []:
                        continue
                    account[5] = account[5] == "True"
                    account[6] = account[6] == "True"
                    account[7] = account[7] == "True"
                    account[8] = account[8] == "True"
                    self.users[account[2]] = User.User(
                        *account)  # Uni end year
            # self.load_friends()
            return True
        except:
            # No accounts file
            return False

    def save_accounts(self):
        if len(self.users) <= Util.MAXIMUM_USER_COUNT:
            with open(self.account_file_name, 'w', encoding="utf8") as target:
                writer = csv.writer(target)
                for account in list(self.users.keys()):
                    accountlist = self.users[account].list()

                    # replacing newlines and commas with uncommon alternative separator characters
                    # for i, item in enumerate(accountlist):
                    #     if(isinstance(item,str)):
                    #         print(item)
                    #         accountlist[i] = item.replace('\n', Util.REPLACE_NEWLINE_CHAR)
                    #         accountlist[i] = item.replace(',', Util.REPLACE_COMMA_CHAR)
                    #         print("*****")
                    #         print(accountlist[i])
                    writer.writerow(accountlist)
            target.close()
            # self.save_friends()
            return True
        else:
            print("All permitted accounts have been created, please come back later.\n")
            return False

    def save_jobs(self):
        if len(self.users) <= Util.MAXIMUM_JOB_COUNT:  # maybe self.jobs
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
                job_list = csv.reader(csvFile, delimiter=',')
                for job in job_list:
                    self.jobs.append(Job.Job(
                        job[1],
                        job[2],
                        job[3],
                        job[4],
                        job[5],
                        job[6]
                    ))
                return True
        except:
            return False

    def load_success_stories(self):
        if self.users != {}:
            self.success_stories = {key: val.success_story for key,
                                    val in self.users.items() if val.success_story != ""}

    # friends
    def save_friends(self):
        with open(self.friends_file_name, 'w+') as target:
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
                # lines = list(line for line in (l.strip() for l in csvFile) if line)  # skip blank lines
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
                        self.users[username].sent_requests.append(friend)
                    elif status == "pending":
                        self.users[username].pending_requests.append(friend)
                return True
        except:
            return False

    def load_experience(self):
        try:
            # import pdb; pdb.set_trace()
            with open(self.experience_file_name, 'r') as csvFile:
                experiences = csv.reader(csvFile, delimiter=',')
                for exp in experiences:
                    username = exp[0]
                    if username in self.users:
                        self.users[username].previous_jobs.append(User.JobExperience(
                            username, exp[1], exp[2], exp[3], exp[4], exp[5], exp[6]))
                    else:
                        raise Exception(
                            "Invalid user in job experience; make sure accounts have already been loaded.")
                return True
        except:
            return False

    def save_experience(self):
        try:
            with open(self.experience_file_name, 'w+') as csvFile:
                experiences = csv.writer(csvFile, delimiter=',')
                for user in self.users:
                    for job in self.users[user].previous_jobs:
                        experiences.writerow(job.list())

            return True
        except:
            return False
