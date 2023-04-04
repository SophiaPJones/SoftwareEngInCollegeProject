#!/usr/bin/env python3
import uuid;

class Job():
    def __init__(self, title, description, employer, location, salary, poster, applications = {}, id = None):
        if id == None:
            self.id = str(uuid.uuid4())
        else:
            self.id = id
        self.title = title
        self.description = description
        self.employer = employer
        self.location = location
        self.salary = salary
        self.poster = poster
        self.applications = applications #maps usernames to application IDs
    def list(self):
        return [self.id, self.title, self.description, self.employer, self.location, self.salary, self.poster, self.applications]
    def str(self):
        return f"Title: {self.title}, Employer: {self.employer}, Location: {self.location}, Salary: {self.salary}"
