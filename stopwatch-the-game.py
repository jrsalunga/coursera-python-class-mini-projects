# Name: Jefferson Salunga
# @jrsalunga
# Mini-project # 3: “Stopwatch: The Game”
# Coursera 
# An Introduction to Interactive Programming in Python
# URL: http://www.codeskulptor.org/#user22_EdujtQFJuNgKMF4.py

import simplegui


# define global variables
interval = 100
ctr = 0
a = 0
b = 0
c = 0
d = 0
score1 = 0
score2 = 0
score = str(score1) + "/" + str(score2)
timex = "0:00.0"
isrunning = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global a, b, c, d
   
    d += 1
    
    if d >= 10:
        d = 0
        c +=1
    
    if c >= 10:
        c = 0
        b +=1
    
    if b >= 6:
        b = 0
        a += 1
  
    if a >= 10:
        a = 0
        
    
    
    return str(a) + ":" +str(b) + str(c) + "." +str(d)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global isrunning
    isrunning = True
    timer.start()
    
    


def stop():
    global score, score1, score2, d, isrunning
    
    if isrunning:
        if d == 0:
            score1 += 1
            
        score2 += 1 
        score = str(score1) + "/" + str(score2)
    
    timer.stop()
    isrunning = False


def reset():
    global ctr, a, b, c, d, score1, score2, score, timex
    ctr = 0
    a = 0
    b = 0
    c = 0
    d = 0
    score1 = 0
    score2 = 0
    score = str(score1) + "/" + str(score2)
    timex = "0:00.0"
    timer.stop()
    isrunning = False

# define event handler for timer with 0.1 sec interval
def tick():
    global ctr, timex
  
    ctr += 1
    
    if ctr >= 60:
        ctr = 0
    
    timex = format(ctr)
    
    
    

# define draw handler
def draw(canvas):
    canvas.draw_text(timex, [80, 120], 60, "White")
    canvas.draw_text(score, [250, 30], 30, "Red")

    
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 200)


# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", start)
frame.add_button("Stop", stop)
frame.add_button("Reset", reset)
timer = simplegui.create_timer(interval, tick)


# start frame
frame.start()


# Please remember to review the grading rubric
