#!/usr/bin/env python3

MINIMUM_PASSWORD_LENGTH = 8
MAXIMUM_PASSWORD_LENGTH = 12
MAXIMUM_USER_COUNT = 5


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
