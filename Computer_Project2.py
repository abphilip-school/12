import random, copy, sys, pygame
from pygame.locals import*

BOARDWIDTH=10
BOARDHEIGHT=10

assert BOARDWIDTH >=4 and BOARDHEIGHT >=4, 'Board must be atleast 4x4'

DIFFICULTY=1 # How many moves to look ahead.
SPACESIZE= 50 # Size of tokens and the board spaces in pixels.
FPS=30 #Frames per second to update the screen.

WINDOWWIDTH=1000 # Width of the program in Window, in pixels.
WINDOWHEIGHT= 700 # Height in pixels.

XMARGIN=int((WINDOWWIDTH-BOARDWIDTH*SPACESIZE)/2)
YMARGIN=int((WINDOWHEIGHT-BOARDHEIGHT*SPACESIZE)/2)

BRIGHTBLUE=(0,50,256)
WHITE=(255,255,255)

BGCOLOR=BRIGHTBLUE
TEXTCOLOR=WHITE

RED='Red'
BLACK='Black'
EMPTY=None
HUMAN='Human'
COMPUTER='Computer'

def main():
    global FPSCLOCK, DISPLAYSURF, REDPILERECT, BLACKPILERECT, REDTOKENIMG
    global BLACKTOKENIMG, BOARDIMG, ARROWIMG, ARROWRECT, HUMANWINNERIMG
    global COMPUTERWINNINERIMG, WINNERRECT, TIEWINNERIMG

    pygame.init()
    FPSCLOCK=pygame.time.clock()
    DISPLAYSURF=pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    pygame.display.set_caption("Four in a Row")

    REDPILERECT=pygame.Rect(int(SPACESIZE/2),WINDOWHEIGHT - int(3*SPACESIZE/2), SPACESIZE, SPACESIZE)
    BLACKPILERECT=pygame.Rect(WINDOWWIDTH-int(3*SPACESIZE/2), WINDOWHEIGHT-int(3*SPACESIZE/2), SPACESIZE, SPACESIZE)
    REDTOKENIMG=pygame.image.load('4row_red.png')
    REDTOKENIMG=pygame.transform.smoothscale(REDTOKENIMG, (SPACESIZE, SPACESIZE))
    BLACKTOKENIMG=pygame.image.load('4row_black.png')
    BLACKTOKENIMG=pygame.transform.smoothscale(BLACKTOKENIMG, (SPACESIZE, SPACESIZE))
    BOARDIMG=pygame.image.load('4row_board.png')
    BOARDIMG=pygame.transform.smoothscale(BOARDIMG, (SPACESIZE, SPACESIZE))

    HUMANWINNERIMG=pygame.image.load('4row_humanwinner.png')
    COMPUTERWINNERIMG=pygame.image.load('4row_computerwinner.png')
    TIEWINNERIMG=pygame.image.load('4row_tie.png')
    WINNERRECT=HUMANWINNERIMG.get_rect()
    WINNERRECT.center=(int(WINDOWWIDTH/2), int(WINDOWHEIGHT/2))

    ARROWIMG=pygame.image.load('4row_arrow.png')
    ARROWRECT=ARROWIMG.get_rect()
    ARROWRECT.left=REDPILERECT.right + 10
    ARROWRECT.centery=REDPILERECT.centery

    isFirstGame=True
    while True:
        runGame(isFirstGame)
        isFirstGame=False
    def runGame(isFirstGame):
        if isFirstGame:
            #Let the computer go first on the game, so the player can see how the tokens are dragged from the token piles
            turn=COMPUTER
            showHelp=True
        else:
            #Randomly choose who goes first
            if random.randint(0,1)==0:
                turn=COMPUTER
            else:
                turn=HUMAN
            showHelp=False

        # Set up a blank board data structure.
        mainBoard=getNewBoard()

        while True: # Main game loop
            if turn==HUMAN:
                # Human player's turn
                getHumanMove(mainBoard,showHelp)
                if showHelp:
                    # Turn off help arrow after the first move
                    showHelp =False
                if isWinner(mainBoard, RED):
                    winnerImg=HUMANWINNERIMG
                    break
                turn=COMPUTER #S witch turn
            else:
                # Computer Players turn
                column=getComputerMove(mainBoard)
                animateComputerMoving(mainBoard, column)
                makeMove(mainBoard, Black, column)
                if isWinner(mainBoard,Black):
                    winnerImg=COMPUTERWINNERIMG
                    break
                turn=Human # Switching to the other player
            if isBoardFull(mainBoard):
                winnerImg=TIEWINNERIMG
                break

        while True:
            # Keeps looping till the player clicks the mouse or quits
            drawBoard(mainBoard)
            DISPLAYSURF.blit(winnerImg, WINNERRECT)
            pygame.display.update()
            FPSCLOCK.tick()

            for event in pygame.event.get(): # Event handling loop
                if event.type == QUIT or (event.type == KEYUP an event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONUP:
                    return

    def makeMove(board, player, column):
        lowest=getLowestEmptySpace(board, column)
        if lowest!=-1:
            board[column][lowest]=player

    def drawBoard(board, extraToken=None):
        DISPLAYSURF.fill(BGCOLOR)

        # Draw tokens
        spaceRect=pygame.Rect(0,0,SPACESIZE,SPACESIZE)
        for x in range(BOARDWIDTH):
            for y in range(BOARDHEIGHT):
                spaceRect.topleft=(XMARGIN+(x*SPACESIZE), YMARGIN+(y*SPACESIZE))
                if board[x][y] == RED:
                    DISPLAYSURF.blit(REDTOKENIMG, spaceRect)
                elif board[x][y] == BLACK:
                    DISPLAYSURF.blit(BLACKTOKENIMG, spaceRect)

        # Draw the extra token
        if extraToken!=None:
            if extraToken['color'] == RED:
                DISPLAYSURF.blit(REDTOKENIMG, (extraToken['x'], extraToken['y'], SPACESIZE, SPACESIZE))
            elif extraToken['color'] == BLACK:
                DISPLAYSURF.blit(BLACKTOKENIMG, (extraToken['x'], extraToken['y'], SPACESIZE, SPACESIZE))

        # Draw board over the tokens
        for x in range(BOARDWIDTH):
            for y in range(BOARDHEIGHT):
                spaceRect.topleft=(XMARGIN+(x*SPACESIZE), YMARGIN+(y*SPACESIZE))
                DISPLAYSURF.blit(BOARDIMG, spaceRect)

        # Draw red and black tokens off to the side
        DISPLAYSURD.blit(REDTOKENIMG, REDPILERECT) # RED on the left
        DISPLAYSURD.blit(BALCKTOKENIMG, BLACKPILERECT) # BLACK on the right

    def getNewBoard():
        board=[]
        for x in range(BOARDWIDTH):
            board.append([EMPTY]*BOARDHEIGHT)
        return board

# The following function is not given correctly:
    def getHumanMove(board, isFirstMove):
        draggingToken = False
        tokenx, tokeny = None,None
        while True:
            for event in pygame.event.get(): # Event handling loop
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN and not draggingToken and REDPILERECT.collidepoint(event.pos):
                    # Start of dragging on red token pile
                    draggingToken=True
                    tokenx, tokeny=event.pos
                elif event.type == MOUSEMOTION and draggingToken:
                    # Update the position of the red token being dragged
                    tokenx, tokeny=event.pos
                elif event.type == MOUSEBUTTONUP and draggingToken:
                    # Let go of the token being dragged
                    if tokeny<YMARGIN and tokenx>XMARGIN and tokenx<WINDOWWIDTH - XMARGIN:
                        # Let go at the top of the screen
                        column=int((tokenx-XMARGIN)/SPACESIZE)
                        if isValidMove(board,column):
                            animateDroppingToken(board,column,RED)
                            board[column][getLowestEmptySpace(board, column)]= RED
                            drawBoard(board)
                            pygame.display.update()
                            return
                    tokenx, tokeny=None, None
                    dragginToken=False
            if tokenx!=None and tokeny!=None:
                drawboard(board,{'x':token-int(SPACESIZE/2),'y':tokeny-int(SPACESIZE/2), 'color':RED})
            else:
                drawBoard(board)

            if isFirstMove:
                # Show the help arrow for the player's first move
                DISPLAYSURF.blit(ARROWIMG, ARROWRECT)

            pygame.display.update()
            FPSCLOCK.tick()
    def 
        
                        
                
