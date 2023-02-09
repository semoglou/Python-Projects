import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}

playing = True

# Card Class (to initiate a card given suit and rank)
class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank +' of '+self.suit

# Deck Class (to create a deck from the given cards)
class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)     # card objects (to put inside the "deck") 
                self.deck.append(card)
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '/n'+ card.__str__()
        return "The deck has"+deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

# Hand Class (to add the cards from Deck Class to the player's hand)
class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 1:
            self.value-=10
            self.aces-=1

# Chips Class (to keep track of a Player's starting chips, bets, and ongoing winnings)
class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0
    
    def win_bet(self):
        self.total+=self.bet

    def lose_bet(self):
        self.total-=self.bet

# Functions :
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet ? "))
        except ValueError:
            print("Sorry, a bet must be an integer!")
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed your total chips ", chips.total)
            else:
                break

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace

def hit_or_stand(deck, hand):
    global playing
    while True:
        answer = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
        if answer[0].lower() == 'h':
            hit(deck, hand)
        elif answer[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False
        else:
            print("Sorry, please try again.")
            continue
        break

def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')

def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

def player_busts(player, dealer, chips):
    print("Player Busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player Wins!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("Dealer Busts!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("Dealer Wins!")
    chips.lose_bet()

def push(player, dealer):
    print("Dealer and Player tie! It's a push!")

# BlackJack Game:

def BlackJack():
    while True:
        print("Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
            Dealer hits until he/she reaches 17. Aces count as 1 or 11. ")

        # Create and Shuffle the deck, then deal two cards to each player

        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        # Chips
        player_chips = Chips()

        # Bet
        take_bet(player_chips)

        # Show Cards but keep one dealer-card hidden
        show_some(player_hand, dealer_hand)
        global playing
        while playing:
            hit_or_stand(deck, player_hand)
            show_some(player_hand, dealer_hand)
            if player_hand.value > 21:
                player_busts(player_hand, dealer_hand, player_chips)
                break
        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(deck, dealer_hand)
            show_all(player_hand, dealer_hand)

            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand,player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)
            else:
                push(player_hand, dealer_hand)
        print("\nPlayer's winnings stand at ",player_chips.total)
        new_game = input("\nWould you like to play again? Enter 'y' or 'n' ")
        if new_game[0].lower() == 'y':
            playing = True
            continue
        else:
            print("\nThanks for playing!")
            break                              # The End
        
        
BlackJack()       
                





