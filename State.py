#!/usr/bin/env python3
class State:
    def __init__(self):
        self.users = {}
        self.current_user = None
        self.application_active = True
        self.current_page = None
        self.root = None
