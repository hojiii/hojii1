from replit import clear
from art import logo
print(logo)
bids ={}
bids_finished = False
def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner=""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount>highest_bid:
      highest_bid = bid_amount
      winner=bidder
  print(f"The winner is {winner},price is {highest_bid}")
while not bids_finished:
  name = input("What is your name?: ")
  price = int(input("How much bid price?: "))
  bids[name]=price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bids_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()
  
