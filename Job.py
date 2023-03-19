#!/usr/bin/env python3
import itertools

class Job():
    new_id = itertools.count()
    def __init__(self, title, description, employer, location, salary, poster):
        self.id = next(Job.new_id)
        self.title = title
        self.description = description
        self.employer = employer
        self.location = location
        self.salary = salary
        self.poster = poster
    def list(self):
        return [self.id, self.title, self.description, self.employer, self.location, self.salary, self.poster]
    def str(self):
        return f"Title: {self.title}, Employer: {self.employer}, Location: {self.location}, Salary: {self.salary}"
