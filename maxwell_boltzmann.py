#Maxwell-Boltzmann distribution for nitrogen gas
#molecule speeds at 30 degrees Celsius.

#Import libraries
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np
import math

#Nitrogen gas steps to calculate scale factor a.
#Boltzmann constant
k = 1.381e-23

#Gas temperature in Kelvins.
T = 303.15

#Mass of nitrogen molecule in kg.
m = 4.65e-26

#Calculate Maxwell-Boltzmann scaling constant for PDF.
a = math.sqrt(k*T/m)

#Bring in Maxwell methods from scipy library.
maxwell = stats.maxwell

#Generate some random smaples of gas speeds from distribution.
gas_data = maxwell.rvs(loc=0, scale = a, size = 50000)

#Mean and variance of gas molecule speed.
mean_speed, var_speed = maxwell.stats(moments='mv', loc=0, scale=a)
print("Mean gas speed (m/s): ", mean_speed)
print("Gas speed standard deviation (m/s): ", math.sqrt(var_speed))

#Plot histogram of nitrogen molecule speed samples with
#theoretical distribution.
plt.hist(gas_data, bins=20, density=True, edgecolor='black')
x = np.linspace(0, 1400, 100)
plt.plot(x, maxwell.pdf(x, loc=0, scale=a), lw=3)
plt.title("Maxwell-Boltzmann Distribution of $N_2$ Gas at $30^\circ$C")
plt.xlabel("Molecule Speed (m/s)")
plt.ylabel("Probability Density (s/m)")
plt.tight_layout()
plt.show()

