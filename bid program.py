
import os
print('Welcome to the Auction')
another_bid='yes'

bids={}

while another_bid=='yes':
    bidder_name=input("Enter your name: ")

    bid_price=float(input('Enter the amount of the bid: '))

    bids[bidder_name]=bid_price

    another_bid=input('Are the other users who want to bid? (enter yes or no)').lower()
    if another_bid=='yes':
      os.system('cls')
maxvalue=max(bids.values())
max_bidder=[key for key, value in bids.items() if value==maxvalue]
print(f'Here is the max bidder {max_bidder}')
winner=' '.join (max_bidder)
print(f'Thanks for submitting all bids, the winner for this bid is {winner}')