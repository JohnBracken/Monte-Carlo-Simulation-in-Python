#Monte Carlo coin toss.

import numpy
import random


count = 0
head_count = 0
tail_count = 0

while count < 10000000:
    coin_toss = random.randint(0,1)
    if coin_toss == 0:
        head_count += 1
    else:
        tail_count += 1

    count += 1

p_heads = head_count/count
p_tails = tail_count/count

#Probabilities should be close to 50% for either heads or tails.
print("Ptails", p_tails)
print("Pheads", p_heads)
