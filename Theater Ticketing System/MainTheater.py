# Caleb Herbel
# Theater Ticketing System
# The Art and Practice of Computer Science
# May 8, 2018

import theaterFunctions
import csv
import os.path

theaterMap = []
costOfRows = []
collumns = 0
rows = 0
keepRunning = True

#Checks if file exists. if file exists it parses data.
#If file doesn't exist, it prompts user to create a new theater.
if os.path.exists('theaterFile.csv'):
    fileInfo = theaterFunctions.openExistingProgram()
    rows = int(fileInfo[0])
    collumns = int(fileInfo[1])
    for row in range(0, rows):
        theaterMap.append([])
        for collumn in range(0, collumns):
            theaterMap[row].append(fileInfo[row+2][collumn])
    for pricesOfRow in range(0, rows):
        costOfRows.append(fileInfo[rows + 2][pricesOfRow])
else:
    rows = theaterFunctions.findRows()
    collumns = theaterFunctions.findCollumns()
    costOfRows = theaterFunctions.findCostOfRows(rows)
    theaterMap = theaterFunctions.buildMap(rows, collumns)

#Prompts user to make a decision.  
while keepRunning:
    print("\nPrint the letter of the action you would like.")
    print("A). Display a Seating chart.")
    print("B). Sell one or more tickets.")
    print("C). Display statistics.")
    print("R). Reset your Theater")
    print("Q). Save and Quit.")
    print("Which would you like to do?")
    decision = input("--> ")

    if decision.lower() == "a":
        #Display Seating Chart
        theaterFunctions.displaySeating(rows, collumns, theaterMap)
    elif decision.lower() == "b":
        #Sell Ticket
        theaterMap = theaterFunctions.sellSeat(rows, collumns, theaterMap)
    elif decision.lower() == "c":
        #Display Statistics
        theaterFunctions.displayStatistics(rows, collumns, theaterMap, costOfRows)
    elif decision.lower() == "r":
        #Reset Theater
        rows = theaterFunctions.findRows()
        collumns = theaterFunctions.findCollumns()
        costOfRows = theaterFunctions.findCostOfRows(rows)
        theaterMap = theaterFunctions.buildMap(rows, collumns)
    elif decision.lower() == "q":
        #Save and Quit
        theaterFunctions.saveProgram(rows, collumns, theaterMap, costOfRows)
        print("Have a Good Day!")
        keepRunning = False
    else:
        print("Invald Input")
