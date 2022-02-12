from replit import clear
from art import logo
print(logo)
print("Welcome to the Secret Auction Program.")
bidding_Finished=False
bids={}

#function to find the highest bidder from a dictionary
def find_highest_bidder(bid_record):
  highest_bidder=""
  highest_bid=0
  for bidder in bid_record:
    if(bid_record[bidder]>highest_bid):
      highest_bid=bid_record[bidder]
      highest_bidder=bidder
  print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")
 
while not bidding_Finished:
  name=input("What is your name?\n")
  price=int(input("What is your bid? $"))
  bids[name]=price
  should_continue=input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
  #when no other bidders are present, call fn to find highest bidder, display and exit.
  if should_continue=="no":
    bidding_Finished=True
    find_highest_bidder(bids)
  elif should_continue=="yes":
   clear()
  

