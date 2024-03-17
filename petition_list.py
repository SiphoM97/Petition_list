# This is a program that allows people to enter their name on a list, till the list reaches 200 names.

petition_list = []

while len(petition_list) < 10:
    name = input("Enter your name here: ")
    surname = input("Enter your surname here: ")
    sign = input("Type 'yes' to sign the petition: ")

    if sign.lower() == "yes":
        petition_list.append((name, surname))
        print("Thank you for signing the petition")
    else:
        print("You chose not to sign the petition")

    if len(petition_list) == 10:
        print("We have reached our goal! Thank you for participating.")
        break

print("Signed petition list:")
for i, signer in enumerate(petition_list, start=1):
    print(f"{i}. {signer[0]} {signer[1]}")
