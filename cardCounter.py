import math

def get_card_value(card):
    if card in ['A', 'K', 'Q', 'J', '10']:
        return -1
    elif card in ['9', '8', '7']:
        return 0
    else:
        return 1

def calculate_bet_size(original_bet_size, true_count):
    if true_count >= 0:
        # Adjust these parameters to fit the exact scaling curve you want
        scale_factor = math.pow(1.5, true_count)
        return original_bet_size * scale_factor
    else:
        scale_down_factor = 1 / (1 + 0.5 * abs(true_count))
        return original_bet_size * scale_down_factor


def main():
    bet_size = int(input("Enter bet size: "))
    number_of_decks = int(input("Enter number of decks: "))
    total_cards = number_of_decks * 52
    cards_dealt = 0
    running_count = 0
    original_bet_size = bet_size

    print("Okay!\nStarting card counting")

    while True:
        cards_input = input("Enter each card with a space in between, EG. K Q 7 6 2 (or type 'exit' to stop): ")
        if cards_input.lower() == 'exit':
            break

        cards = cards_input.upper().split()
        for card in cards:
            cards_dealt += 1
            running_count += get_card_value(card)

        decks_remaining = (total_cards - cards_dealt) / 52
        true_count = running_count / max(1, decks_remaining) 

        bet_size = round(calculate_bet_size(original_bet_size, true_count))

        print(f"Total Cards Dealt: {cards_dealt}")
        print(f"Total Decks Remaining: {decks_remaining:.2f}")
        print(f"True Count: {true_count:.2f}")
        print(f"Bet Size: {bet_size:.2f}")

main()
