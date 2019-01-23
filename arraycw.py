def main():
    # problem1()
    # problem2()
    # problem3()
    # problem4()
    # problem5()



def problem1():
    awesomePeeps = ["kenn", "Kevin", "Erin", "Meka"] #made an array

    print(awesomePeeps[2]) #printing the second element
    print(len(awesomePeeps)) #printing the length and how many inside
    awesomePeeps.remove("Kevin") #removing kevin
    print(awesomePeeps[2])

#
# Create a function with the variable below. After you create the variable do the instructions below that.
# ```
# arrayForProblem2 = ["Kenn", "Kevin", "Erin", "Meka"]
# ```
# a) Print the 3rd element of the numberList.
#
#     b) Print the size of the array
#
# c) Delete the second element.
#
#     d) Print the 3rd element.


def problem2():
    userInput = "" #making a blank input
    while(userInput != 'q'): #if its not equal to q it will continue to ask
        userInput = input("Enter something")


def problem3():
    nickNames = {   #this is my dictionary
            "johnathan" : "John",
            "Micheal":"Mike",
            "William":"Bill",
            "RObert":"Rob"
    }

    print(nickNames)  #printing all the objects
    print(nickNames["William"])  #printing william nick name

# Create a function that contains a collection of information for the following. After you create the collection do the instructions below that.
# ```
# Jonathan/John
# Michael/Mike
# William/Bill
# Robert/Rob
# ```
# a) Print the collection
#
# b) Print William's nickname




def problem4():

    rando = [23,34,45,7,89]   #my rando arrAay
    for elements in range(len(rando)-1,-1,-1): #making it go backwards
        print(rando[elements]) #printing the elements

    # Create an array of 5 numbers.
    # <strong>Using a loop</strong>, print the elements in the array reverse order.
    # <strong>Do not use a function</strong>
    #
    #
    #
    #
def problem5():
    higher = 0
    lower = 0    #setting my variables to zero
    equal = 0
    pickaNumber = [2,4,5,7,8]   #made my array
    userinput=int(input("Enter a number"))
    for eachEl in range(0,len(pickaNumber)-1,1):    #calling each number in the array
        if(userinput>pickaNumber[eachEl]):
            lower+=1
        elif(userinput==pickaNumber[eachEl]):   #comparing them to if its lkarger or maller
            equal+=1
        elif(userinput<pickaNumber[eachEl]):
            higher+=1
    print(higher)
    print(lower)  #printing each function
    print(equal)







    #
    # Create a function that will have a hard coded array then ask the user for a number.
    #     Use the userInput to state how many numbers in an array are higher, lower, or equal to it.
    #
    #









if __name__ == '__main__':
    main()