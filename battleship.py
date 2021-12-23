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
    data["user"]=emptyGrid(data["rows"],data["cols"])
    data["computer"]=addShips(data["computer"],data["numOfShips"])
    data["tempShip"]=[]
    data["numOfUserShips"]=0
    data["winner"]="draw"
    data["maxTurns"]=50
    data["currentTurns"]=0
    return


'''
makeView(data, userCanvas, compCanvas)
Parameters: dict mapping strs to values ; Tkinter canvas ; Tkinter canvas
Returns: None
'''
def makeView(data, userCanvas, compCanvas):
    drawGrid(data,compCanvas,data["computer"],True)
    drawGrid(data,userCanvas,data["user"],True)
    drawShip(data,userCanvas,data["tempShip"])
    drawGameOver(data,compCanvas)


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
    if(data["winner"] == None):
        pos=getClickedCell(data,event)
        if("user" == board):
            clickUserBoard(data,pos[0],pos[1])
        else:
            if(data["numOfUserShips"] == 5 and board == "comp"):
                runGameTurn(data,pos[0],pos[1])
    

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
                if(showShips):
                    canvas.create_rectangle(j*data["cellSize"],i*data["cellSize"],(j+1)*data["cellSize"],(i+1)*data["cellSize"],fill="yellow")
                else:
                    canvas.create_rectangle(j*data["cellSize"],i*data["cellSize"],(j+1)*data["cellSize"],(i+1)*data["cellSize"],fill="blue")
            elif(grid[i][j] == SHIP_CLICKED):
                canvas.create_rectangle(j*data["cellSize"],i*data["cellSize"],(j+1)*data["cellSize"],(i+1)*data["cellSize"],fill="red")
            elif(grid[i][j] == EMPTY_CLICKED):
                canvas.create_rectangle(j*data["cellSize"],i*data["cellSize"],(j+1)*data["cellSize"],(i+1)*data["cellSize"],fill="white")
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
    X=[]
    for shipI in range(len(ship)):
        if(shipI == 0):
            X.append(ship[shipI][0])
            tempY=ship[shipI][1]
        elif(tempY == ship[shipI][1]):
            X.append(ship[shipI][0])
            tempY=ship[shipI][1]
            continue
        else:
            return False
    if(max(X) != min(X)+2):
        return False
    if(sum(X)%3 == 0):
        return True
    else:
        return False


