import stddraw
import random
from color import Color

def generateBoard(time):
    board = []

    if time != 9999:
        numberOfObjects = 6
    else:
        numberOfObjects = 8

    for i in range(11): #9
        board += [[]]
        for a in range(9): #7
            if i >= 9 or a >= 7: #The top 2 rows and right 2 columns are blank cause it simplifies things (listIndexRange when making checks)
                board[i] += ["-"]
            else:
                board[i] += [random.randrange(numberOfObjects)]
    for i in range(9): #checks for 3 in a row
        for a in range(7):
            if board[i-1][a] == board[i][a] == board[i+1][a] or board[i][a-1] == board[i][a] == board[i][a+1]: #if there are 3 in a row horizontally or vertically             
                while True:
                    b = random.randrange(numberOfObjects)
                    if board[i][a] != b and not board[i-2][a] == board[i-2][a] == b and not board[i-1][a] == b == board[i+1][a] and not b == board[i+1][a] == board[i+2][a] and not board[i][a-2] == board[i][a-2] == b and not board[i][a-1] == b == board[i][a+1] and not b == board[i][a+1] == board[i][a+2]: #makes sure it doesn't create new 3 in a rows
                        board[i][a] = b #replace it with a value that will not create new 3 in a rows
                        break
    return board

def drawTop(score, time):
    stddraw.setPenColor(stddraw.DARK_BLUE)
    stddraw.filledRectangle(0,9,9,2)

    stddraw.setPenColor(stddraw.WHITE)
    stddraw.setFontSize(15)
    stddraw.text(5, 10.3, "SCORE:")
    stddraw.text(2, 10.3, "TIME REMAINING:")

    stddraw.setFontSize(40)
    if time != 9999:
        stddraw.text(5, 9.8, str(score)+"/1000")
        stddraw.text(2, 9.8, str(25-int(time)))
    else:
        stddraw.text(5, 9.8, str(score))
        stddraw.text(2, 9.8, "∞")

def drawBoard():
    stddraw.setFontSize(40)
    for row in range(9):
        for column in range(7):
            drawPiece(column, row, 0)

