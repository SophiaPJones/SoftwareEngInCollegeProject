from Util import *
import pytest


def test_contains_capital_letter():
    assert contains_capital_letter('Squeaky1!') == True
    assert contains_capital_letter('squEaky1!') == True
    assert contains_capital_letter('squeaky1!') == False


def test_contains_number():
    assert contains_number('Squeaky0!') == True
    assert contains_number('Squ1eaky!') == True
    assert contains_number('Sque2aky!') == True
    assert contains_number('Sq3ueaky!') == True
    assert contains_number('S4queaky!') == True
    assert contains_number('5Squeaky!') == True
    assert contains_number('Squeak6y!') == True
    assert contains_number('Sq7ueaky!') == True
    assert contains_number('Squeaky8!') == True
    assert contains_number('Squeak9y!') == True
    assert contains_number('Squeaky!') == False


def test_contains_special_character():
    assert contains_special_character('Squeaky1!') == True
    assert contains_special_character('Sq@ueaky1') == True
    assert contains_special_character('Sq#ueaky1') == True
    assert contains_special_character('Squeak$y1') == True
    assert contains_special_character('S%queaky1') == True
    assert contains_special_character('Squeak^y1') == True
    assert contains_special_character('&Squeaky1') == True
    assert contains_special_character('Squea*ky1') == True
    assert contains_special_character('S(queaky1') == True
    assert contains_special_character('Squeaky1') == False


def test_validate_password():
    assert validate_password('Squeaky1!') == True
    assert validate_password('squeaky2!') == False
    assert validate_password('Squeaky!') == False
    assert validate_password('Squeaky3') == False
