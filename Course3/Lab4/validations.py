#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")

    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        return False
    # Usernames can only use letters, numbers, dots, and underscores
    if not re.match('^[a-zA-Z][a-zA-Z0-9._]*$', username):
        return False
    return True

def print_validation_result(username, minlen):
    is_valid = validate_user(username, minlen)
    if is_valid:
        print(f"True")
    else:
        print(f"False")

# Test cases
print_validation_result("blue.kale", 3)  # blue.kale is a valid username.
print_validation_result(".blue.kale", 3)  # .blue.kale is not a valid username.
print_validation_result("red_quinoa", 4)  # red_quinoa is a valid username.
print_validation_result("_red_quinoa", 4)  # _red_quinoa is not a valid username.

