#Quiz Game SOB:28, 29 ,30 MINI PROJECT
#This trivia is based on some general UAE questions.
#User will get an option to play the quiz or exit, if he/she choose to play then they will get a random question, for which user can answer (the answer can be in any case)
#User will get appropriate message after each question.
import random #this is to import random module in the code.

def quiz(question,answer):  #function quiz defined to get the question and check it's answer 
    randomInteger = random.randint(0,15) #randomInteger variable to give the random number of the questions to display
    print("Question : ")
    print(question[randomInteger])  #Random question will be printed according to the random number (randomInteger)
    userAnswer = str(input("Please Enter Answer : "))   #taking the answer input from the user
    answerLower=userAnswer.lower()            #converting the user's answer into lowercase, so the user can enter the answer in any case(lower or upper) 
    if(answerLower == answer[randomInteger]):      #Checking if the answer is correct 
        print("Wohoo, Answer is Correct!!!")
    else:
        print("Ooops, wrong answer!")
    

#menu Function for displaying the menu
def menu(): #menu function is defined to print the options for the user
    print(" ______________________________")
    print("|          Quiz Game           |")
    print("|______________________________|")
    print("|  0. Exit the game            |")
    print("|  1. Continue Playing         |")
    print("|______________________________|")

#Project function to call menu function and decide which function to call
def project(question,answer):
    #Running infinite loop so that user can use options multiple times
    while(True):   #the loop will be infinite until the user breaks it.
        
        #Calling the menu function from which user can choose
        menu()
        #Taking the input of user's choice from menu
        optionSelected = int(input("Please Enter Your Choice : "))  
        #If the user chooses 0 then we will exit the program
        if(optionSelected == 0):
            print("Thank you for playing!")
            break
        #If the user selects 1 then continuing the loop again
        elif(optionSelected == 1):
            quiz(question,answer)  #initialising quiz function
        else:
            print("Wrong Input! Please enter a valid option ")
            continue  #the loop will be continued if wrong input is there.

question = ["How many emirates are there in UAE?" ,"Which is the official language of UAE?","The National Day of UAE is on?","The UAE dirham was introduced in the year","Which is the second most largest Emirates by area wise in UAE","Which is the largest port in UAE? ","Which is recognized as National Bird of UAE"," In which year Burj Khalifa was opened for public?","Which is the most populated city in UAE","What is the capital of UAE?", "what is the largest city of UAE?", "National dish of emirates?", "What is the dialing code of UAE?","UAE was established in which year?", "Who was the first President of the UAE"]
answer = ["7","arabic","2nd December","1973","dubai","jebel ali","Falcon","2010","dubai", "abu dhabi", "abu dhabi", "kabsa", "+971","1971","zayed bin sultan al nahyan"]
project(question,answer) #initiating the project function



