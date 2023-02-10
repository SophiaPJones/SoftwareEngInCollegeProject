#!/usr/bin/env python3
import csv
import User
import Util


class State:
    def __init__(self):
        self.users = {}
        self.account_file_name = ''
        self.current_user = None
        self.application_active = True
        self.current_page = None
        self.root = None

    def load_accounts(self):
        try:
            with open(self.account_file_name) as csvFile:
                lines = list(line for line in (l.strip()
                             for l in csvFile) if line)  # skip blank lines
                accountList = csv.reader(lines, delimiter=',')
                for account in accountList:
                    self.users[account[2]] = User.User(
                        account[0], account[1], account[2], account[3])
                pass
        except:
            return

    def save_accounts(self):
        if len(self.users) <= Util.MAXIMUM_USER_COUNT:
            with open(self.account_file_name, 'w') as target:
                writer = csv.writer(target)
                for account in list(self.users.keys()):
                    writer.writerow(self.users[account].list())

            target.close()
            return True
        else:
            print("All permitted accounts have been created, please come back later.\n")
            return False
