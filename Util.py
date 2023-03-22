#!/usr/bin/env python3
import os

MINIMUM_PASSWORD_LENGTH = 8
MAXIMUM_PASSWORD_LENGTH = 12
MAXIMUM_USER_COUNT = 10
MAXIMUM_JOB_COUNT = 5
MAXIMUM_FRIEND_COUNT = 10
REPLACE_NEWLINE_CHAR = '\u2063'
REPLACE_COMMA_CHAR = '\u2064'
MAXIMUM_EXPERIENCE_COUNT = 3
language_list = ["english", "spanish"]


def contains_capital_letter(string):
    return [c for c in string if c.isupper()] != []


def contains_number(string):
    return [c for c in string if c.isnumeric()] != []


def contains_special_character(string):
    return [c for c in string.replace(" ", "") if not c.isalnum()] != []


def validate_password(password):
    password_length_check = (len(password) >= MINIMUM_PASSWORD_LENGTH and len(
        password) <= MAXIMUM_PASSWORD_LENGTH)
    return (password_length_check and contains_capital_letter(password) and contains_number(password) and contains_special_character(password))


def clear_console():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def format_words(string):
    return string.title()
