import random

def create_deck():
    deck = [str(num) for num in range(2, 11)] + ['J', 'Q', 'K', 'A']
    random.shuffle(deck)
    return deck

def get_card_value(card):
    if card in ['K', 'Q', 'J']:
        return 10
    elif card == 'A':
        return 11
    else:
        return int(card)

def play_game():
    deck = create_deck()
    player_hand = []
    dealer_hand = []

    for _ in range(2):
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())

    player_score = sum(get_card_value(card) for card in player_hand)
    dealer_score = sum(get_card_value(card) for card in dealer_hand)

    print(f"Jouw kaarten: {player_hand}, huidige score: {player_score}")
    print(f"Dealer kaart: {dealer_hand[0]}")

    if player_score == 21:
        print("Gefeliciteerd! Je hebt Blackjack!")
        return
    elif dealer_score == 21:
        print("Dealer heeft Blackjack. Je verliest!")
        return

    while player_score < 21:
        should_continue = input("Typ 'h' om een kaart te nemen, typ 's' om te stoppen: ").lower()
        if should_continue == 'h':
            player_hand.append(deck.pop())
            player_score = sum(get_card_value(card) for card in player_hand)
            print(f"Jouw kaarten: {player_hand}, huidige score: {player_score}")
        else:
            break

    while dealer_score < 17:
        dealer_hand.append(deck.pop())
        dealer_score = sum(get_card_value(card) for card in dealer_hand)

    print(f"\nJouw kaarten: {player_hand}, jouw score: {player_score}")
    print(f"Dealer kaarten: {dealer_hand}, dealer score: {dealer_score}\n")

    if player_score > 21:
        print("Je hebt verloren!")
    elif dealer_score > 21:
        print("Je hebt gewonnen!")
    elif player_score == dealer_score:
        print("Gelijkspel!")
    elif player_score > dealer_score:
        print("Je hebt gewonnen!")
    else:
        print("Je hebt verloren!")

play_game()
