#Monte Carlo simulation of roulette wheel

from numpy import random
from matplotlib import pyplot as plt


#Part 1.  Outside bets, 5$ bets on red.
#Roulette spins, bet on red, 90 spins a night for a whole year.
land_on_red = list(random.binomial(n=90, p = 18/38, size = 365))

#Gains and losses for each night playing roulette, betting on red.
gains_losses = []

#Calculate the gains/losses for each night of 90 wheel spins.
#Bet $5 on each wheel spin.
for sample in land_on_red:
    winnings_or_losses_per_night = 5*sample -5*(90-sample)
    gains_losses.append(winnings_or_losses_per_night)

#Histogram of nightly wins/losses for the year.
plt.figure()
plt.hist(gains_losses, bins = 8)
plt.title('Histogram of Nightly Wins/Losses for 1 Year: Betting on Red in Roulette')
plt.xlabel('Nightly Winnings/Losses($)')
plt.ylabel('Counts of Winnings/Losses')


#Part 2, Inside bet, 5$ bet on one number (35x payout).
bet_size = 5
winnings_losses = 0
bets_per_night = 90
count_bets = 0
count_days = 0
winnings_losses_list = []

#Simulate betting on a number and then spinning the wheel for that number.
#90 bets per night for a whole year.
while count_days < 365:
    while count_bets < bets_per_night:
        land_on_number = random.randint(1, 38)
        bet_number = random.randint(1, 38)
        if land_on_number == bet_number:
            winnings_losses = winnings_losses + bet_size*35
        else:
            winnings_losses = winnings_losses - bet_size
        count_bets += 1
    winnings_losses_list.append(winnings_losses)
    count_bets = 0
    winnings_losses = 0
    count_days += 1

plt.figure()    
plt.hist(winnings_losses_list, bins = 8)
plt.title('Histogram of Nightly Wins/Losses for 1 Year: Betting on a Number in Roulette')
plt.xlabel('Nightly Winnings/Losses($)')
plt.ylabel('Counts of Winnings/Losses')

plt.show()     

