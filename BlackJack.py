import random
import time
import sys


class Card:

    def __init__(self, val, su1t, card_val):
        self.value = val
        self.suit = su1t
        self.card_value = card_val

    def show(self):
        print(f"{self.value} of {self.suit}")


class Deck:
    def __init__(self):
        self.deck = []
        values = {"Ace": 11,
                  2: 2,
                  3: 3,
                  4: 4,
                  5: 5,
                  6: 6,
                  7: 7,
                  8: 8,
                  9: 9,
                  10: 10,
                  "Jack": 10,
                  "Queen": 10,
                  "King": 10}

        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in values:
                self.deck.append(Card(v, s, values.get(v)))

    def shuffle(self):
        for x in range(len(self.deck)-1, 0, -1):
            r = random.randint(0, x)
            self.deck[x], self.deck[r] = self.deck[r], self.deck[x]

    def draw(self):
        return self.deck.pop()

    def show(self):
        for card in self.deck:
            card.show()


class BlackJack:
    def __init__(self):
        self.players_cards = []
        self.dealers_cards = []
        self.money = 100
        self.players_score = 0
        self.dealers_score = 0
        self.bet = 0

    def round(self, round):
        print(f"Round {round}")
        print()
        print(f"You have ${self.money} left")
        time.sleep(0.4)
        while True:
            if self.money == 0:
                print("No money left")
                print("Restart the program")
                sys.exit()

            self.bet = float(input("Make your bet: "))
            if self.bet > self.money:
                print("Not enough $")
                print()
                pass
            elif self.bet < 0:
                print("Bet can't be negative")
                print()
                pass
            else:
                break

        self.money -= self.bet
        print(f"${self.money} left")

    def player_draws(self):
        self.players_cards.append(deck.draw())
        self.players_score = 0

        for card in self.players_cards:
            self.players_score += card.card_value
            if card.value == "Ace":
                if game.players_score > 21:
                    self.players_score -= 10
        return self

    def dealer_draws(self):
        self.dealers_cards.append(deck.draw())
        self.dealers_score = 0
        
        for card in self.dealers_cards:
            self.dealers_score += card.card_value
            if card.value == "Ace":
                if game.dealers_score > 21:
                    self.dealers_score -= 10
        return self

    def show1(self):
        print()
        print("Your cards:")
        for card in self.players_cards:
            time.sleep(0.7)
            card.show()
        time.sleep(0.7)
        print(f"[{self.players_score}]")
        print()

        print("Dealers cards:")
        for card in self.dealers_cards:
            time.sleep(0.7)
            card.show()
        time.sleep(0.7)
        print("*Secret card*")
        time.sleep(0.7)
        print(f"[{self.dealers_score}]")

    def show2(self):
        print()
        print("Your cards:")
        for card in self.players_cards:
            time.sleep(0.7)
            card.show()
        time.sleep(0.7)
        print(f"[{self.players_score}]")

        if self.players_score <= 21:
            print()
            print("Dealers cards:")
            for card in self.dealers_cards:
                time.sleep(0.7)
                card.show()
            time.sleep(0.7)
            print(f"[{self.dealers_score}]")

    def blackjack(self):
        print()
        print(f"{self.players_score}! BLACKJACK!")
        print("You lucky mf!")

    def lose(self):
        print()
        print("YOU LOSE!")
        print(f"You lose your bet of ${self.bet}")
        print(f"${self.money} left")

    def win(self):
        print()
        print("YOU WIN")
        self.bet *= 1.5
        print(f"You got ${self.bet} richer")
        self.money += self.bet
        print(f"${self.money} left")

    def draw(self):
        print()
        print("DRAW")
        self.money += self.bet
        print(f"${self.money} left")


deck = Deck()
deck.shuffle()

print("The game begins")

round = 1
game = BlackJack()

while True:
    game.players_cards.clear()
    game.dealers_cards.clear()
    
    print()
    game.round(round)
    round += 1

    game.player_draws().\
        player_draws()
    game.dealer_draws()
    game.show1()

    if game.players_score == 21:
        game.blackjack()

    while game.players_score < 21:
        print()
        hit = input("You wanna hit or stay?: ")
        if hit.upper() == "HIT" or hit.upper() == "H":
            game.player_draws()
            while game.players_score < 21:
                game.show1()
                break
            pass
        elif hit.upper() == "STAY" or hit.upper() == "S":
            break
        else:
            pass

    while game.dealers_score < 17:
        game.dealer_draws()

    game.show2()

    if game.players_score > 21 or game.players_score < game.dealers_score <= 21:
        game.lose()
    elif game.dealers_score < game.players_score <= 21 or game.dealers_score > 21:
        game.win()
    else:
        game.draw()

    while True:
        print()
        new_round = input("Another round?: ")
        if new_round.upper() == "YES" or new_round.upper() == "Y":
            break
        elif new_round.upper() == "NO" or new_round.upper() == "N":
            print(f"You stop playing with ${game.money} in your pocket")
            sys.exit()
        else:
            pass
