import csv

def displaySeating(rows, collumns, theaterMap):
    '''
    Displays theater map in an easy to read fashion.
    '''
    print("")
    #Prints Collumns at top of Map
    print("      Collumns")
    topNumbers = "      "
    botNumbers = "      "
    counter = 1
    for seat in range(collumns):
        if seat % 10 == 0 and seat > 0:
            topNumbers += str(int(seat/10))
        else:
            topNumbers += " "
    print(topNumbers)
    for seat in range(collumns):
        botNumbers += str(counter)
        counter += 1
        if counter == 10:
            counter = 0
    print(botNumbers)
    #converts theater map list into string and prints.
    for row in range(rows):
        stringRow = str(row + 1)
        if int(stringRow) < 10:
            newCollumn = "Row " + stringRow + " "
        else:
            newCollumn = "Row " + stringRow
        for seat in range(collumns):
            newCollumn = newCollumn + theaterMap[row][seat]
        print(newCollumn)

def sellSeat(rows, collumns, theaterMap):
    '''
    Gathers User Input to select seat for purchase with error checking.
    Returns TheaterMap with seat as marked sold.
    '''
    keepSelling = True
    while keepSelling:
        seatTaken = True
        while seatTaken:
            #Gather Input and Error Check for Row.
            correctInput = False
            while not correctInput:
                print("What row would you like your seat to be on: ")
                sellRow = input("--> ")
                try:
                    sellRow = int(sellRow) - 1
                except ValueError:
                    print("Invald input, Please Try Again.")
                    continue
                if sellRow < rows and sellRow >= 0:
                    correctInput = True
                else:
                    print("Invald input, Please Try Again.")
            #Gather Input and Error Check for Collumn.
            correctInput = False
            while not correctInput:
                print("What seat on that row would you like to buy: ")
                sellCollumn = input("--> ")
                try:
                    sellCollumn = int(sellCollumn) - 1
                except ValueError:
                    print("Invald input, Please Try Again.")
                    continue
                if sellCollumn < collumns and sellCollumn >= 0:
                    correctInput = True
                else:
                    print("Invald input, Please Try Again.")
            #Marks Seat as taken if available.
            if theaterMap[sellRow][sellCollumn] == "X":
                theaterMap[sellRow][sellCollumn] = "O"
                seatTaken = False
            else:
                print("This seat is already taken. Please try again.")
        validInput = False
        while not validInput:
            print("Would you like to buy another ticket?")
            buyAnotherTicket = input("y or n --> ")
            if buyAnotherTicket.lower() == "n":
                keepSelling = False
                validInput = True
            elif buyAnotherTicket.lower() == "y":
                validInput = True
            else:
                print("Invalid Input, Please Try Again")
    return theaterMap


def displayStatistics(rows, collumns, theaterMap, costOfRows):
    '''
    Displays number of seats sold along with current theater Revenue.
    '''
    counter = 0
    seatsSold = 0
    revenue = 0
    for row in range(rows):
        for seats in range(collumns):
            if theaterMap[row][seats] == "O":
                seatsSold += 1
                revenue = revenue + costOfRows[row]
    print("\nYou have sold ", seatsSold, " out of ", (rows * collumns), " seats.")
    print("Your current revenue is $",revenue)
    
def buildMap(rows, collumns):
    '''
    Builds a theater map to specified amound of rows and collumns.
    '''
    theaterMap = []
    theaterMapTemp = []
    #Creates single row.
    for seat in range(collumns):
        theaterMapTemp.append("X")
    #Appends duplicates row to create theater map.
    for row in range(rows):
        theaterMap.append(theaterMapTemp[:])

    return theaterMap

def findRows():
    '''
    :Gathers User Input for rows with error checking.
    :Returns rows.
    '''
    correctInput = False
    while not correctInput:
        print("How many rows Do you want your theater to have? (Max 99)")
        rows = input("--> ")
        try:
            rows = int(rows)
        except ValueError:
            print("Invald input, Please Try Again.")
            continue
        if rows < 100 and rows > 0:
                correctInput = True
        else:
            print("Invald input, Please Try Again.")
    return rows

def findCollumns():
    '''
    :Gathers User Input for collumns with error checking.
    :Returns collumns.
    '''
    correctInput = False
    while not correctInput:
        print("How many chairs do you want in each row? (Max 99)")
        collumns = input("--> ")
        try:
            collumns = int(collumns)
        except ValueError:
            print("Invald input, Please Try Again.")
            continue
        if collumns < 100 and collumns > 0:
                correctInput = True
        else:
            print("Invald input, Please Try Again.")
    return collumns
    
def findCostOfRows(rows):
    '''
    Gathers a price for each row with error checking.
    Returns list containing the cost of each row.
    '''
    costOfRows = []
    for row in range(rows):
        correctInput = False
        cost = 0
        while not correctInput:
            print("What would you like row", (row + 1), "to cost? (Less than $1000.)")
            cost = input("--> $")
            try:
                cost = float(cost)
            except ValueError:
                print("Invald input, Please Try Again.")
                continue
            if cost < 1000 and cost > 0:
                    correctInput = True
            else:
                print("Invald input, Please Try Again.")
        costOfRows.append(cost)
    return costOfRows
    
def openExistingProgram():
    '''
    Opens and saves data from file into list fileInfo.
    '''
    fileInfo = []
    with open("theaterFile.csv", "r") as f:
        r = csv.reader(f, delimiter=",")
        for row in r:
            tempFileInfo = "".join(row)
            fileInfo.append(tempFileInfo[:])
    return fileInfo

def saveProgram(rows, collumns, theaterMap, costOfRows):
    '''
    Saves current theater data into file. 
    '''
    with open("theaterFile.csv", "w", newline='') as f:
        w = csv.writer(f, delimiter=",")
        w.writerow([rows])
        w.writerow([collumns])
        for row in range(0, rows):
            w.writerow(theaterMap[row])
        w.writerow(costOfRows)
    print("Program Saved.")
