# -*- coding: utf-8 -*-
"""
Created on Sat May  9 16:25:26 2020

@author: sonu
"""
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

stillgoing = True

winner = None

cplayer = "X"

def disp():
    
    print(board[0] + "|" + board[1] +"|" + board[2])
    print(board[3] + "|" + board[4] +"|" + board[5])
    print(board[6] + "|" + board[7] +"|" + board[8])

def pgame():
     
    disp()
   
    while stillgoing:
       
        hturn(cplayer)
    
        over()
    
        flip()

    if winner == "X" or winner == "O" :
      print(winner  + " you won ")
    elif winner == None:
      print("tie")  
def hturn(player):
    
    print( player + "  now its your turn")
    possition = input("kon si jagah chiye choose kro   ")
    
    valid = False
         
    while not valid :
        
        while  possition not in ["1","2","3","4","5","6","7","8","9"]:
        
                  possition = input("Matlb kuch bhi daal do ")  
    
        possition = int(possition)-1
        
        if board[possition] =="-":
            valid = True
        else:
            print("dubara dalo no")
        board[possition] = player
    
    disp()

def over():
    
     win()
     tie()
    
def win():
    
    global winner
    # rows
    rowwin = rows()
    #column
    colwin = col()
    #digonals
    digwin = dig()
    
    if rowwin:
        winner = rowwin
    elif colwin:
        winner = colwin
    elif digwin:
        winner = digwin
    else :
        winner = None
    
    return

def rows():
    
    global stillgoing
    
    r1=board[0]== board[1] == board [2] !="-"
    r2=board[3]== board[4] == board [5] !="-" 
    r3=board[6]== board[7] == board [8] !="-"
           
    if r1 or r2 or r3 :
        
        stillgoing = False
    if r1 :
        return board[0]
    elif r2 :
        return board[3]
    elif r3 :
        return board[6]
        
    return

def col():
      
    global stillgoing
    
    c1=board[0]== board[3] == board [6] !="-"
    c2=board[1]== board[4] == board [7] !="-" 
    c3=board[2]== board[5] == board [8] !="-"
           
    if c1 or c2 or c3 :
        
        stillgoing = False
    if c1 :
        return board[0]
    elif c2 :
        return board[1]
    elif c3 :
        return board[2]
         
    return

def dig():
     
    global stillgoing
    
    d1=board[0]== board[4] == board [8] !="-"
    d2=board[6]== board[4] == board [2] !="-" 
           
    if d1 or d2 :
        
        stillgoing = False
    if d1 :
        return board[0]
    elif d2 :
        return board[6]
    
    return    


def tie():
    
    global stillgoing

    if " " in board :
        stillgoing = False
     
    return
def flip():
    
    global cplayer
    if cplayer == "X" :
     cplayer = "O"
    elif cplayer == "O" :
     cplayer = "X"
    return
pgame()