import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

# card class is used to get suits and rank to make an object
class Card:
    
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    
    def __str__(self):
        return self.rank + ' of ' + self.suit
    
# deck class to make a deck of 52 cards with suits and ranks
        
class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        all_cards = " "
        for card in self.deck:
            all_cards += '\n '+card.__str__()
        return all_cards
    
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()
  
#  hand class is sued to make add card to hand from the deck and check for ace condition
       
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if  card.rank ==  'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -=1
  
#   chips class is used for calculating total bets and toatal balace amount to pay
    
class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet
        
        
# take_bet function is used to ask the player input amount to bet
        
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("enter the amount you are going to take bet :  "))
            if chips.bet>chips.total:
                print('you dont have enought value to take this bet',chips.total)
            else:
                break
        except ValueError:
            print('the value  must be an integer')

            # hit function is what happens if they hit 
    
def hit(deck,hand):
    
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

# hit_or_stand function is to ask the input from the players to hit or stand

def hit_or_stand(deck,hand):
    
    global playing  # to control an upcoming while loop
    
    while True:
        x = input("would you like to hit or stand pls enter h or s :")
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print('player choose stand dealer will start playing')
            playing = False
        else:
            print("pls provide crt value")
            continue
        break

# this function is show the first card of dealer hidden and show the two cards of  the player
            
def show_some(player,dealer):
    
    print("\n dealer hand")
    print("<HIDDEN>")
    print(dealer.cards[1])
    print("\n player hands")
    print(*player.cards , sep = "\n")
    
    # this function will show all the 2 cards of player and dealer
    
def show_all(player,dealer):
    print("\n")
    print(*dealer.cards , sep = "\n")
    print("\n dealer value is " ,dealer.value)
    print("\n")
    print(*player.cards , sep = "\n")
    print("\n player value is " ,player.value)


# the below function will check if the player or dealr wins or loose the game then what happens    

def player_busts(player,dealer,chips):
    print("player burst")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print('player wins')
    chips.win_bet()
       

def dealer_busts(player,dealer,chips):
    print("dealer burst")
    chip.lose_bet()
    
def dealer_wins(player,dealer,chips):
    print('dealer wins')
    chips.win_bet()
    
    
def push(player,dealer):
    print("its a tie")
    
    # here is the actual game logic starts
    
while True:
    
    # Print an opening statement
    print("welcome black jack game , get close to 21  and try to be greater than the dealer dealer hits until 17 and if value is greater than 21  ace can be considered  as 1 ")
    
    # Create & shuffle the deck, deal two cards to each player

    deck= Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
        
    # Set up the Player's chips
    player_chips = Chips()
    
    
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    print("\n player total value for the cards in hands " ,player_hand.value)
    
    while playing:# recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        print("\n player total value fo the cards in hands " ,player_hand.value)
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            print('player loose the game! better luck next time')
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value  <= 21:
        print('\n dealer will start playing')
        while dealer_hand.value <  17:
            hit(deck,dealer_hand)
    
        # Show all cards
        show_all(player_hand,dealer_hand)
        
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
             push(player_hand,dealer_hand)
    
    # Inform Player of their chips total 
    print("\n Balance of player chips   " ,player_chips.total)
    
    # Ask to play again
    new_game = input("\n would you like to play a new game y or n")
    
    if new_game[0].lower() == 'y':
        playing= True
        continue
     
    else:
        print("thanks for playing") 
        break
