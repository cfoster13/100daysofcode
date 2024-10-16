bidder = {
    "name": [],
    "bid_amount": [],
}

continue_asking = True

while continue_asking:
    new_name = input("What is your name? ")
    bidder["name"].append(new_name)
    new_bid_amount = int(input("What is your bid amount? "))
    bidder["bid_amount"].append(new_bid_amount)
    new_bidder = input("Are there any other bidders? y/n").lower()
    #Clear the terminal
    print("\n" * 100)

    if new_bidder == "n":
        continue_asking = False

#Loop through dictionary to find the highest bidder
max_bid = 0
winner = ""

for bids in range(len(bidder["bid_amount"])):
    if bidder["bid_amount"][bids] > max_bid:
        max_bid = bidder["bid_amount"][bids]
        winner = bidder["name"][bids]


print(f"The winner is {winner} with a bid of {max_bid}")