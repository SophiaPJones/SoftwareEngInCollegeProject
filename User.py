#!/usr/bin/env python3

class User:
    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.success_story = ""
        pass

    def __string__(self):
        return f"{self.first_name},{self.last_name},{self.username},{self.password}"

    def change_password(self, new_password):
        self.password = new_password

    def list(self):
        return [self.first_name, self.last_name, self.username, self.password, self.success_story]

    def set_success_story(self, success_story):
        self.success_story = success_story
