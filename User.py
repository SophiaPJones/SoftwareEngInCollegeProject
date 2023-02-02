#!/usr/bin/env python3

class User:
    def __init__(self, username, password):
        self.username = username;
        self.password = password;
        pass
    def __string__(self):
        return f"{self.username},{self.password}";
    def change_password(self, new_password):
        self.password = new_password
