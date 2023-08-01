import os

folder_name = "../journal"

user_date = input("Enter today's date: ")
user_mood = input("How do you rate your mood today from 1 to 10? ")
user_thoughts = input("Let your thoughts flow:\n")

if not os.path.exists(folder_name):
    os.mkdir(folder_name)

file_path = os.path.join(folder_name, user_date + ".txt")

with open(file_path, 'w') as fh:
    fh.write(user_mood + 2 * '\n')
    fh.write(user_thoughts)