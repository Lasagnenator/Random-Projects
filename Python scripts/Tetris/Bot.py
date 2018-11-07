#Tetris bot
#The window has equal space on the top and bottom
import ctypes
import time
import numpy as np

dc = ctypes.windll.user32.GetDC(0)

def get_pixel(pos):
    return ctypes.windll.gdi32.GetPixel(dc, pos[0], pos[1])
def get_pixelxy(x, y):
    return ctypes.windll.gdi32.GetPixel(dc, int(x), int(y))

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

def get_mouse_pos():
    pt = POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(pt))
    return pt.x, pt.y

key_down = lambda x:ctypes.windll.user32.keybd_event(x,0,0,0)
key_up = lambda x:ctypes.windll.user32.keybd_event(x,0,2,0)
hit_key = lambda x:(key_down(x),key_up(x))
set_mouse_pos = lambda x,y:ctypes.windll.user32.SetCursorPos(x,y)

right = 0x27
left = 0x25
soft = 0x28
rotate = 0x26
#rotate = 0x5a
hard = 0x20

next_colour_pos = (834, 212) # screen coordinates of next block
next_green_pos = (827, 207) #screen coordinates if the next block is green
bg = [1973021, 14994363, 16772828] #all background colours
btl = (430, 181) #board top left
bbr = (682, 657) #board bottom right

colours = {
    62196:'Yellow',
    16136645:'Purple',
    16199940:'Blue',
    28917:'Orange',
    62464:'Green',
    16106327:'Aqua',
    9463:'Red'}

blocks = {
    "Yellow":'T',
    "Purple":'J',
    "Blue":'L',
    "Orange":'I',
    "Green":'Z',
    "Aqua":'S',
    "Red":'O'}


r = np.linspace(btl[0], bbr[0], 10, endpoint=True, dtype=int)
c = np.linspace(btl[1], bbr[1], 18, endpoint=True, dtype=int)
c, r = np.meshgrid(r,c)
spawn_pos = (int(c[0][4]), int(r[0][0])) #current block spawn
empty_board = np.array([[0]*10]*20) #twenty here to not raise errors on I rotated

prev = 0

def get_board():
    return np.vectorize(get_colour)(np.vectorize(get_pixelxy)(c,r))
def mono_board(arr): #0 for empty, 1 for block
    arr[arr==None] = 0
    arr[arr!=0] = 1
    return arr

def wait_for_spawn():
    while get_colour(get_pixel(spawn_pos))==None:
        pass
    return get_block(get_pixel(spawn_pos))

def get_next_colour():
    next_colour = get_pixel(next_colour_pos)
    if next_colour in bg and (not get_pixel(next_green_pos) in bg):
        next_colour = get_pixel(next_green_pos)
    if not next_colour in bg:
        return next_colour

def get_current_block():
    return getblock(get_pixel(spawn_pos))

def get_colour(colour):
    try:return colours[colour]
    except:return
def get_block(colour):
    try:return blocks[colours[colour]]
    except:return

def start():
    key_down(0x12)
    hit_key(0x09)
    key_up(0x12)
    hit_key(0x0D)
    time.sleep(0.1)
    hit_key(hard)

def test_pixel_board(): #moves mouse to each center of block to test if it is correct
    for i in range(0,10):
        for j in range(0,18):
            set_mouse_pos(int(c[0][i]), int(r[j][0]))
            time.sleep(0.4)
    set_mouse_pos(next_colour_pos[0], next_colour_pos[1])

def get_piece_combs(piece): #Gets every possible orientation of a piece
    if piece == "I":
        start = np.array([[-1,0], [0,0], [1,0], [2,0]])
        rot1 = np.array([[0,1], [0,0], [0,-1], [0,-1]])
        rot2 = start
        rot3 = rot1
    elif piece == "O":
        start = np.array([[0,0], [1,0], [0,-1], [1,-1]])
        rot3 = rot2 = rot1 = start
    elif piece == "S":
        start = np.array([[-1,-1], [0,-1], [0,0], [1,0]])
        rot1 = np.array([[0,1], [0,0], [1,0], [1,-1]])
        rot2 = start
        rot3 = rot1
    elif piece == "Z":
        start = np.array([[-1,0], [0,0], [0,-1], [1,-1]])
        rot1 = np.array([[1,1], [1,0], [0,0], [0,-1]])
        rot2 = start
        rot3 = rot1
    elif piece == "L":
        start = np.array([[-1,-1], [-1,0], [0,0], [1,0]])
        rot1 = np.array([[-1,1], [0,1], [0,0], [0,-1]])
        rot2 = np.array([[-1,0], [0,0], [1,0], [1,1]])
        rot3 = np.array([[1,0], [0,0], [0,-1], [1,-1]])
    elif piece == "J":
        start = np.array([[-1,0], [0,0], [1,0], [1,-1]])
        rot1 = np.array([[-1,-1], [0,-1], [0,0], [0,1]])
        rot2 = np.array([[-1,1], [-1,0], [0,0], [1,0]])
        rot3 = np.array([[-1,0], [0,0], [0,1], [1,1]])
    elif piece == "T":
        start = np.array([[-1,0], [0,0], [0,-1], [1,0]])
        rot1 = np.array([[-1,0], [0,0], [0,-1], [0,1]])
        rot2 = np.array([[-1,0], [0,0], [0,1], [1,0]])
        rot3 = np.array([[1,0], [0,0], [0,-1], [1,0]])
    else:
        return
    return start, rot1, rot2, rot3 #rotating right
    return start, rot3, rot2, rot1 #rotating left

