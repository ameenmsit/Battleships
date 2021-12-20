"""
Battleship Project
Name: Ameen N.A
Roll No: 2021-IIITH-C2-002
"""

import battleship_tests as test

project = "Battleship" # don't edit this

### SIMULATION FUNCTIONS ###

from tkinter import *
import random

EMPTY_UNCLICKED = 1
SHIP_UNCLICKED = 2
EMPTY_CLICKED = 3
SHIP_CLICKED = 4


'''
makeModel(data)
Parameters: dict mapping strs to values
Returns: None
'''
def makeModel(data):
    data["rows"]=10
    data["cols"]=10
    data["boardSize"]=500
    data["cellSize"]=data["boardSize"]//(data["rows"])
    data["numOfShips"]=5
    data["computer"]=emptyGrid(data["rows"],data["cols"])
    data["user"]=test.testGrid()#emptyGrid(data["rows"],data["cols"])
    data["computer"]=addShips(data["computer"],data["numOfShips"])
    return


'''
makeView(data, userCanvas, compCanvas)
Parameters: dict mapping strs to values ; Tkinter canvas ; Tkinter canvas
Returns: None
'''
def makeView(data, userCanvas, compCanvas):
    drawGrid(data,compCanvas,data["computer"],True)
    drawGrid(data,userCanvas,data["user"],True)
    return


'''
keyPressed(data, events)
Parameters: dict mapping strs to values ; key event object
Returns: None
'''
def keyPressed(data, event):
    pass


'''
mousePressed(data, event, board)
Parameters: dict mapping strs to values ; mouse event object ; 2D list of ints
Returns: None
'''
def mousePressed(data, event, board):
    pass

#### WEEK 1 ####

'''
emptyGrid(rows, cols)
Parameters: int ; int
Returns: 2D list of ints
'''
def emptyGrid(rows, cols):
    outer=[]
    for i in range(rows):
        inner=[]
        for j in range(cols):
            inner.append(EMPTY_UNCLICKED)
        outer.append(inner)
    return outer


'''
createShip()
Parameters: no parameters
Returns: 2D list of ints
'''
def createShip():
    randRow=random.randint(1,8)
    randCol=random.randint(1,8)
    VERTICAL=0
    HORIZONTAL=1
    align=random.randint(0,1)
    if(align == HORIZONTAL):
        ship=[[randRow,randCol-1],[randRow,randCol],[randRow,randCol+1]]
    else:
        ship=[[randRow-1,randCol],[randRow,randCol],[randRow+1,randCol]]
    return ship


