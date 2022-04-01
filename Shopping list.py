#Inports
import time
#Functions
#Display list code
def DisplayList ():
    global list
    for i in list:
        print(i)
#Add to list code
def AddList ():
    global list
    add = input("Enter what you would like to add. \nType skip if you would not like to add anything\nEnter here: ")
    if add == "skip" or add == "Skip":
        print("Nothing is added")
        time.sleep(1)
    elif list.count(add) == 1:
        print("You already have this item")
    else:
        list.append(str(add))
        DisplayList()
        time.sleep(1)
#remove from list code
def RemoveList ():
    remove = input("Is there anything you would like to remove?\nIf there is nothing enter 'skip'\nEnter here: ")
    if remove == "skip" or remove == "Skip":
        print("Nothing is removed")
        DisplayList()
        time.sleep(1)
    else:
        list.remove(remove)
        DisplayList()
        time.sleep(1)



print("Welcome to your shopping list.\n")
time.sleep(1)
#My list
list = []
#Define varribles
x = True

#Main Code
while x == True:

    AddList()
    time.sleep(1)
    RemoveList()
    view = input("Do you want to view the list?: ")
    if view == "yes" or view == "Yes":
        DisplayList()
        time.sleep(2)
    else:
        end = input("Are you done the list?: ")
        if end == "yes" or end == "Yes":
            x = False
