#!/usr/bin/env python3

import uuid;

class Application():
    def __init__(self, job_id, user, graduation_date, proposed_start_date, paragraph, id = None):
        if id == None:
            self.id = str(uuid.uuid4())
        else:
            self.id = id
        self.job_id = job_id
        self.user = user
        self.graduation_date = graduation_date
        self.proposed_start_date = proposed_start_date
        self.paragraph = paragraph
    def list(self):
        return [self.id, self.job_id, self.user, self.graduation_date, self.proposed_start_date, self.paragraph]
    def str(self):
        return f"{self.user}, {self.graduation_date}, {self.proposed_start_date}, {self.paragraph}"
