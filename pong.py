# Name: Jefferson Salunga
# @jrsalunga
# Mini-project # 4: "Pong"
# Coursera 
# An Introduction to Interactive Programming in Python
# URL: http://www.codeskulptor.org/#user25_zOk0fTXlq3IvsGZ.py

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

ball_pos = [WIDTH/2 , HEIGHT/2]
ball_vel = [0, 0]

paddle1_pos = HEIGHT / 2
paddle2_pos = HEIGHT / 2

paddle1_vel = 0
paddle2_vel = 0

paddle_speed = 4

score1 = 0
score2 = 0




# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists   
    
    ball_pos = [WIDTH/2 , HEIGHT/2]

    if direction == 'left':
        ball_vel[0] = random.randrange(120, 240) / 100
    else:
        ball_vel[0] = -(random.randrange(120, 240) / 100)
    
    ball_vel[1] = -(random.randrange(60, 180) / 100)
    
    #print ball_vel
    
    if score1 == 5 or score2 == 5:
        ball_pos = [WIDTH/2 , HEIGHT/2]
        ball_vel = [0, 0]
   
        


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2, ball_vel  # these are ints
        
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2
    ball_pos = [WIDTH/2 , HEIGHT/2]
    score1 = score2 = 0
    ball_vel[0] = random.randrange(120, 240) / 100
    ball_vel[1] = random.randrange(60, 180) / 100

def increase_speed():
    global ball_vel
    
    ball_vel[0] = ball_vel[0] + 1
    ball_vel[1] = ball_vel[1] + 1 
    
    print ball_vel
    

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global paddle1_vel, paddle2_vel
 
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    #print ball_pos, ball_vel
    
    #check for bottom collision
    if ball_pos[1] + BALL_RADIUS >= HEIGHT :
        ball_vel[1] = -ball_vel[1]
        
    #check for right collision    
    if ball_pos[0] + BALL_RADIUS >= WIDTH - 8 :
        paddle2 = [paddle2_pos-HALF_PAD_HEIGHT, paddle2_pos+HALF_PAD_HEIGHT]
        #print ball_pos[1], paddle2
        if ball_pos[1] >= paddle2[0] and ball_pos[1] <= paddle2[1]:
            increase_speed()
            ball_vel[0] = -ball_vel[0]
        else: 
            score1 += 1
            spawn_ball('left')
                       
    #check for top collision
    if ball_pos[1] - BALL_RADIUS <= 0 :
        ball_vel[1] = -ball_vel[1]
    #check for left collision    
    if ball_pos[0] - BALL_RADIUS <= 0 + 8:
        paddle1 = [paddle1_pos-HALF_PAD_HEIGHT, paddle1_pos+HALF_PAD_HEIGHT]
        if ball_pos[1] >= paddle1[0] and ball_pos[1] <= paddle1[1]:
            
            ball_vel[0] = -ball_vel[0]
            increase_speed()
        else: 
            score2 += 1
            spawn_ball('right')
        
                  
    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 1, "Red", "White")
    
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    
    if paddle1_pos - PAD_HEIGHT/2 <= 0:
        paddle1_vel = 0
    if paddle1_pos + PAD_HEIGHT/2 >= HEIGHT:
        paddle1_vel = 0
    if paddle2_pos - PAD_HEIGHT/2 <= 0:
        paddle2_vel = 0
    if paddle2_pos + PAD_HEIGHT/2 >= HEIGHT:
        paddle2_vel = 0
   
    
    # draw paddles
    paddle1_tl = [0, paddle1_pos-PAD_HEIGHT/2]
    paddle1_tr = [PAD_WIDTH, paddle1_pos-PAD_HEIGHT/2]
    paddle1_br = [PAD_WIDTH, paddle1_pos+PAD_HEIGHT/2]
    paddle1_bl = [0, paddle1_pos+PAD_HEIGHT/2]
    
    paddle2_tl = [WIDTH-PAD_WIDTH, paddle2_pos-PAD_HEIGHT/2]
    paddle2_tr = [WIDTH, paddle2_pos-PAD_HEIGHT/2]
    paddle2_br = [WIDTH, paddle2_pos+PAD_HEIGHT/2]
    paddle2_bl = [WIDTH-PAD_WIDTH, paddle2_pos+PAD_HEIGHT/2]
    
    c.draw_polygon([paddle1_tl, paddle1_tr, paddle1_br, paddle1_bl], 1, 'White', 'White')
    c.draw_polygon([paddle2_tl, paddle2_tr, paddle2_br, paddle2_bl], 1, 'White', 'White')
    
    
    # draw scores
    c.draw_text(str(score1), [(WIDTH/2)/2, 60], 50, "White")
    c.draw_text(str(score2), [(WIDTH/2)+(WIDTH/2)/2, 60], 50, "White")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["up"]:
        if paddle2_pos - PAD_HEIGHT/2 <= 0:
            paddle2_vel = 0
        else:
            paddle2_vel = -paddle_speed
    if key == simplegui.KEY_MAP["down"]:
        if paddle2_pos + PAD_HEIGHT/2 >= HEIGHT:
            paddle2_vel = 0
        else:
            paddle2_vel = +paddle_speed
    if key == simplegui.KEY_MAP["w"]:
        if paddle1_pos - PAD_HEIGHT/2 <= 0:
            paddle1_vel = 0
        else:
            paddle1_vel = -paddle_speed
    if key == simplegui.KEY_MAP["s"]:
        if paddle1_pos + PAD_HEIGHT/2 >= HEIGHT:
            paddle1_vel = 0
        else:
            paddle1_vel = +paddle_speed
    
        
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.add_button('Start New Game', new_game, 200)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
#new_game()
frame.start()
