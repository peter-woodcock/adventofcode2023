import re
from collections import defaultdict

running_total = 0
count_of_cards = defaultdict(int)

with open("input.txt") as f:
    for line in f:
        card_id = int(re.search("([0-9]+):", line).group(1))
        winning_numbers = list(filter(None, re.search(": (.*) \|", line).group(1).split(' ')))
        ticket_numbers = list(filter(None, re.search("\| (.*)", line).group(1).split(' ')))

        count_of_cards[card_id] += 1

        matching_numbers = set(winning_numbers) & set(ticket_numbers)
        if matching_numbers:
            for i in range(1, len(matching_numbers) + 1):
                count_of_cards[card_id + i] += count_of_cards[card_id]

print(sum(count_of_cards.values()))
