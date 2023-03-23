#!/usr/bin/env python3
import uuid


class Message():
    def __init__(self, sender, receiver, message):
        self.id = uuid.uuid4()
        self.sender = sender  # from
        self.receiver = receiver  # to
        self.message = message

    def list(self):
        return [self.id, self.sender, self.receiver, self.message]

    def str(self):
        return f"Sender: {self.sender}, Receiver: {self.receiver}, Message: {self.message}"
