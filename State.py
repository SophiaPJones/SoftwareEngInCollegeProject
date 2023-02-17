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
        self.current_user = None
        self.application_active = True
        self.current_page = None
        self.root = None
        self.jobs = []
        self.success_stories = {}

    def load_accounts(self):
        try:
            with open(self.account_file_name, encoding="utf8") as csvFile:
                lines = list(line for line in (l.strip()
                             for l in csvFile) if line)  # skip blank lines
                accountList = csv.reader(lines, delimiter=',')
                for account in accountList:
                    self.users[account[2]] = User.User(
                        account[0],  # first name
                        account[1],  # last name
                        account[2],  # username
                        account[3])  # password
                    account[4] = account[4].replace('\u2063', '\n')
                    account[4] = account[4].replace('\u2064', ',')
                    self.users[account[2]].set_success_story(
                        account[4])  # success story

                pass
        except:
            return

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
            self.success_stories = {key: val.success_story for key,
                                    val in self.users.items() if val.success_story != ""}
