"""
-------------------------
    Advent of Code 2023
    Alireza Bolourian
    Challenge 7 of 25
      Part 2 of 2
-------------------------
"""

real_data = True

example = ["32T3K 765",
            "T55J5 684",
            "KK677 28",
            "KTJJT 220",
            "QQQJA 483"]

rank = {
    "A":14,
    "K":13,
    "Q":12,
    "J":1,
    "T":10,
    "9":9,
    "8":8,
    "7":7,
    "6":6,
    "5":5,
    "4":4,
    "3":3,
    "2":2
}

with open("Day7/day_7_input.txt", "r", encoding="utf-8") as file:
    data = [line.strip() for line in file.readlines()]

if real_data:
    lines = data
else:
    lines = example

#print(lines)

def sort_rank(hands):
    five_of_kind = []
    four_of_kind = []
    full_house = []
    three_of_kind = []
    two_pair = []
    one_pair = []
    high_card = []
    for hand in hands:
        cards = hand.split()[0]
        repeated_cards = []
        num_labels = 1
        for i, card in enumerate(cards):
            if card not in repeated_cards and card != "J":
                for j in range(i+1, len(cards)):
                    if card == cards[j]:
                        num_labels += 1
                        if card not in repeated_cards:
                            repeated_cards.append(card)
            elif card == "J":
                num_labels += 1
        # to account for all Joker hand
        if num_labels == 5 or cards[0]==cards[1]==cards[2]==cards[3]==cards[4]:
            five_of_kind.append(hand)
        if num_labels == 4 and len(repeated_cards) != 2:
            four_of_kind.append(hand)
        if num_labels == 4 and len(repeated_cards) == 2:
            full_house.append(hand)
        if num_labels == 3 and len(repeated_cards) != 2:
            three_of_kind.append(hand)
        if num_labels == 3 and len(repeated_cards) == 2:
            two_pair.append(hand)
        if num_labels == 2:
            one_pair.append(hand)
        if num_labels == 1:
            high_card.append(hand)
        #print(repeated_cards)
    return five_of_kind, four_of_kind, full_house, three_of_kind, two_pair, one_pair, high_card

#Bubble Sort
def sort_strength(hands):
    sorted = False
    for i in range(len(hands)):
        if not sorted:
            sorted = True
            for j in range(len(hands)-i-1):
                cards_1 = hands[j].split()[0]
                cards_2 = hands[j+1].split()[0]
                for k in range(5):
                    if rank.get(cards_1[k]) == rank.get(cards_2[k]):
                        continue
                    if rank.get(cards_1[k]) > rank.get(cards_2[k]):
                        temp = hands[j]
                        hands[j] = hands[j+1]
                        hands[j+1] = temp
                        sorted = False
                    break
    return hands

five_of_kind, four_of_kind, full_house, three_of_kind, two_pair, one_pair, high_card = sort_rank(lines)

five_of_kind = sort_strength(five_of_kind)
four_of_kind = sort_strength(four_of_kind)
full_house = sort_strength(full_house)
three_of_kind = sort_strength(three_of_kind)
two_pair = sort_strength(two_pair)
one_pair = sort_strength(one_pair)
#print(high_card)
high_card = sort_strength(high_card)

#print(high_card)

sorted_hands = high_card + one_pair + two_pair + three_of_kind + full_house + four_of_kind + five_of_kind

def calculate_total_winnings(hands_sorted):
    total_winings = 0
    for i, hand in enumerate(hands_sorted):
        bid = int(hand.split()[1])
        total_winings += bid*(i+1)
    return total_winings

result = calculate_total_winnings(sorted_hands)
print(result)