def drawPiece(x, y, ay):

    stddraw.setPenRadius(0.008)

    if board[y][x] == 0: #diamond
        FILL = Color(250,252,255)
        stddraw.setPenColor(FILL)
        xs = [x+0.5, x+0.2, x+0.35, x+0.65, x+0.8]
        ys = [y+ay+0.2, y+ay+0.5, y+ay+0.7, y+ay+0.7, y+ay+0.5]
        stddraw.filledPolygon(xs, ys)

        OUTLINE = Color(220,225,255)
        stddraw.setPenColor(OUTLINE)
        xs = [x+0.5, x+0.2, x+0.35, x+0.65, x+0.8]
        ys = [y+ay+0.2, y+ay+0.5, y+ay+0.7, y+ay+0.7, y+ay+0.5]
        stddraw.polygon(xs, ys)

    if board[y][x] == 1: #emerald
        FILL = Color(180,255,180)
        stddraw.setPenColor(FILL)
        xs = [x+0.5, x+0.7, x+0.7, x+0.5, x+0.3, x+0.3]
        ys = [y+ay+0.8, y+ay+0.6, y+ay+0.4, y+ay+0.2, y+ay+0.4, y+ay+0.6]
        stddraw.filledPolygon(xs, ys)

        FILL = Color(210,255,210)
        stddraw.setPenColor(FILL)
        xs = [x+0.5, x+0.7, x+0.5, x+0.3]
        ys = [y+ay+0.8, y+ay+0.6, y+ay+0.4, y+ay+0.6]
        stddraw.filledPolygon(xs, ys)

        OUTLINE = Color(100,225,100)
        stddraw.setPenColor(OUTLINE)
        xs = [x+0.5, x+0.7, x+0.7, x+0.5, x+0.3, x+0.3]
        ys = [y+ay+0.8, y+ay+0.6, y+ay+0.4, y+ay+0.2, y+ay+0.4, y+ay+0.6]
        stddraw.polygon(xs, ys)

    if board[y][x] == 2: #ruby
        FILL = Color(245,140,140)
        stddraw.setPenColor(FILL)
        xs = [x+0.65, x+0.75, x+0.75, x+0.65, x+0.35, x+0.25, x+0.25, x+0.35]
        ys = [y+ay+0.8, y+ay+0.7, y+ay+0.3, y+ay+0.2, y+ay+0.2, y+ay+0.3, y+ay+0.7, y+ay+0.8]
        stddraw.filledPolygon(xs, ys)

        FILL2 = Color(255,180,180)
        stddraw.setPenColor(FILL2)
        xs = [x+0.65, x+0.75, x+0.5, x+0.25, x+0.35]
        ys = [y+ay+0.8, y+ay+0.7, y+ay+0.5, y+ay+0.7, y+ay+0.8]
        stddraw.filledPolygon(xs, ys)

        OUTLINE = Color(205,80,80)
        stddraw.setPenColor(OUTLINE)
        xs = [x+0.65, x+0.75, x+0.75, x+0.65, x+0.35, x+0.25, x+0.25, x+0.35]
        ys = [y+ay+0.8, y+ay+0.7, y+ay+0.3, y+ay+0.2, y+ay+0.2, y+ay+0.3, y+ay+0.7, y+ay+0.8]
        stddraw.polygon(xs, ys)

    if board[y][x] == 3: #saphhire
        FILL = Color(60,120,255)
        stddraw.setPenColor(FILL)
        stddraw.filledCircle(x+0.5, y+ay+0.5, 0.3)

        FILL = Color(80,190,255) 
        stddraw.setPenColor(FILL)
        stddraw.filledCircle(x+0.4, y+ay+0.6, 0.1)

        OUTLINE = Color(20,50,255) 
        stddraw.setPenColor(OUTLINE)
        stddraw.circle(x+0.5, y+ay+0.5, 0.3)

    if board[y][x] == 4: #topaz
        FILL = Color(255,255,200)
        stddraw.setPenColor(FILL)
        xs = [x+0.5, x+0.2, x+0.3, x+0.7]
        ys = [y+ay+0.2, y+ay+0.5, y+ay+0.7, y+ay+0.7]
        stddraw.filledPolygon(xs, ys)

        OUTLINE = Color(225,225,100)
        stddraw.setPenColor(OUTLINE)
        stddraw.polygon(xs, ys)

    if board[y][x] == 5: #amethyst
        FILL = Color(225,170,225)
        stddraw.setPenColor(FILL)
        xs = [x+0.5, x+0.8, x+0.5, x+0.2]
        ys = [y+ay+0.8, y+ay+0.5, y+ay+0.2, y+ay+0.5]
        stddraw.filledPolygon(xs, ys)

        FILL = Color(245,180,245)
        stddraw.setPenColor(FILL)
        xs = [x+0.5, x+0.5, x+0.2]
        ys = [y+ay+0.8, y+ay+0.4, y+ay+0.5]
        stddraw.filledPolygon(xs, ys)

        OUTLINE = Color(155,100,155)
        stddraw.setPenColor(OUTLINE)
        xs = [x+0.5, x+0.8, x+0.5, x+0.2]
        ys = [y+ay+0.8, y+ay+0.5, y+ay+0.2, y+ay+0.5]
        stddraw.polygon(xs, ys)

    if board[y][x] == 6: #aquamarine
        FILL = Color(100,250,220)
        stddraw.setPenColor(FILL)
        xs = [x+0.5, x+0.8, x+0.7, x+0.3, x+0.2]
        ys = [y+ay+0.8, y+ay+0.4, y+ay+0.2, y+ay+0.2, y+ay+0.4]
        stddraw.filledPolygon(xs, ys)

        FILL = Color(190,255,250)
        stddraw.setPenColor(FILL)
        xs = [x+0.5, x+0.7, x+0.6, x+0.4, x+0.3]
        ys = [y+ay+0.7, y+ay+0.45, y+ay+0.3, y+ay+0.3, y+ay+0.45]
        stddraw.filledPolygon(xs, ys)

        OUTLINE = Color(50,200,170) 
        stddraw.setPenColor(OUTLINE)
        xs = [x+0.5, x+0.8, x+0.7, x+0.3, x+0.2]
        ys = [y+ay+0.8, y+ay+0.4, y+ay+0.2, y+ay+0.2, y+ay+0.4]
        stddraw.polygon(xs, ys)

    if board[y][x] == 7: #citrine
        FILL = Color(255,160,70)
        stddraw.setPenColor(FILL)
        xs = [x+0.3, x+0.2, x+0.7, x+0.7]
        ys = [y+ay+0.2, y+ay+0.6, y+ay+0.8, y+ay+0.3]
        stddraw.filledPolygon(xs, ys)

        FILL = Color(255,190,90)
        stddraw.setPenColor(FILL)
        xs = [x+0.5, x+0.2, x+0.7, x+0.7]
        ys = [y+ay+0.5, y+ay+0.6, y+ay+0.8, y+ay+0.6]
        stddraw.filledPolygon(xs, ys)

        OUTLINE = Color(205,100,30) 
        stddraw.setPenColor(OUTLINE)
        xs = [x+0.3, x+0.2, x+0.7, x+0.7]
        ys = [y+ay+0.2, y+ay+0.6, y+ay+0.8, y+ay+0.3]
        stddraw.polygon(xs, ys)

