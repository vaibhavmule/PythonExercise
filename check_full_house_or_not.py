
def is_full_house(list_of_cards):
    unique_cards = set(list_of_cards)
    if len(unique_cards) == 2:
        first_card, second_card = unique_cards
        first_counter = list_of_cards.count(first_card)
        second_counter = list_of_cards.count(second_card)
        first_condition = first_counter == 2 and second_counter == 3
        second_condition = first_counter == 3 and second_counter == 2
        if first_condition or second_condition:
            return True
    return False


print(is_full_house([1, 2, 1, 2, 1]))
