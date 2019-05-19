from osi_flashcards_v2_classes import Layer
from random import *


def getNumberOfRounds():
    return int(input("How many times would you like to play? "))

def askQuestion(chosenLayer):
    if random() < 0.5:        
        userAnswer = input("Which layer of the OSI model does the following " +
            "sentence describe\n'{0}'\n".format(chosenLayer.getDescription()))
    else:
        userAnswer = input("The name of OSI layer #{0} is the ____ layer \n".format(
                        chosenLayer.getNumber()))
    return userAnswer

def checkAnswer(chosenLayer, userAnswer):
    if chosenLayer.getName() == userAnswer.title():
        return True
    return False

def printResult(chosenLayer, response, score, i):
    print("The correct answer was {0} \n".format(chosenLayer.getName()) + 
        "It seems you are {0} \nYour current score is {1}/{2} \n".format(
        response, score, i + 1))

def createOSIModel():
    return [
        Layer(1, "Physical", "Deals with the physical characteristics of the transmission medium (hardware)"),
        Layer(2, "Data", "Provides the functional and procedural means to transfer data between network entities"),
        Layer(3, "Network", "Defines how routing works and how routes are learned so that the packets can be delivered"),
        Layer(4, "Transport", "Regulates information flow to ensure end-to-end connectivity between host applications reliably and accurately"),
        Layer(5, "Session", "Defines how to start, control and end conversations between applications using dialogue control"),
        Layer(6, "Presentation", "Ensures that the information that the application layer of one system sends out is readable by the application layer of another system"),
        Layer(7, "Application", "Provides network services to the user’s applications. Synchronizes and establishes agreement on procedures for error recovery and control of data integrity")
    ]

def main():
    osiModel = createOSIModel()
    score = 0
    rounds = getNumberOfRounds()
    for i in range(rounds):
        chosenLayer = choice(osiModel)
        userAnswer = askQuestion(chosenLayer)
        response = "wrong :("
        if checkAnswer(chosenLayer, userAnswer):
            response = "correct!"
            score += 1
        printResult(chosenLayer, response, score, i)

main()