def select(score, time):
    while True: 
        stddraw.show(100) #pause for .1 second
        drawTop(score, time) #draw this each time to update time

        if time != 9999:
            time += .1
            if checkScoreTime(time): #if times out then stop waiting for input
                return [0,0], score, time

        if stddraw.mousePressed() and stddraw.mouseY() < 9: #you press on the board
            mx = stddraw.mouseX()
            my = stddraw.mouseY()
            return [int(mx), int(my)], score, time

def drawSelect(point, score, time): #[x, y], score
    x = point[0]
    y = point[1]
    stddraw.clear()
            
    LIGHT_BLUE = Color(190,240,255)
    stddraw.setPenColor(LIGHT_BLUE)
    stddraw.filledSquare(x-1+0.5, y+0.5, 0.5) #the 4 adjacent squares to the one you clicked
    stddraw.filledSquare(x+1+0.5, y+0.5, 0.5)
    stddraw.filledSquare(x+0.5, y-1+0.5, 0.5)
    stddraw.filledSquare(x+0.5, y+1+0.5, 0.5)

    drawTop(score, time)
    drawBoard()

    stddraw.setPenColor(stddraw.BLACK)
    stddraw.setPenRadius(0.04)
    
    stddraw.line(x, y, x+0.25, y) #the 4 corners around the selected square
    stddraw.line(x, y, x, y+0.25) #bottom left

    stddraw.line(x+0.75, y, x+1, y) #bottom right
    stddraw.line(x+1, y, x+1, y+0.25)

    stddraw.line(x, y+0.75, x, y+1) #top left
    stddraw.line(x, y+1, x+0.25, y+1)

    stddraw.line(x+0.75, y+1, x+1, y+1) #top right
    stddraw.line(x+1, y+0.75, x+1, y+1)

def checkValid(point1, point2): #if you clicked next to the square and it connected 3 or more squares together
    validCheck1 = False
    #if next to each other the difference in x should be +- 1 and difference in y should be 0
    if point1[0] - point2[0] == 1 or point1[0] - point2[0] == -1:
        if point1[1] - point2[1] == 0:
            validCheck1 = True
    #or difference in x should be 0 and difference in y should be +-1
    if point1[0] - point2[0] == 0:
        if point1[1] - point2[1] == 1 or point1[1] - point2[1] == -1:
            validCheck1 = True

    if validCheck1 == True:
        move(point1, point2) #make the move
        a = checkThree() #checks if there are 3 points next to each other anywhere on the map
        if a:
            return True
        else: 
            move(point1, point2) #move back the points because move was not valid
            return False
    return False

