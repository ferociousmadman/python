# ----------------------------------------------------------------------
# Author: Skipper Davies
# Date: 3-21-22
#
# This program asks the user for input for the password
# they want to create. This input is passed to a function, along
# with a salt. The salt is appended to the password and then sha256
# encryption is used to hash the password. NOTE: What I have written
# below is NOT a secure way to do this, and this code should NEVER
# be used to protect someone's password before storing it in a database.
# This program is for demonstrational purposes only. 
# ----------------------------------------------------------------------

import os
import hashlib

password_chosen_by_user = input("Choose your password ")


Salt = os.urandom(32).hex()

def salted_password(password_chosen_by_user, Salt):

    password_chosen_by_user = password_chosen_by_user + Salt
    password_chosen_by_user = hashlib.sha256(password_chosen_by_user.encode('utf-8')).hexdigest()
    
    return password_chosen_by_user




password_chosen_by_user = salted_password(password_chosen_by_user, Salt) 
print(password_chosen_by_user)