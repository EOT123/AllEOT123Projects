print("")
print("")
print("Welcome to your Contacts Manager")

print("This is a persistent database manager which will allow you to: ")

mycontacts = []
userchoice = 0

while userchoice != 4:
    print ("")
    print("1) Add Contacts")
    print("2) Look Up A Contact")
    print("3) Display All Contacts")
    print("4) Exit Contacts Manager")
    userchoice = eval(input())

    if userchoice == 1:
        print("")
        print("Adding A Contact To Your Database")
        name = input ("Enter Your Contact Name: First Last (No Commas)")
        email = input ("Enter A Contact Email: ")
        phone = input ("Enter Contact Phone Number: ")
        mycontacts.append([name, email, phone])

    elif userchoice == 2:
        print("")
        print("Looking Up Contact")
        keyword = input("Enter Lookup Term: ")
        for checker in mycontacts:
            if keyword in checker:
                print(checker)
            else:
                print ("That Term Does Not Exist In Your Contacts")
    elif userchoice == 3:
        print(mycontacts)
    elif userchoice == 4:
        print("")
        print("Exiting Contact Manager")
    else:
        print("Invalid Response")
outfile = open("Data01", "a")
for checker in mycontacts:
    outfile.write(",".join(checker) + "\n")
    outfile.close()
