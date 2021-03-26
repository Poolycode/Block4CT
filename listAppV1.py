"""
Program Goals:
1. Get the input from the user!
2. Convert that input to an INT
3. Add that input to a list
4. Pull values from specific index positions
"""

#create functions that will perform those actions above
import random

myList = []
unique_list = []

def mainProgram():
    while True:
        try:
            print("Hello, there! Let's work with lists!")
            print("Chose one of the following options.   Type a number ONLY!")
            choice = input("""1. Add to list,
2. Add a bunch of numbers
3. Return the number at an index position
4. Sort list
5. Random Choice
6. Liear Search
7. PrintLists
8. End program    """)
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
                printLists()
            else:
                break
        except:
            print("An error occurred")
        
def addToList():
    newItem = input("please type an intager!    ")
    myList.append(int(newItem))
    print(myList)

def addABunch():
    print("We're gonna add a bunch of numbers!")
    numToAdd = input("How many integers do you want to add?   ")
    numRange = input("And how high would you like these numbers to go?   ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0,int(numRange)))
    print("Your list is now complete!")


def sortList(myList):
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = input("Wanna see your new list?   Y/N    ")
    if showMe.lower() == "y":
        print(unique_list)


def indexValues():
    indexPos = input("What index position would you like to look at?")
    print(myList[int(indexPos)])
        
def randomSearch():
    print("Here's a random value from your list!")
    print(myList[random.randint(0, len(myList)-1)])

def linearSearch():
    print("We're going to search through the IN THE WORST WAY POSSINLE!")
    searchItem = input("What are you looking for?  Number-wise?  ")
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            print("Your item is at index {}".format(x))
    print("Your number appeared {} times in the list".format(indexCount))

def recursiveBinarySearch(unique_list, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if uniquelist[mid] == x:
            print("On, what luck.   Your number is at position {}".format(mid))
        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, mid - 1, x)
        else:
            return recursiveBinarySearch(unique_list, mid + 1, high, x)

    else:
        print("your number isn't here!")

def printLists():
    if len(unique_list) == 0:
        print(myList)
    else:
        whichOne = input("Wich list? Sorted or un-sorted?   ")
        if whichOne.lower() == "sorted":
                         print(unique_list)

if __name__ == "__main__":
    mainProgram()
    