def move(point1, point2): # [x, y], [x, y]
    a = board[point1[1]][point1[0]]
    b = board[point2[1]][point2[0]]
    board[point2[1]][point2[0]] = a
    board[point1[1]][point1[0]] = b

def checkThree(): #checks if there are 3 in a row anywhere on board
    for i in range(9):
        for a in range(7):
            if board[i-1][a] == board[i][a] == board[i+1][a]: #if vertical
                return True
            if board[i][a-1] == board[i][a] == board[i][a+1]: #if horizontal            
                return True         
    return False

def eliminate(score, bonus):
    toRemove = []

    for row in range(9):
        length = 1
        for column in range(7):
            if board[row][column] == board[row][column+1]: #if there is a chain of same squares
                length += 1
            elif length >= 3: #chain breaks here
                for b in range(length): 
                    toRemove += [ [row, column-b] ] # y,x location
                length = 1
            else: #chain didn't reach at least 3 so reset it
                length = 1

    for column in range(7):
        length = 1
        for row in range(9):
            if board[row][column] == board[row+1][column]: #same as above, but check horizontally
                length += 1
            elif length >= 3: #chain breaks here
                for b in range(length): 
                    toRemove += [ [row-b, column] ] # y,x location
                length = 1
            else: #chain didn't reach at least 3 so reset it
                length = 1

    LIGHT_GREEN = Color(230,255,230)
    stddraw.setPenColor(LIGHT_GREEN)

    for point in toRemove:
        if board[point[0]][point[1]] != "":
            board[point[0]][point[1]] = ""
            stddraw.setPenColor(LIGHT_GREEN)
            stddraw.filledSquare(point[1]+0.5, point[0]+0.5, 0.5)
            score += 10 + bonus #the more you get in a row the higher score you get
            bonus += 1
    stddraw.show(150) #briefly flash light green where tiles connected and disapeared
    return score, bonus

def drop(time):
    toDrop = []
    for row in range(9):
        for column in range(7):
            if board[row][column] == "":
                for i in range(row, 9): #if there is a blank tile, all the tiles above it need to move down
                    toDrop += [[i, column]]
                if row == 8: #if top row, replace with random number
                    if time == 9999:
                        b = random.randrange(8)
                    else:
                        b = random.randrange(6)
                    board[row][column] = b
                else: #if not move down
                    move([column, row], [column, row+1]) # [x, y], [x, y]
    return toDrop

def animateDrop(toDrop, score, time):
    a = 0.8
    while a > 0:
        stddraw.clear()
        for row in range(9):
            for column in range(7):
                q = True
                for i in range(len(toDrop)): #if the tile is one that is dropped
                    if [row, column] == toDrop[i]:
                        drawPiece(column, row, a) #a = 1, so show it as 1 higher and decrease
                        q = False
                if q: #if the tile doesn't get dropped, show it in its normal position
                    drawPiece(column, row, 0)
        drawTop(score, time)
        a -= 0.20
        stddraw.show(10)

def completeDrop(score, time): #combines the two functions into one
    while emptyTileExists():
        a = drop(time)
        animateDrop(a, score, time)

def emptyTileExists():
    for row in range(9):
        for column in range(7):
            if board[row][column] == "":
                return True
    return False

def checkPossibleMoves():
    """ look at all positions with *
       -*--*-     --*--       --*--
    A: *-Xx-*  B: -X-x-       -*-*-      --x--
       -*--*-     --*--    C: --x--   D: -*-*-
                              --X--      --X--
                              -*-*-
                              --*--
    """
    for row in range(9):
        for column in range(7):
            if board[row][column] == board[row][column+1]: #A
                a = board[row][column]
                if column != 6: #column +3 would lead to an error
                    if a == board[row+1][column+2] or a == board[row][column+3] or a == board[row-1][column+2] or a == board[row-1][column-1] or a == board[row][column-2] or a ==board[row+1][column-1]:
                        return False
                else: 
                    if a == board[row+1][column+2] or a == board[row-1][column+2] or a == board[row-1][column-1] or a == board[row][column-2] or a ==board[row+1][column-1]:
                        return False
            if board[row][column] == board[row][column+2]: # B
                if board[row][column] == board[row+1][column+1] or board[row][column] == board[row-1][column+1]:
                    return False

            if board[row][column] == board[row+1][column]: #C
                a = board[row][column]
                if row != 8: #row +3 would lead to an error
                    if a == board[row-1][column+1] or a == board[row-2][column] or a == board[row-1][column-1] or a == board[row+2][column-1] or a == board[row+3][column] or a == board[row+2][column+1]:
                        return False
                else:
                    if a == board[row-1][column+1] or a == board[row-2][column] or a == board[row-1][column-1] or a == board[row+2][column-1] or a == board[row+2][column+1]:
                        return False

            if board[row][column] == board[row+2][column]: #D
                if board[row][column] == board[row+1][column-1] or board[row][column] == board[row+1][column+1]:
                    return False
    return True
    
