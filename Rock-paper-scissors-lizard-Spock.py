# Name: Jefferson Salunga
# @jrsalunga
# Mini-project # 1
# Coursera 
# An Introduction to Interactive Programming in Python
# URL: http://www.codeskulptor.org/#user20_VXN1yItrFV2ElDR.py


import random

# helper function: convert number to name
def name_to_number(name):
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else :
        return 'name not found'
    
# helper function: convert name to number 
def number_to_name(num):
    if num == 0:
        return 'rock'
    elif num == 1: 
        return 'Spock'
    elif num == 2:
        return 'paper'
    elif num == 3:
        return 'lizard'
    elif num == 4: 
        return 'scissors'
    else:
        return 'number not found'
    

    
#main function    
def rpsls(name):
    player_number = name_to_number(name)
    comp_number = random.randrange(0, 5)
    
    print 'Player chooses '+ number_to_name(player_number)
    print 'Computer chooses '+ number_to_name(comp_number)
    
    diff = ((player_number - comp_number) % 5) 
    
    if diff==1 or diff == 2:
        print 'Player wins!'
    elif diff==3 or diff == 4:
        print 'Computer wins!'
    else:
        print 'Player and Computer tie!'
        
    print ''
    
    
    
rpsls('rock')
rpsls('Spock')
rpsls('paper')
rpsls('lizard')
rpsls('scissors')