def local2global(arr, root): #arr and root are arrays. root is 0,0 local
    #converts local coordinates to global coordinates based on root
    return np.array(arr)+np.array(root)

def simulate_piece_drop(board, piece_rot, root): #returns a board with piece dropped from root
    #assumes that the root is valid and the whole piece can be placed with
    #nothing ovn the edges
    temp_board = np.append(empty_board, [1]*10) #floor
    #get board to be matching size
    board = np.insert(board, [0]*10, 0)
    board = np.insert(board, [0]*10, 0)
    board = board.append([0]*10)
    root += [0, -2]
    glob_rot = local2global(piece_rot, root)
    temp_board[glob_rot] = 1
    for i in range(0, 18):
        if 1 in temp_board&board: # if pieces collide
            break
        glob_rot += [0,-1] #lower piece by one
        prev = temp_board #store previous incase next has collision
        temp_board = empty_board
        temp_board[glob_rot] = 1
    fin = prev|board
    fin = fin[2:-1]
    return fin

def get_row_transitions(board):
    transitions = 0
    prev_block = 1
    for row in board:
        for block in row:
            if block != prev_block:
                transitions += 1
            prev_block = block
        prev_block = 1
    return transitions

def get_column_transitions(arr):
    transitions = 0
    prev_block = 1
    board = np.rot90(arr, -1)
    for column in board:
        for block in column:
            if block != prev_block:
                transitions += 1
            prev_block = block
        prev_block = 1
    return transitions

def get_holes(board):
    holes = 0
    board = board[::-1] #vertically flip the board
    for i in range(0, 18):
        row = board[i]
        for j in range(0,10):
            block = row[j]
            if i==0:
                floor = 1
            else:
                floor = board[i-1][j]
            if i==17:
                ceil = 1
            else:
                ceil = board[i+1][j]
            if floor == 1 and ceil == 1 and block == 0:
                holes += 1

def get_wells(arr): #Copied!
    wells = 0
    board = [0]*18
    i = 0
    for row in arr:
        board[i] = int(''.join(board[i]), 2)
        i+=1
    for i in range(1, 9): #Inner wells
        for j in range(17, -1, -1):
            if ((((board[j]>>i)&1)==0) and
                (((board[j]>>(i-1))&1)==1) and
                (((board[j]>>(i+1))&1)==1)):
                wells += 1
                for k in range(j-1, -1, -1):
                    if ((board[k]>>i)&1)==0:
                        wells += 1
                    else:
                        break
    for j in range(17, -1, -1): #Left wells
        if ((((board[j]>>0)&1)==0) and
            (((board[j]>> (0+1))&1)==1)):
            wells += 1
            for k in range(j-1, -1, -1):
                if ((board[k]>>0)&1)==0:
                    wells += 1
                else:
                    break
    for j in range(17, -1, -1): #Right wells
        if ((((board[j]>>9)&1)==0) and
            (((board[j]>>8)&1)==1)):
            wells += 1
            for k in range(j-1, -1, -1):
                if ((board[k]>>9)&1)==0:
                    wells += 1
                else:
                    break
    return wells

def get_height(board): #Find highest row with 1 in it
    height = 18
    for row in board:
        if 1 in row:
            break
        height -= 1
    return height

def get_rows_removed(board):
    removed = 0
    for row in board:
        if not 0 in row:
            removed += 1
    return removed
    
def eval_board(board): #board must not have cleared lines and pieces dropped.
    return (get_height(board)*-4.500158825082766+
            get_rows_removed(board)*3.4181268101392694+
            get_row_transitions(board)*-3.2178882868487753+
            get_column_transitions(board)*-9.348695305445199+
            get_holes(board)*-7.899265427351652+
            get_wells(board)*-3.3855972247263626)
            
def main():
    pass

print('break')
##while True:
##    next_colour = get_next_colour()
##    try:
##        if next_colour!=prev:
##            if get_colour(next_colour)!=None:
##                print(get_block(next_colour), get_colour(next_colour))
##            prev = next_colour
##    except:
##        pass
##    #print(get_pixel(next_green_pos))
while True:
    if get_pixel((568, 243))==0:
        hit_key(hard)
    #if wait_for_spawn()=="I":
        #hit_key(rotate)
        
    
