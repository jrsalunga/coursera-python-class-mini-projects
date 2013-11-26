# Name: Jefferson Salunga
# @jrsalunga
# Mini-project # 6: "Blackjack"
# Coursera 
# An Introduction to Interactive Programming in Python
# URL: http://www.codeskulptor.org/#user26_PaWLb1YZEC_7.py


import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = [0,0]
# score[0] = dealer
# score[1] = player
card_points = ['','']


# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.player_hand = []

    def __str__(self):
        # return a string representation of a hand
        s = ''
        for c in self.player_hand:
            s = s + str(c) + ' '
        return s

    def add_card(self, card):
        # add a card object to a hand
        self.player_hand.append(card)
        return self.player_hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        value = 0
        for card in self.player_hand:
            rank = card.get_rank()
            value = value + VALUES[rank]
        for card in self.player_hand:
            rank = card.get_rank()    
            if rank == 'A' and value <= 11:
                value += 10
        return value
        
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for card in self.player_hand:
            card.draw(canvas, pos)
            pos[0] = pos[0] + 90
        if in_play == True:
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [165.5,204], CARD_BACK_SIZE)
 
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        #popped = []
        self.cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]
        self.shuffle()

    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        random.shuffle(self.cards)

    def deal_card(self):
        # deal a card object from the deck
        return self.cards.pop(0)
        #return popped
    
    def __str__(self):
        # return a string representing the deck
        s = ''
        for c in self.cards:
            s = s + str(c) + ' '
        return s



# helper function
def new_sets():
    global player, dealer, deck

    deck = Deck()
    player = Hand()
    dealer = Hand()
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())

#define event handlers for buttons        
def deal():
    global outcome, in_play, score, message, card_points
    card_points = ['','']
    
    if in_play == True:
        # if player clicks Deal button during game in progress, player loses
        score[0] += 1 # dealer score +1
        new_sets()
        message = "Here are the new set of cards"    
    else:
        # starts a new game
        new_sets()
        message = "New Game: Hit or Stand?"
        in_play = True
    
    outcome = ""

def hit():
    global in_play, score, message, card_points
    # deals player a new hand and ends hand if it causes a bust.
    
    # check if the game is in progress
    if in_play == False:
        message = "The game is already over. Deal again?"
    else:
        player.add_card(deck.deal_card()) #player can hit
        message = "Hit again or Stand?"
        
        # if busted, assign a message to outcome, update in_play and score
        if player.get_value() > 21:
            in_play = False
            message = "You Lose! Busted! Play again?"
            score[0] += 1
            card_points[0] = str(dealer.get_value())
            card_points[1] = str(player.get_value())
            outcome = "Dealer: " + str(dealer.get_value()) + "  Player: " + str(player.get_value())
  
def stand():   
    global in_play, score, message, outcome, card_points
    
    # check if the game is in progress
    if in_play == False:
        message = "The game is already over. Deal again?"
    else:
        # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
        
        # check the card values of each player 
        if dealer.get_value() > 21:
            message = "You win! Dealer busted. Play again?"
            card_points[0] = str(dealer.get_value())
            card_points[1] = str(player.get_value())
            score[1] += 1           
        elif dealer.get_value() > player.get_value():
            message = "Dealer win! Play again?"
            score[0] += 1   
        elif dealer.get_value() == player.get_value():
            message = "Tie! Dealer wins! Play again?"
            score[0] += 1
        elif dealer.get_value() < player.get_value():
            message = "You win! Play again?"
            score[1] += 1
       
        in_play = False
        
        # assign a message to outcome, update in_play and score
        card_points[0] = str(dealer.get_value())
        card_points[1] = str(player.get_value())
        outcome = "Dealer: " + str(dealer.get_value()) + "  Player: " + str(player.get_value())
        
   

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    canvas.draw_text("Blackjack", [270,50], 48, "Yellow")
    #canvas.draw_text("Score : " + str(score), [80,520], 36, "Black")
    
    canvas.draw_text("Dealer :", [130,110+30], 30, "Black")
    canvas.draw_text("Player :", [130,300+20], 30, "Black")
    
    canvas.draw_text(str(score[0]), [250,110+30], 40, "White")
    canvas.draw_text(str(score[1]), [250,300+20], 40, "White")
    
    canvas.draw_text(card_points[0], [50,190+20], 50, "White")
    canvas.draw_text(card_points[1], [50,385+10], 50, "White")
    
    
    canvas.draw_text(message, [130,500], 30, "Black")
    #canvas.draw_text(outcome, [80,560], 28, "White")
    
    dealer.draw(canvas, [130,135+20])
    player.draw(canvas, [130,325+10])


# initialization frame
frame = simplegui.create_frame("Blackjack", 700, 550)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric