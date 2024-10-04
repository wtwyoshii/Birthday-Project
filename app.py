import datetime

def load_birthdays(filepath):
    birthdays = {
        
    }
    with open(filepath, "r") as file:
        for line in file:
            name, date = line.strip().split(', ')
            birthdays[name] = date
    return birthdays
print(load_birthdays("data.txt"))