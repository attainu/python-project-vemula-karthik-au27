from tkinter.tix import MAIN
import pygame as p
# from chess import chessmain
from chessmain import gamestate

width=height=512
dimension=8
SQ_SIZE=height//dimension
max_fps=15
images={}

def loadimages():
    pieces=['wP','wR','wN','wB','wK','wQ','bp','bR','bN','bB','bK','bQ']
    for piece in pieces:
        images[piece]=p.image.load("images/"+piece+".png"),(SQ_SIZE,SQ_SIZE)


def main():
    p.init()
    screen=p.display.set_mode((width,height))
    clock=p.time.Clock()
    screen.fill(p.Color("white"))
    gs=gamestate()
    loadimages()
    print(images)
    running = True
    while running:
        for e in p.event.get():
            if e.type==p.quit:
                runing=False
        drawgamestate(screen,gs)
        clock.tick(max_fps)
        p.display.flip()

def drawGamestate(screen,gs):
    drawboard(screen)
    drawpieces(screen,gs.board)

def drawboard(screen):
    colors=[p.Color("white"),p.Color("gray")]
    for r in range(dimension):
        for c in range(dimension):
            color=colors[((r+c)%2)]
            p.draw.rect(screen,color,p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))
           
def drawpieces(screen,board):
    for r in range(dimension):
        for c in range(dimension):
            piece=board[r][c]
            if piece!="--":
                screen.blit(images[piece],p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))

if __name__ == "__main__":
   main()      



