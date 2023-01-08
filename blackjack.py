from deck import Deck
from hand import Hand
from logo import Logo


# functions

def hit(deck, hand):
    hand.add_card(deck.draw_card())
    hand.adjust_for_aces()


# 6. Reveal Dealer's first card to the Player.
def show_someCard(dealer, player):
    print("\n Dealer's Hand:")
    print(" [<Hidden Card>]")
    print("", dealer.cards[1])
    print("\n Player's Hand: ", *player.cards, sep="\n")


# display all card after the Player declare STAND
def show_allCard(dealer, player):
    print("\nDealer's Hand:", *dealer.cards, sep='\n')
    print("Dealer's Final Score: ", dealer.value)
    print("\nPlayer's Hand: ", *player.cards, sep='\n')
    print("Player's Final Score: ", player.value)


# GamePlay

# 4. Calculate the Player's and Dealer's scores based on their card values.
# 5. If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1 instead.
def calculate_score(cardValues, hand):
    # 2. Detect when Dealer or Player has a blackjack. (Ace + 10 value card).
    if cardValues == 21 and len(hand) == 2:
        return 0
    if "A" in [hand] and cardValues > 21:
        hand.adjust_for_aces()
    return cardValues


def compare(playerScore, dealerScore):
    if playerScore > 21 and dealerScore > 21:
        return "Player went over. Player lose 😣 "

    if playerScore == dealerScore:
        return "Draw 😐"
    elif dealerScore == 0:
        return "Dealer has the BlackJack 🙄"
    elif playerScore == 0:
        return "Player has the BlackJack 🤩"
    elif playerScore > 21:
        return "Player Busted 😕"
    elif dealerScore > 21:
        return "Dealer went over. Player has the Blackjack 🤩"
    elif playerScore > dealerScore:
        return "Player wins!! BlackJack 🤩"
    else:
        return "Player lose 😕😕"


def play_game():
    deck_1 = Deck()
    deck_1.shuffle()
    is_game_over = False

    # 1. Deal both Player and Dealer a starting hand of 2 random card values.
    player_hand = Hand()
    for _ in range(2):
        player_hand.add_card(deck_1.draw_card())

    dealer_hand = Hand()
    for _ in range(2):
        dealer_hand.add_card(deck_1.draw_card())

    show_someCard(dealer_hand, player_hand)

    while not is_game_over:
        dealer_score = calculate_score(dealer_hand.value, dealer_hand.cards)
        player_score = calculate_score(player_hand.value, player_hand.cards)
        # print("dealer hidden card value: ", dealer_hand.list_of_card_values)
        print(f"dealer's current score : {dealer_hand.list_of_card_values[1]}")
        print(F"Player's current score : {player_score}")

        # 3. If Dealer gets blackjack (score = 0), then the Player loses (even if the Player also has a blackjack).
        #    If the Player gets a blackjack, then they win (unless the Dealer also has a blackjack).
        if player_score == 0 or dealer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            # 8. Ask the Player if they want to get another card.
            should_player_deal = input("Type 'h' to HIT another card, type 's' to STAND: ")
            if should_player_deal.lower() == 'h':
                hit(deck_1, player_hand)
                show_someCard(dealer_hand, player_hand)
            else:
                is_game_over = True

    while dealer_score != 0 and dealer_score < 17:
        hit(deck_1, dealer_hand)
        dealer_score = calculate_score(dealer_hand.value, dealer_hand.cards)
    # 9. Show all cards in both sides when Dealer total score over 17
    show_allCard(dealer_hand, player_hand)
    # 10. Compare Player and Dealer scores and see if it's a win, loss, or draw.
    print(compare(player_score, dealer_score))

# ****************Start the Game by "python blackjack.py" ****************
def play():
    print(Logo)
    should_play_again = True
    while should_play_again:
        should_play = input("Do you want to play a game of BlackJack? Type 'y' for Yes or 'n for No : ")
        if should_play not in ['y', 'n']:
            raise Exception("Please type y for YES or n for NO only..no other letter!!")
        if should_play.lower() == 'y':
            play_game()
        elif should_play.lower() == 'n':
            should_play_again = False
            print("The End Game!!")
        else:
            break


if __name__ == '__main__':
    play()
