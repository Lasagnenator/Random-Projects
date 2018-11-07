import pygame,random
from pygame.locals import *
pygame.font.init()

PLAYERS=int(input('players: '))
COLUMN_AMOUNT=int(input("Amount of columns (enter 0 for default): "))
if COLUMN_AMOUNT==0:
    COLUMN_AMOUNT=20
ROW_AMOUNT=int(input("Amount of rows (enter 0 for default): "))
if ROW_AMOUNT==0:
    ROW_AMOUNT=20
mine_ratio=int(input("Percent of mines (enter 0 for default): "))/100.0
tile_amount=ROW_AMOUNT*COLUMN_AMOUNT
if mine_ratio==0:
    MINE_AMOUNT=int(tile_amount/5)
else:
    MINE_AMOUNT=int(tile_amount*mine_ratio)
screen=pygame.display.set_mode([700,700])
cell_pic=pygame.image.load('cell.png')
cell_pressed=pygame.image.load('cell_pressed.png')
cell_flagged=pygame.image.load('cell_flagged.png')
font=pygame.font.Font(None,16)

class Cell:
    def init(self,pos):
        self.pos=pos
        self.mine=0
        self.flagged=0
        self.pushed=0
        self.number=0
        self.rect=pygame.rect.Rect([pos,[16,16]])
    def detect(self,cells):
        minecount=0
        for a in range(-1,2):
            for b in range(-1,2):
                temppos=[self.pos[0]/16+a,self.pos[1]/16+b]
                if not (temppos[0]==COLUMN_AMOUNT or temppos[1]==ROW_AMOUNT or temppos[0]==-1 or temppos[1]==-1):
                    try:
                        if cells[temppos[0]][temppos[1]].mine:
                            minecount=minecount+1
                    except IndexError:
                        print('ERROR: Index error 4')
        self.mines=minecount
    def draw(self,pressed):
        if pressed or self.pushed:
            screen.blit(cell_pressed,self.pos)
            if self.pushed and self.mines!=0:
                if self.number==0:
                    number=font.render(str(self.mines),1,[0,0,0])
                    screen.blit(number,[self.pos[0]+5,self.pos[1]])
                else:
                    screen.blit(cell_pic,self.pos)
                    number=font.render(str(self.number),1,[0,0,255])
                    screen.blit(number,[self.pos[0]+5,self.pos[1]])
        elif not (pressed or self.pushed):
            if not self.flagged:
                screen.blit(cell_pic,self.pos)
            else:
                screen.blit(cell_flagged,self.pos)
    def click(self,cells):
        self.pushed=1
        return [self.mine,not self.mines]
    def flag_toggle(self):
        if self.flagged:
            self.flagged=0
        else:
            self.flagged=1
    def claim(self,number):
        self.number=number

def main():
    if PLAYERS>1:
        turn=1
    cells=[]
    clicked_cells=[]
    clicked=0
    for a in range(COLUMN_AMOUNT):
        cells.append([])
    for a in range(ROW_AMOUNT):
        for column in range(len(cells)):
            cells[column].append(Cell())
    for column in range(len(cells)):
        for row in range(len(cells[column])):
            cells[column][row].init([column*16,row*16])
    for mine in range(MINE_AMOUNT):
        minepos=[random.randint(0,COLUMN_AMOUNT-1),random.randint(0,ROW_AMOUNT-1)]
        try:
            while cells[minepos[0]][minepos[1]].mine:
                minepos=[random.randint(0,COLUMN_AMOUNT-1),random.randint(0,ROW_AMOUNT-1)]
        except IndexError:
            print('ERROR: index error 2')
            print('minepos:',minepos)
            return 0
        cells[minepos[0]][minepos[1]].mine=1
    for column in range(len(cells)):
        for row in range(len(cells[column])):
            cells[column][row].detect(cells)
    while 1:
        screen.fill([0,0,0])
        if PLAYERS>1:
            turn_display=font.render('Player '+str(turn),1,[0,255,0])
            screen.blit(turn_display,[COLUMN_AMOUNT*16+5,5])
            for player in range(1,PLAYERS+1):
                playerscore=0
                for column in cells:
                    for cell in column:
                        if cell.number==player:
                            playerscore=playerscore+1
                score=font.render(str(player)+': '+str(playerscore),1,[255,255,255])
                screen.blit(score,[COLUMN_AMOUNT*16+5,player*20+40])
        pos=pygame.mouse.get_pos()
        for column in cells:
            for cell in column:
                cell.draw(0)
        for event in pygame.event.get():
            if event.type==QUIT:
                return 0
            if event.type==MOUSEBUTTONUP and (event.pos[0]<ROW_AMOUNT*16 and event.pos[1]<COLUMN_AMOUNT*16):
                if event.button==1:
                    clicked_cells.append([event.pos[0]/16,event.pos[1]/16])
                    clicked=1
                    [mined,empty]=cells[event.pos[0]/16][event.pos[1]/16].click(cells)
                    if mined:
                        if PLAYERS==1:
                            return 1
                        else:
                            cells[event.pos[0]/16][event.pos[1]/16].claim(turn)
                    elif PLAYERS>1:
                        turn=turn+1
                        if turn>PLAYERS:
                            turn=1
                elif event.button==3 and PLAYERS==1:
                    cells[event.pos[0]/16][event.pos[1]/16].flag_toggle()
        templist=[]
        for cell in clicked_cells:
            [mined,empty]=cells[cell[0]][cell[1]].click(cells)
            if empty:
                for a in range(-1,2):
                    for b in range(-1,2):
                        temppos=[cell[0]+a,cell[1]+b]
                        if temppos[0]==COLUMN_AMOUNT or temppos[1]==ROW_AMOUNT or temppos[0]==-1 or temppos[1]==-1:
                            break
                        try:
                            if not cells[temppos[0]][temppos[1]].pushed:
                                templist.append([temppos[0],temppos[1]])
                        except IndexError:
                            print('ERROR: index error 2')
                            print('a, b:',a,b)
                            print('temppos:',temppos)
        clicked_cells=[]
        for cell1 in templist:
            try:
                if not cells[cell1[0]][cell1[1]].pushed:
                    match=0
                    for cell2 in clicked_cells:
                        if cell1==cell2:
                            match=1
                    if not match:
                        clicked_cells.append(cell1)
            except IndexError:
                print('ERROR: index error 1')
                print('cell1:',cell1)
                print('cell2:',cell2)
                return 0
        if templist!=[]:
            clicked_cells.append(templist[0])
        for cell1 in templist:
            match=0
            for cell2 in clicked_cells:
                if cell1==cell2:
                    match=1
            if not match:
                clicked_cells.append(cell1)
        if (pygame.mouse.get_pressed()[0] or clicked) and (event.pos[0]<ROW_AMOUNT*16 and event.pos[1]<COLUMN_AMOUNT*16):
            cells[pos[0]/16][pos[1]/16].draw(1)
        clicked=0
        pygame.display.flip()
                

while main()==1:
    pass
