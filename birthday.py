with open("birthday.txt", "r") as file:
    content = file.read()
    print(content)

with open("birthday.txt", "w") as file:
    file.write("4/8/10")
    # print(file.read)



# with open("birthday.txt", "w") as file:
#     def addtext(birthday):
#         print(f"Friend - {birthday}")

# addtext("4/9/10")