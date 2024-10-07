#!/usr/bin/env python3

import re

# Function to validate email using regular expressions
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

# Function to validate password strength
def is_valid_password(password):
    return len(password) >= 8

# Function to validate gender input
def is_valid_gender(gender):
    return gender.lower() in ['male', 'female', 'other']

# Function to validate the form data
def register_user():
    fullname = input("Enter your full name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")
    gender = input("Enter your gender (male/female/other): ").lower()
    dob = input("Enter your date of birth (YYYY-MM-DD): ")

    # Validate email
    if not is_valid_email(email):
        print("Invalid email address.")
        return

    # Validate password
    if not is_valid_password(password):
        print("Password must be at least 8 characters long.")
        return

    # Check if passwords match
    if password != confirm_password:
        print("Passwords do not match.")
        return

    # Validate gender
    if not is_valid_gender(gender):
        print("Invalid gender. Please enter 'male', 'female', or 'other'.")
        return

    # Process registration
    print(f"Welcome, {fullname}! You have successfully registered.")
    print(f"Details:\nEmail: {email}\nGender: {gender.capitalize()}\nDate of Birth: {dob}")

# Call the function to handle registration
if __name__ == "__main__":
    register_user()
