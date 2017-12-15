def sort_cards(cards):
    output = []
    for card in cards:
        if card.isdigit():
            output.append(card)
    output = sorted(output)
    for card in cards:
        if card == 'A':
            output.insert(0, 'A')
    for card in cards:
        if card == 'T':
            output.append('T')
    for card in cards:
        if card == 'J':
            output.append('J')
    for card in cards:
        if card == 'Q':
            output.append('Q')
    for card in cards:
        if card == 'K':
            output.append('K')
    return output
