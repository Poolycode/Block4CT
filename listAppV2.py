"""
Program Goals:
1. Get the input from the user!
2. Convert that input to an INT
3. Add that input to a list
4. Pull values from specific index positions
"""

#This line makes it so that I can use random
import random
#This line makes a list called myList
myList = []
#This line makes a list called unique_list
unique_list = []
#This line makes a function called mainProgram 
def mainProgram():
#This is a function that calls other functions if the user inputs difrent things to answer what the computer has printed
    while True:
        try:
            print("Hello, there! Let's work with lists!")
            print("Chose one of the following options.   Type a number ONLY!")
            choice = input("""1. Add to list,
2. Add a bunch of numbers
3. Get an item at an index
4. Sort list
5. Random Search
6. Liear Search
7. Recursive Binary Search
8. Iterative Binary Search
9. Print List
10. Quit    """)
            if choice == "1":
                addToList()
            elif choice == "2":
                addABunch()
            elif choice == "3":
                indexValues()
            elif choice == "4":
                sortList(myList)
            elif choice == "5":
                randomSearch()
            elif choice == "6":
                linearSearch()
            elif choice == "7":
                binsearch = input("What number are you looking for?   ")
                recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(binSearch))
            elif choice == "8":
                binSearch = input("What number are you looking for?  ")
                result = iterativeBinarySearch(unique_list, int(binSearch))
                if result != -1:
                    print("your number is at index posionion {}".format(result))
                else:
                    print("Your number is not found in that list.")
            elif choice == "9":
                printLists()
            else:
                break
        except:
            print("There was an error")
#This function is called to if the users input is "1". This function just adds the users input to the list myList.
def addToList():
    print("Adding to a list! Great choice!")
    newItem = input("please type an intager!    ")
    myList.append(int(newItem))
    #we need to think about errors!
#This function is called to if the users input is "2". This function adds numToAdd amount of numbers that are random and in range of numRange.
def addABunch():
    print("We're gonna add a bunch of numbers to your list!")
    numToAdd = input("How many integers do you want to add?   ")
    numRange = input("And how high would you like these numbers to go?   ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0,int(numRange)))
    print("Your list is now complete!")
#This function is called to if the users input is "4". This function sorts the list myList by putting all of the items in order starting at 1 into the list unique_list and skiping any numbers if there is a repeat of a number
def sortList(myList):
    #note that this is the first function we"ve build here that takes ARGUMENTS
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = input("Would you like to see the unique calues in your list?   Y/N    ")
    if showMe.lower() == "y":
        print(unique_list)
#This function is called to if the users input is "3". This function prints the number at an inxed position inputed by the user.
def indexValues():
    print("At what index position do you want to search?")
    indexPos = input("Type an indec position here:    ")
    print(myList[int(indexPos)])
#This function is called to if the users input is "5". This function prints a random number in the list myList.
def randomSearch():
    print("oH iM sO rAnDom!!!")
    print(myList[random.randint(0, len(myList)-1)])
    if len(unique_list) > 0:
        print(unique_list[random.randint(0, len(unique_list)-1)])
#This function is called to if the users input is "6". This function searches every number to see if it matches the users input and if so it prints the index postion of that number
def linearSearch():
    print("We're going to search through this list one item at a time!")
    searchValue = input("What are you looking for?  ")
    for x in range(len(myList)):
        if myList[x] == int(searchValue):
            print("Your item is at index position {}".format(x))
#This function is called to if the users input is "9". This function prints eather myList or unique_list baised on the input of the user.
def printLists():
    if len(unique_list) == 0:
        print(myList)
    else:
        whichOne = input("Which list do you want to see, sorted or un-sorted?   ")
        if whichOne.lower() == "sorted":
                         print(unique_list)
#This function is called to if the users input is "7". This function finds the middle of the list unique_list and if the input of the user is greater than the mid of unique list then it finds -
# the middle of the new section witch is where low is equal to the last mid and high is equal to the highest number and then sees if the new mid is greater, less than, or equal to the users input-
# and it keeps on going on until the new mid is equal to the users input and if it gets to a plave where a number is both the high and low and that is not the users input then it prints your number is not here.
# this function is recursive unlike the function below
def recursiveBinarySearch(unique_list, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if uniquelist[mid] == x:
            print("Your number is at position {}".format(mid))
        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, mid - 1, x)
        else:
            return recursiveBinarySearch(unique_list, mid + 1, high, x)
    else:
        print("your number isn't here!")
#This function is called to if the users input is "8". This function finds the middle of the list unique_list and if the input of the user is greater than the mid of unique list then it finds -
# the middle of the new section witch is where low is equal to the last mid and high is equal to the highest number and then sees if the new mid is greater, less than, or equal to the users input-
# and it keeps on going on until the new mid is equal to the users input and if it gets to a plave where a number is both the high and low and that is not the users input then it prints your number is not here.
# this function is not recurseve but is a while loop unlike the function above
def iterativeBinarySearch(unique_list, x):
    low = 0
    high = len(unique_list) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if unique_list[mid] < x:
            low = mid +1

        elif unique_list[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

# I think that this basicly ends and makes this whole program one whole piece.
if __name__ == "__main__":
    mainProgram()
    
