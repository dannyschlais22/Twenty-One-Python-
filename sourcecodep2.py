# prolog
# section 005
# Name: Daniel Schlais, drsc232@uky.edu
# Purpose: The program is a dicegame called Twenty-One, 2 players. The players will take turns rolling die or choosing to pass. The first player to reach or exceed 21 loses.
# Pre-conditions: The users must enter their player names and a response (P or R). Dice rolls are randomley generated. 
# Post-conditions: The program will output each round, what choices were made, the totals, who lost and who won the game. 

# import graphics
from graphics import *
import random
# Checks for point within defined region
def between(p1, p2, p3):
    return (p1.getX() <= p2.getX() <= p3.getX()) and \
           (p1.getY() <= p2.getY() <= p3.getY())
# Sets die image to the anchor point
def d_die(value, win, anchorPoint):
    filename = f"{value}.gif"
    img = Image(anchorPoint, filename)
    img.draw(win)
    return img

# define pass or roll
#purpose: get user choice for turn, pass or roll
#precon: name(parameter, sting) and choice (input)
#postcon: user response (R or P)
def pass_roll(name, win):
    
    prompt = Text(Point(250, 100), f"{name}: Pass or Roll?")
    prompt.setSize(18)
    prompt.draw(win)
    
    pass_rec = Rectangle(Point(100, 140), Point(200, 200))
    pass_rec.setFill("lightgray")
    pass_rec.draw(win)
    pass_lab = Text(Point(150, 170), "Pass")
    pass_lab.draw(win)
    
    roll_rec = Rectangle(Point(300, 140), Point(400, 200))
    roll_rec.setFill("lightgray")
    roll_rec.draw(win)
    roll_lab = Text(Point(350, 170), "Roll")
    roll_lab.draw(win)
    
    choice = ""
# while input is not "P" and not "R":
    while choice == "":
        click = win.getMouse()
        if between(Point(100, 140), click, Point(200, 200)):
            choice = "P"
        elif between(Point(300, 140), click, Point(400, 200)):
            choice = "R"
    #cleanup
    prompt.undraw()   
    pass_rec.undraw()
    pass_lab.undraw()
    roll_rec.undraw()
    roll_lab.undraw()
    
    return choice

# define play turn
#purpose: to carry out each turn for each player, a player rolls or passes, if available.
#precon: player name (string), total (int) and passes (int)
#postcon: returns updated totals and passes
def play_turn(name, total, passes, win, die_anchor, pmsg):
    roll_value = 0
# if passes > 0:
    if passes > 0:
        choice = pass_roll(name, win)
# if choice == "P"    
        if choice == "P":
            passes -= 1
            pmsg.setText(f"{name} passed.")
            die_img = d_die(0, win, die_anchor)
        else:
            roll_value = random.randint(1, 6) # generate random die roll
            total += roll_value # update totals
            pmsg.setText(f"{name} rolled a {roll_value}.")
            die_img = d_die(roll_value, win, die_anchor)
    else:
        roll_value = random.randint(1, 6)
        total += roll_value
        pmsg.setText(f"{name} rolled a {roll_value}.")
        die_img = d_die(roll_value, win, die_anchor)
        
    win.getMouse()
    
    #cleanup
    die_img.undraw()
    pmsg.setText("")
    
 # return total and passes       
    return total, passes

# main program
def main():
    # create window
    win = GraphWin("Twenty One", 500, 500)
    
    head_anchor = Point(250, 50)
    msg_anchor = Point(250, 350)
    p1_anchor = Point(100, 50)
    p2_anchor = Point(400, 50)
    die_anchor = Point(250, 250)
    
    header = Text(head_anchor, "")
    header.setSize(20)
    header.draw(win)
    
    p1_t = Text(p1_anchor, "")
    p1_t.setSize(12)
    p1_t.draw(win)
    p2_t = Text(p2_anchor, "")
    p2_t.setSize(12)
    p2_t.draw(win)
    
    msg_obj = Text(msg_anchor, "")
    msg_obj.setSize(16)
    msg_obj.draw(win)
    
    name_l1 = Text(Point(250, 100), "Enter Player 1: ")
    name_l1.draw(win)
    z1 = Entry(Point(250, 130), 20)
    z1.draw(win)
    
    name_l2 = Text(Point(250, 170),"Enter player 2: ")
    name_l2.draw(win)
    z2 = Entry(Point(250, 200), 20)
    z2.draw(win)
    
    msg_obj.setText("Click to continue")
    win.getMouse()
    
    player1 = z1.getText()
    player2 = z2.getText()
    
    #cleanup
    name_l1.undraw()
    name_l2.undraw()
    z1.undraw()
    z2.undraw()
    msg_obj.setText("")
    
# initialize totals 
    total1 = 0
    total2 = 0
    passes1 = 3
    passes2 = 3
    round_n = 1
    
    while total1 < 21 and total2 < 21:
        
        header.setText(f"Round {round_n}")
        
        total1, passes1 = play_turn(player1, total1, passes1, win, die_anchor, msg_obj)
        
        p1_t.setText(f"{player1}: {total1} (passes {passes1})")
        p2_t.setText(f"{player2}: {total2} (passes {passes2})")
        
        if total1 < 21:
            
            total2, passes2 = play_turn(player2, total2, passes2, win, die_anchor, msg_obj)
            
            p1_t.setText(f"{player1}: {total1} (passes {passes1})")
            p2_t.setText(f"{player2}: {total2} (passes {passes2})")
        
        round_n +=1
        
    header.setText("Game Over")
    
    if total1 >= 21:
        msg_obj.setText(f"{player2} wins! Click to exit.")
    else:
        msg_obj.setText(f"{player1} wins! Click to exit.")
            
    win.getMouse()
    win.close()
    
main() # end main program