'''
isHorizontal(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isHorizontal(ship):
    Y=[]
    for shipI in range(len(ship)):
        if(shipI == 0):
            Y.append(ship[shipI][1])
            tempX=ship[shipI][0]
        elif(tempX == ship[shipI][0]):
            Y.append(ship[shipI][1])
            tempX=ship[shipI][0]
            continue
        else:
            return False
    if(max(Y) != min(Y)+2):
        return False
    elif(sum(Y)%3 == 0):
        return True
    else:
        return False


'''
getClickedCell(data, event)
Parameters: dict mapping strs to values ; mouse event object
Returns: list of ints
'''
def getClickedCell(data, event):
    result=[]
    for i in range(data["rows"]):
        for j in range(data["cols"]):
            if((j*data["cellSize"]<=event.x and (j+1)*data["cellSize"]>=event.x) and (i*data["cellSize"]<=event.y and (i+1)*data["cellSize"]>=event.y)):
                result=[i,j]
    return result


'''
drawShip(data, canvas, ship)
Parameters: dict mapping strs to values ; Tkinter canvas; 2D list of ints
Returns: None
'''
def drawShip(data, canvas, ship):
    for cord in ship:
        canvas.create_rectangle(cord[1]*data["cellSize"],cord[0]*data["cellSize"],(cord[1]+1)*data["cellSize"],(cord[0]+1)*data["cellSize"],fill="white")


'''
shipIsValid(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def shipIsValid(grid, ship):
    if len(ship) != 3:
        return False
    elif(isHorizontal(ship) == False and isVertical(ship) == False):
        return False
    else:    
        for ships in ship:
            if(grid[ships[0]][ships[1]] == SHIP_UNCLICKED):
                return False
    return True


'''
placeShip(data)
Parameters: dict mapping strs to values
Returns: None
'''
def placeShip(data):
    if(data["numOfUserShips"] == 5):
        return
    if(shipIsValid(data["user"],data["tempShip"])):
        for cord in data["tempShip"]:
            data["user"][cord[0]][cord[1]]=SHIP_UNCLICKED
        data["numOfUserShips"]+=1
    else:
        print("Ship is not valid, try again")
    data["tempShip"]=[]


'''
clickUserBoard(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def clickUserBoard(data, row, col):
    if([row,col] in data["tempShip"]):
        return
    elif(data["numOfUserShips"] >= 5):
        return
    else:
        data["tempShip"].append([row,col])
        if(len(data["tempShip"])==3):
            placeShip(data)
        if(data["numOfUserShips"] == 5):
            print("Start playing the game")


### WEEK 3 ###

'''
updateBoard(data, board, row, col, player)
Parameters: dict mapping strs to values ; 2D list of ints ; int ; int ; str
Returns: None
'''
def updateBoard(data, board, row, col, player):
    if(board[row][col] == SHIP_UNCLICKED):
        board[row][col]=SHIP_CLICKED
    elif(board[row][col] == EMPTY_UNCLICKED):
        board[row][col]=EMPTY_CLICKED
    if(isGameOver(board)):
        print(player)
        data["winner"]=player
    #data["winner"]=player


'''
runGameTurn(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def runGameTurn(data, row, col):
    comp=data["computer"]
    if(comp[row][col] == SHIP_CLICKED or comp[row][col] == EMPTY_CLICKED):
        return
    else:
        updateBoard(data,data["computer"],row,col,"computer")
        cord=getComputerGuess(data["user"])
        updateBoard(data,data["user"],cord[0],cord[1],"user")
        data["currentTurns"]+=1
        if(data["currentTurns"] == data["maxTurns"]):
            data["winner"]="draw"


'''
getComputerGuess(board)
Parameters: 2D list of ints
Returns: list of ints
'''
def getComputerGuess(board):
    row=random.randint(0,9)
    col=random.randint(0,9)
    while(board[row][col] == EMPTY_CLICKED or board[row][col] == SHIP_CLICKED):
        row=random.randint(0,9)
        col=random.randint(0,9)
    if(board[row][col] == EMPTY_UNCLICKED):
        board[row][col]=EMPTY_CLICKED
    elif(board[row][col] == SHIP_UNCLICKED):
        board[row][col]=SHIP_CLICKED
    return [row,col]


'''
isGameOver(board)
Parameters: 2D list of ints
Returns: bool
'''
def isGameOver(board):
    for row in board:
        for col in row:
            if(col == SHIP_UNCLICKED):
                return False
    return True


'''
drawGameOver(data, canvas)
Parameters: dict mapping strs to values ; Tkinter canvas
Returns: None
'''
def drawGameOver(data, canvas):
    if(data["winner"] == "computer"):
        canvas.create_text(data["boardSize"]//2, data["boardSize"]//2, text="CONGRADULATIONS... YOU WON!...",fill="yellow",font=("Helvetica-Bold", 15))
    elif(data["winner"] == "user"):
        canvas.create_text(data["boardSize"]//2, data["boardSize"]//2, text="YOU LOSS..",fill="black",font=("Helvetica-Bold", 15))
    elif(data["winner"] == "draw"):
        canvas.create_text(data["boardSize"]//2, data["boardSize"]//2, text="Sorry..Out of moves!..",fill="green",font=("Helvetica-Bold", 15))


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
    # test.testIsVertical()
    # test.testIsHorizontal()
    #test.testDrawGrid()
    #test.testMakeModel()
    test.week1Tests()
    test.week2Tests()
    ## Finally, run the simulation to test it manually ##
    runSimulation(500, 500)
    #test.testShipIsValid()
    #test.testAddShips()
    #test.testUpdateBoard()
    #test.testGetComputerGuess()
    #test.testIsGameOver()
