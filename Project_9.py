from replit import clear
from art import logo
print(logo)

bids = {}
bidder_is_present = True

while bidder_is_present:
    name = input('What is your name? : ')
    price = int(input('What\'s your bid? : $ '))
    bids[name] = price
    any_other_bidders = input('Are there any other bidders? Type \'yes\' or \'no\'.\n').lower()
    if any_other_bidders == 'yes':
        clear()
    else:
        bidder_is_present = False
        clear()

winner = max(bids, key=bids.get)
max_bid = (max(bids.values()))
print(f'The final winner is {winner} with a bid of ${max_bid}.')