def checkScoreTime(time):
    if time != 9999:
        if  time >= 25:
            return True    
    return False

stddraw.setXscale(0,7)
stddraw.setYscale(0,11)
stddraw.setCanvasSize(420, 660) #700*0.6, 1100*0.6

stddraw.setFontSize(50)
stddraw.setPenColor(stddraw.DARK_BLUE)
stddraw.text(3.5, 9.5, "How do you")
stddraw.text(3.5, 8.5, "want to play?")

stddraw.filledRectangle(1, 5, 5, 2)
stddraw.filledRectangle(1, 2, 5, 2)

stddraw.setPenColor(stddraw.WHITE)
stddraw.text(3.5, 6, "Timed")
stddraw.text(3.5, 3, "Perfection")

while True: 
    stddraw.show(0.0) #pause for .1 second

    if stddraw.mousePressed():
        if 5 < stddraw.mouseY() < 7 and 1 < stddraw.mouseX() < 6: #Timed
            time = 0
            break
        if 2 < stddraw.mouseY() < 4 and 1 < stddraw.mouseX() < 6: #Perfection
            time = 9999
            break

score = 0
board = generateBoard(time)

gameOver = False
while not gameOver:

    validMove = False
    while not validMove: #wait until you make a possible move
        stddraw.clear()
        drawTop(score, time)
        drawBoard()
        point1, score, time = select(score, time) #select the first point
        if checkScoreTime(time):
            break
        drawSelect(point1, score, time)
        point2, score, time = select(score, time) #select the second point
        if checkScoreTime(time):
            break
        validMove = checkValid(point1, point2) #see if you can move those 2 points
        stddraw.clear()
        drawBoard()
        drawTop(score, time)

    if checkScoreTime(time):
        break
    bonus = 0 #get more points for each you get in a row, including 3 you connected from making tiles fall
    score, bonus = eliminate(score, bonus)

    while emptyTileExists():
        completeDrop(score, time)
        score, bonus = eliminate(score, bonus)
    
    gameOver = checkPossibleMoves()

stddraw.clear()
drawBoard()

stddraw.setPenColor(stddraw.DARK_BLUE)
stddraw.filledRectangle(0,9,9,2)

stddraw.setPenColor(stddraw.WHITE)
stddraw.setFontSize()

if not checkScoreTime(time):
    stddraw.setFontSize(35)
    stddraw.text(3.5, 10, "No Possible Moves Left")
    ORANGE = Color(255, 100, 00)
    stddraw.setPenColor(ORANGE)
else:
    stddraw.setFontSize(60)
    if score >= 1000:
        stddraw.text(3.5, 10, "You Win")
        stddraw.setPenColor(stddraw.BLUE)
    else:
        stddraw.text(3.5, 10, "You Lose")
        stddraw.setPenColor(stddraw.RED)

stddraw.setFontSize(40)
stddraw.setPenRadius(0.004)

stddraw.filledRectangle(1.5, 4.5, 4, 3) #2 + 3 + 2
stddraw.setPenColor(stddraw.WHITE)
stddraw.text(3.5, 6.5, "Final Score:")
stddraw.setFontSize(60)
stddraw.text(3.5, 5.5, str(score))

stddraw.show()