'''
checkShip(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def checkShip(grid, ship):
    for ships in ship:
        if(grid[ships[0]][ships[1]] != EMPTY_UNCLICKED):
                return False
    return True


'''
addShips(grid, numShips)
Parameters: 2D list of ints ; int
Returns: 2D list of ints
'''
def addShips(grid, numShips):
    while(numShips>0):
        ship=createShip()
        status=checkShip(grid,ship)
        if(status):
            for s in ship:
                grid[s[0]][s[1]]=SHIP_UNCLICKED
        numShips-=1
    return grid


'''
drawGrid(data, canvas, grid, showShips)
Parameters: dict mapping strs to values ; Tkinter canvas ; 2D list of ints ; bool
Returns: None
'''
def drawGrid(data, canvas, grid, showShips):
    for i in range(data["rows"]):
        for j in range(data["cols"]):
            if(grid[i][j] == SHIP_UNCLICKED):
                canvas.create_rectangle(j*data["cellSize"],i*data["cellSize"],(j+1)*data["cellSize"],(i+1)*data["cellSize"],fill="yellow")
            else:
                canvas.create_rectangle(j*data["cellSize"],i*data["cellSize"],(j+1)*data["cellSize"],(i+1)*data["cellSize"],fill="blue")
    return


### WEEK 2 ###

'''
isVertical(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isVertical(ship):
    sumX=0
    for shipI in range(len(ship)):
        if(shipI == 0):
            sumX+=ship[shipI][0]
            tempY=ship[shipI][1]
        elif(tempY == ship[shipI][1]):
            sumX+=ship[shipI][0]
            tempY=ship[shipI][1]
            continue
        else:
            return False
    if(sumX%3 == 0):
        return True
    else:
        return False


'''
isHorizontal(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isHorizontal(ship):
    sumY=0
    for shipI in range(len(ship)):
        if(shipI == 0):
            sumY+=ship[shipI][1]
            tempX=ship[shipI][0]
        elif(tempX == ship[shipI][0]):
            sumY+=ship[shipI][1]
            tempX=ship[shipI][0]
            continue
        else:
            return False
    if(sumY%3 == 0):
        return True
    else:
        return False


'''
getClickedCell(data, event)
Parameters: dict mapping strs to values ; mouse event object
Returns: list of ints
'''
def getClickedCell(data, event):
    return


'''
drawShip(data, canvas, ship)
Parameters: dict mapping strs to values ; Tkinter canvas; 2D list of ints
Returns: None
'''
def drawShip(data, canvas, ship):
    return


'''
shipIsValid(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def shipIsValid(grid, ship):
    return


'''
placeShip(data)
Parameters: dict mapping strs to values
Returns: None
'''
def placeShip(data):
    return


'''
clickUserBoard(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def clickUserBoard(data, row, col):
    return


### WEEK 3 ###

'''
updateBoard(data, board, row, col, player)
Parameters: dict mapping strs to values ; 2D list of ints ; int ; int ; str
Returns: None
'''
def updateBoard(data, board, row, col, player):
    return


'''
runGameTurn(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def runGameTurn(data, row, col):
    return


'''
getComputerGuess(board)
Parameters: 2D list of ints
Returns: list of ints
'''
def getComputerGuess(board):
    return


'''
isGameOver(board)
Parameters: 2D list of ints
Returns: bool
'''
def isGameOver(board):
    return


'''
drawGameOver(data, canvas)
Parameters: dict mapping strs to values ; Tkinter canvas
Returns: None
'''
def drawGameOver(data, canvas):
    return


### SIMULATION FRAMEWORK ###

from tkinter import *

def updateView(data, userCanvas, compCanvas):
    userCanvas.delete(ALL)
    compCanvas.delete(ALL)
    makeView(data, userCanvas, compCanvas)
    userCanvas.update()
    compCanvas.update()

def keyEventHandler(data, userCanvas, compCanvas, event):
    keyPressed(data, event)
    updateView(data, userCanvas, compCanvas)

def mouseEventHandler(data, userCanvas, compCanvas, event, board):
    mousePressed(data, event, board)
    updateView(data, userCanvas, compCanvas)

def runSimulation(w, h):
    data = { }
    makeModel(data)

    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window

    # We need two canvases - one for the user, one for the computer
    Label(root, text = "USER BOARD - click cells to place ships on your board.").pack()
    userCanvas = Canvas(root, width=w, height=h)
    userCanvas.configure(bd=0, highlightthickness=0)
    userCanvas.pack()

    compWindow = Toplevel(root)
    compWindow.resizable(width=False, height=False) # prevents resizing window
    Label(compWindow, text = "COMPUTER BOARD - click to make guesses. The computer will guess on your board.").pack()
    compCanvas = Canvas(compWindow, width=w, height=h)
    compCanvas.configure(bd=0, highlightthickness=0)
    compCanvas.pack()

    makeView(data, userCanvas, compCanvas)

    root.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    compWindow.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    userCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "user"))
    compCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "comp"))

    updateView(data, userCanvas, compCanvas)

    root.mainloop()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":
    #test.week1Tests()
    test.testIsVertical()
    test.testIsHorizontal()
    ## Finally, run the simulation to test it manually ##
    #runSimulation(500, 500)
