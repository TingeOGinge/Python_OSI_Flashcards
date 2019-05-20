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
        Layer(1, "Physical", "Send data on to the physical wire"),
        Layer(2, "Data", "Reads the MAC address from the data packet"),
        Layer(3, "Network", "Reads the IP address from the packet"),
        Layer(4, "Transport", "Responsible for the transport protocol and error handling"),
        Layer(5, "Session", "Establishes/ends connections between two hosts"),
        Layer(6, "Presentation", "Formats the data so that it can be viewed by the user. Encrypt and decrypt."),
        Layer(7, "Application", "Services that are used with end user applications")
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