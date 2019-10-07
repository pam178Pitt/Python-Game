from random import shuffle
print("Project 3 By: Patrick Mayer")
print("---------------------------")
#uses total of 4 classes
#create card clas
class Card(object):
    def __init__(self, player, funds=1000):
        self.dealer = Dealer()
        self.player = Player(player, funds)
        self.deck = Deck()
        self.cards()

    def dealer_hit(self):
        score = self.dealer.score
        if score <= 16:
            self.deal(self.dealer)
            self.calculate_score(self.dealer)
            print(self)
        else:
            self.check_final_score()
            self.end_game()

    def __str__(self):  #format game
        dealer_hand = [card for card, value in self.dealer.hand]
        player_hand = [card for card, value in self.player.hand]
        print("Dealer hand: {}".format(dealer_hand))
        print("Hand Value: {}".format(self.dealer.score))
        print("------------------")
        print("{}'s hand: {}".format(self.player.name, player_hand))
        print("{}'s hand value: {}".format(self.player.name, self.player.score))
        print("------------------")
        print(("{}'s current bet: {}".format(self.player.name, self.player.bet)))
        print("{}'s current funds: {}".format(self.player.name, self.player.funds))
        print("------------------")
        return " "
        print()

    def deal(self, player):
        card = self.deck.stack.pop()  #return card removed from list @w3schools
        player.hand.append(card)  #append cards into hand

    def calculate_score(self, player):
        ace = False  
        score = 0
        for card in player.hand:
            if card[1] == 1 and not ace:
                ace = True
                card = ('A', 11)
            score += card[1]
        player.score = score
        if player.score > 21 and ace:
            player.score -= 10
            score = player.score
        self.check_win(score, player)
        return

    def check_win(self, score, player):
        if score == 21:
            print()
            print(self)
            print("{} wins".format(player.name))
            print()
            self.end_game()
        elif score > 21:
            print(self)
            print("{} busts".format(player.name))
            self.end_game()
            
    def check_final_score(self):
        dealer_score = self.dealer.score
        player_score = self.player.score
        if dealer_score > player_score:
            print("Dealer wins")
            self.end_game()
        else:
            print("{} wins!".format(self.player.name))
            self.end_game()

    def end_game(self):
        bank = self.player.funds
        if bank >=0:
            again = input("Would you like to play again (Y/N)? ")
            if again.lower().startswith('y'):
                self.__init__(self.player.name, funds=self.player.funds)
            elif again.lower().startswith('n'):
                exit()  
        elif bank < 100:
            print("You are broke!")
    
    def cards(self):
        self.deal(self.player)
        self.deal(self.dealer)                     
        self.calculate_score(self.player)  
        self.calculate_score(self.dealer)
        self.deck.shuffle()
        self.player.place_bet()
        self.main()

    def main(self):
        while True:
            print(self)
            player_move = self.player.hit_or_stand()
            if player_move:
                self.deal(self.player)
                self.calculate_score(self.player)
            elif self.dealer.score <= 16:
                self.dealer_hit()
            else:
                self.check_final_score()
                self.end_game()
    
#create dealer class, could not identify way to store hand outside of class
class Dealer(object):
    def __init__(self):
        self.name = "Dealer"
        self.score = 0  #dealer score
        self.hand = []  #dealer hand

#It was in fact beneficial to use classes for the player and dealer:)
#Create player class to store funds
class Player(Dealer): 
    def __init__(self, name, funds, bet=0):
        super().__init__()  #super used to gain access to inherited method
        self.name = name
        self.funds = funds
        self.bet = bet
    def place_bet(self, amount=100):         
        self.funds -= amount
        self.bet += amount
    
    @staticmethod  #no parameters
    def hit_or_stand():
        while True:
            choice = input("Would you like to hit (Y/N)? ")
            if choice == "y" or choice == "Y":
                return True
            elif choice == "n" or choice =="N":
                return False
            
#create deck class
class Deck(object):    
    def __init__(self):       
        self.stack = [('A', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5),
                      ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10),  #assign values to cards
                      ('Jack', 10), ('Queen', 10), ('King', 10)] * 4  #assign values to entire deck
        self.shuffle() 
    def shuffle(self):
        shuffle(self.stack)#shuffle list of cards
    def deal(self):
        card = self.stack.pop()  #returns last item.pop
        return card
    
def main():   #program main function begin
    name = input("Enter your name? ")
    if name == "Muneeb" or name == "muneeb":  #Merry Christmas
        print("Greetings Professor")
        print("Have a Happy Holidays")
        print()
    else:
        pass
    Card(name)
        
if __name__ == '__main__':
    main() #final call of main function
    

