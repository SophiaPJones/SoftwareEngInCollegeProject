#!/usr/bin/env python3

class Job():
    def __init__(self, title, description, employer, location, salary):
        self.title = title
        self.description = description
        self.employer = employer
        self.location = location
        self.salary = salary
    def list(self):
        return [self.title, self.description, self.employer, self.location, self.salary]
