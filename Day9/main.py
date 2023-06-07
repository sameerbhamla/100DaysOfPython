import art

print(art.logo)
bids = {}
bid_is_on = True

while bid_is_on:
    name = input("What is your name?: ")
    bid = input("How much would you like to bid: ")
    bids[name] = bid
    response = input("Are there any other bidders?(Y/N): ")
    if response.upper() == 'Y':
        pass
    else:
        bid_is_on = False

winner_name = ""
winner_bid = -1
for bid in bids:
    if int(bids[bid]) > int(winner_bid):
        winner_bid = bids[bid]
        winner_name = bid

print(f"The winner is {winner_name} with a bid of {winner_bid}")