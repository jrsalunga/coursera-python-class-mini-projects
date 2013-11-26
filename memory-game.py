# Name: Jefferson Salunga
# @jrsalunga
# Mini-project # 5: "Memory"
# Coursera 
# An Introduction to Interactive Programming in Python
# URL: http://www.codeskulptor.org/#user25_BzhIdd17IPjAyG6.py

import simplegui
import random

# helper function to initialize globals
def new_game():
    global state, cards, moves
    state = 0 
    moves = 0
    cards = []
    
    for i in range(16):
        x = i % 8
        cards.append([x, False])

    random.shuffle(cards)
     
# define event handlers
def mouseclick(pos):
    global state, cards, cardone, cardtwo, moves

    # if the y coordinate of pos is within the frame and the card you clicked on is face down
    if 0 <= pos[1] <= 100 and cards[pos[0] // 50][1] == False: 
        if state == 0:
            state = 1
            cardone = pos[0] // 50
            cards[(pos[0] // 50)][1] = True
        elif state == 1:
            state = 2
            cardtwo = pos[0] // 50
            cards[(pos[0] // 50)][1] = True
            moves += 1
        elif state == 2:
            state = 1
            if cards[cardone][0] != cards[cardtwo][0] :
                cards[cardone][1] = False
                cards[cardtwo][1] = False
            cardone = pos[0] // 50
            cards[pos[0] // 50][1] = True
    else:
        print 'Card is already exposed!'    

                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global cards, state
    label.set_text("Moves = " + str(moves))
    for c in range(len(cards)):
        if cards[c][1] == True:
            canvas.draw_text(str(cards[c][0]), (c*50 + 10, 75), 50, "grey")
        elif cards[c][1] == False:
            canvas.draw_polygon([(c*50, 0), ((c+1)*50, 0), ((c+1)*50, 100), (c*50, 100)], 1,"black", "green")


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Moves = 0")

# initialize global variables
new_game()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()


# Always remember to review the grading rubric