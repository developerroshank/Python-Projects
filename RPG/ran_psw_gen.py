import random

char_of_pass = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*_()"

while True:
    len_of_pass = int(input("Enter the lenght Of Password : "))
    con_of_pass = int(input("Enter the number Of Password : "))

    for i in range(0, con_of_pass):
        password = ""
        for j in range(0, len_of_pass):
            pass_char = random.choice(char_of_pass)
            password += pass_char
        print("The Generated Password is : ", password)

    repeat = input("Do you want to Generate more password? (yes/no) : ")
    if repeat == "no" or repeat == "No":
        break
print("Thank You! ")

input("Thanku")
