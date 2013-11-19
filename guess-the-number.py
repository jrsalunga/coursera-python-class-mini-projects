# Name: Jefferson Salunga
# @jrsalunga
# Mini-project # 2: “Guess the number”
# Coursera 
# An Introduction to Interactive Programming in Python
# URL: http://www.codeskulptor.org/#user21_7Mo2VHXWoaL5ejm.py

import simplegui
import math
import random

# initialize global variables needed to starts the game immediately 

num_range = 100
ctr = 7


# helper function to start and restart the game
def new_game():
    global num_range, ctr, rnd
    
    rnd = random.randrange(0, num_range)
    
    print "\nNew Game. Range is 0 to ",num_range
    print "Number of remaining guesses is ",ctr
    


# define event handlers for control panel
def range100():
   
    # button that changes range to range [0,100) and restarts
    global num_range, rnd, ctr
    num_range = 100
    ctr = 7
    rnd = random.randrange(0, num_range)
    new_game()
    


def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range, rnd, ctr
    num_range = 1000
    ctr = 10
    rnd = random.randrange(0, num_range)
    new_game()
    
    
    
def input_guess(guess):
    # main game logic goes here	
    global num_range, rnd, ctr
    guess = int(guess)

    if(ctr!=0):
        
        ctr = ctr - 1
        print "\nGuess was",guess
        print "Number of remaining guesses is",ctr
        
        #print rnd, "=", guess
        if rnd > guess:
            print "Higher!"
        elif rnd < guess:
            print "Lower!"
        else:
            print "Correct!"
            new_game()      
    else:
        print "\nSorry you lose!"
        print "Out of guess!"
        new_game()
       
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)


# register event handlers for control elements
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)



# call new_game and start frame
new_game()


# always remember to check your completed program against the grading rubric
