#Stock price simulation.  Wiener process with drift.  
#S_(t + delta_t) = S_t(1 + (mu*delta_t + sigma*epsilon*sqrt(delta_t)))

# mu is stocks risk-netural expected return rate, continuous compounding
# sigma is stock volatility
# epsilon is random number from standard normal distribution.

#Generate large number of random numbers epsilon.  For each of these,
#calculate S_(t + delta_t).  Average result to get estimate for risk-neutral
#value of share price at t + delta_t.  Standard deviation for confidence interval.

# mu = 0.20 per year
# sigma = 0.25 per year
# delta_t = 0.01 years (3.65 days)

#Can calculate mean and confidence interval by running simulation for each time 
#interval

import numpy as np
import math
import statistics
from matplotlib import pyplot as plt

mu = -0.07
sigma = 0.3
delta_t = 0.002737851

mean_stock_prices = []
std_stock_prices = []
stock_price_init = 34.57
mean_stock_prices.append(stock_price_init)
std_stock_prices.append(0)
stock_price_current = stock_price_init

for j in range(1, 365):
    epsilons = np.random.standard_normal(1000)
    stock_price_next_array = np.array([])

    for i in range(len(epsilons)):
        stock_price_next = stock_price_current*(1 + (mu*delta_t + sigma*epsilons[i]*(math.sqrt(delta_t)))) 
        stock_price_next_array = np.append(stock_price_next_array, stock_price_next)

    stock_price_avg = np.mean(stock_price_next_array)
    stock_price_std = np.std(stock_price_next_array)

    mean_stock_prices.append(stock_price_avg)
    std_stock_prices.append(stock_price_std)

    stock_price_current = stock_price_avg

plt.plot(mean_stock_prices, color='magenta') 
plt.xticks(range(0,len(mean_stock_prices)+1, 30)) 

plt.ylabel('Stock Price ($)') 
plt.xlabel('Day') 
plt.title("Stock Price over a year") 
plt.show() 
