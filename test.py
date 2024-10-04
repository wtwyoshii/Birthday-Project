def read_data():
    with open("data.txt", "r") as file:
        content = file.read()
        print(content)

read_data()