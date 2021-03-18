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

def mainProgram():
    while True:
        try:
            print("Hello, there! Let's work with lists!")
            print("Chose one of the following options.   Type a number ONLY!")
            choice = input("""1. Add to list,
2. Add a bunch of numbers
3. Return the calue at an index position
4. Print contence of list
5. Random choice
6. Liear Search
7. End program    """)
            if choice == "1":
                addToList()
            elif choice == "2":
                addABunch()
            elif choice == "3":
                indexValues
            elif choice == "4":
                print(myList)
            elif choice == "5":
                randomSearch()
            elif choice == "6":
                linearSearch()
            else:
                break
        except:
            print("An error occurred")
        
def addToList():
    newItem = input("please type an intager!    ")
    myList.append(int(newItem))
    print(myList)

def addABunch():
    print("we're gonna add a bunch of numbers!")
    numToAdd = inpit("How many integers do you want to add?   ")
    num = input("And how high would you like these numbers to go?   ")
    for x in range(0, int(numberToAdd)):
        myList.append(random.randint(0,int(numRange)))
    print("Your list is now complete!")

def indexValues():
    indexPos = input("What index position would you like to look at?")
    print(myList[int(indexPos)])
        
def randomSearch():
    print("Here's a random value from your list!")
    print(myList[random.randint(0, len(myList)-1)])

def linearSearch():
    pring("we're going to search through the IN THE WORST WAY POSSINLE!")
    searchItem = input("What are you looking for?  Number-wise?  ")
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            print("Your item is at index {}".format(x))

if __name__ == "__main__":
    mainProgram()
    
