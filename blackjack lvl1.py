import random

cards = [2,3,4,5,6,7,8,9,10,'k','q','j','a']

def score(hand):
    # print(hand)
    point = 0
    for card in hand:
        if card == 'k' or card == 'q' or card == 'j':
            point += 10
        elif card != 'a':
            point += card
    if hand.count('a'):
        if point + 11 <= 21:
            point += 11
        else:
            point += 1
    return point
def game():
    print("""WELCOME TO BLACKJACK GAME""")
    your_hand = random.choices(cards,k=2)
    dealer_hand = [random.choice(cards)]
    your_score = score(your_hand)
    dealer_score = score(dealer_hand)
    print(f"Your score is {your_score} and dealer score is {dealer_score}")
    choice = int(input("Enter 1 for picking more card\nEnter 2 for end your turn\n"))
    defeat = 0
    win = 0
    while defeat == 0 and win == 0:
        while choice == 1:
            temp = [random.choice(cards)]
            # print(f"user{temp}")
            if temp[0] == 'a':
                if your_score + 11 <= 21:
                    your_score += 11
                else:
                    your_score += 1
            else:
                your_score += score(temp)
            if your_score > 21:
                defeat = 1
                break
            elif your_score == 21:
                win = 1
            print(f"Your score is {your_score} and dealer score is {dealer_score}")
            choice = int(input("Enter 1 for picking more card\nEnter 2 for end your turn\n"))
        else:
            while dealer_score < 17:
                temp = [random.choice(cards)]
                # print(f"dealer{temp}")
                if temp[0] == 'a':
                    if dealer_score + 11 <= 21:
                        dealer_score += 11
                    else:
                        dealer_score += 1
                else:
                    dealer_score += score(temp)
                if dealer_score > 21:
                    win = 1
                    break
                print(f"Your score is {your_score} and dealer score is {dealer_score}")
            break
    if defeat:
        print("bust")
    elif win:
        print("you won")
    else:
        if 21-your_score < 21-dealer_score:
            print("win")
        elif 21-your_score == 21-dealer_score:
            print("draw")
        else:
            print("defeat")



game()
need = int(input("press 1 to play again\nPress 2 to exit the game\n"))
if need == 1:
    game()



