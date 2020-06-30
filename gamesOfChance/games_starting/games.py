import random

money = 100

#Write your game of chance functions here

def flip_coin(bet, rigged = 0):
    global money #enables changing "money" within function
    if bet > money:
        raise Exception("You don't have that much money!")
    call = input("\nHeads or Tails? \n").capitalize()
    result = random.choice(("heads", "tails")) #coinflip

    if rigged == 1234 and (call == "Heads" or call == "Tails"): #password in second parameter to win
        money += bet
        print("\nYour call: " + call)
        print("Coinflip result: " + call)
        print(f"\nCongratulations! You win ${bet}!\n")
        return bet

    if call.lower() == result: #winning scenario
        money += bet
        print("\nYour call: " + call)
        print("Coinflip result: " + result.capitalize())
        print(f"\nCongratulations! You win ${bet}!\n")
        return bet
    else: #losing scenario
        money -= bet
        print("\nYour call: " + call)
        print("Coinflip result: " + result.capitalize())
        print(f"\nOh no! you lost ${bet}!\n")
        return -bet

def cho_han(bet):
    global money
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    eyesum = die1 + die2
    
    call = input("\nOdd or even? \n").capitalize()
    
    result = ""
    if eyesum % 2 == 0:
        result = "Even"
    else:
        result = "Odd"
    
    if result == call:
        money += bet
        print("\nYour call: " + call)
        print("Sum of the eyes: " + str(eyesum))
        print(f"\nCongratulations! You win ${bet}!\n")
        return bet
    else:
        money -= bet
        print("\nYour call: " + call)
        print("Sum of the eyes: " + str(eyesum))
        print(f"\nOh no! you lost ${bet}!\n")
        return -bet

#function to spit out names for special cards, returns card number as string otherwise. 
def card_name(card): #input int in range(13)
    if card == 1: #
        return "Ace", 1
    if card == 11:
        return "Jack", 11
    if card == 12:
        return "Queen", 12
    if card == 13 or card == 0: #because of %, 13 shouldn't be input in the first place
        return "King", 13
    return str(card), card

#returns a suit for a given card.
def card_suit(card): #input float in range(4)
    if card <= 1:
        return "Clubs"
    if card <= 2:
        return "Spades"
    if card <= 3:
        return "Hearts"
    if card <= 4:
        return "Diamonds"

def card_draw(deck): #input a deck (list) to draw from
    cardindex = random.choice(deck) #picks a card from deck and pops it from deck
    deck.pop(cardindex - 1)
    name, card = card_name(cardindex % 13)
    suit = card_suit(cardindex / 13)

    return card, name, suit



def draw_a_card(bet):
    global money
    deck = [i + 1 for i in range(52)] #full deck o' cards
    first = random.randint(0, 1)

    card1, card1name, card1suit = card_draw(deck)

    card2, card2name, card2suit = card_draw(deck)


    if first == 0:
        print("\nYour opponent goes first!\n")
        print(f"Opponent's draw: {card1name} of {card1suit}")
        print(f"Your draw: {card2name} of {card2suit}")
        if card1 > card2:
            money -= bet
            print(f"\nOh no! you lost ${bet}!\n")
            return -bet
        if card2 > card1:
            money += bet
            print(f"\nCongratulations! You win ${bet}!\n")
            return bet
        print("\nIt's a tie! You recover your bets!\n")
        return 0

    if first == 1:
        print("\nYou go first!\n")
        print(f"Your draw: {card1name} of {card1suit}")
        print(f"Opponent's draw: {card2name} of {card2suit}")
        if card1 < card2:
            money -= bet
            print(f"\nOh no! you lost ${bet}!\n")
            return -bet
        if card2 < card1:
            money += bet
            print(f"\nCongratulations! You win ${bet}!\n")
            return bet
        print("\nIt's a tie! You recover your bets!\n")
        return 0

def roulette(bet):
    global money
    call = input("\nMake your call: \n")
    result = str(random.choice(range(38)))
    if result == "37":
        result = "00"
    
    print("\nSpinning wheel...")
    print("Result: " + str(result))
    
    if call.lower() == "even":
        if int(result) % 2 == 0:
            money += bet
            print(f"\nCongratulations! You won ${bet}!\n")
            return bet
        money -= bet
        print(f"\nOh no! You lost ${bet}!\n")
        return -bet
    elif call.lower() == "odd":
        if int(result) % 2 == 1:
            money += bet
            print(f"\nCongratulations! You won ${bet}!\n")
            return bet
        money -= bet
        print(f"\nOh no! You lost ${bet}!\n")
        return -bet
    
    if str(result) == call:
        money += bet * 35
        print(f"\nIncredible! You won ${bet * 35}!\n")
        return bet * 35
    
    money -= bet
    print(f"\nYou guessed wrong and lost ${bet}...\n")
    return -bet


#Call your game of chance functions here

print(f" Your money: {money + flip_coin(101)}\n")
print(f" Your money: {money + cho_han(10)}\n")
print(f" Your money: {money + draw_a_card(10)}\n")
print(f" Your money: {money + roulette(10)}\n")