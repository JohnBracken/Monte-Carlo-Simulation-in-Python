#The following code is a code sample that demonstrates a Monte Carlo simulation.
#The code highlights the classic example of estimating the value of pi by comparing
#the number of events that happen within a square to the number of events within a circle
#contained in the square and also bounded by the square.  The trial demonstrated by
#the figure gave an estimate of pi = 3.12.  This pi estimate will fluctuate a bit with each trial run.




#Numeric Python library for random number generation.
import numpy as np

#Import the plotting tools from matplotlib
from matplotlib import pyplot as plt




#Number of random point samples to be pulled from the uniform distribution.
sample_size = 400



#X axis and corresponding y-axis values for multiple samples pulled
#from a continuous uniform distribution between 0 and 1.
x_axis = np.random.random_sample(sample_size)
y_axis = np.random.random_sample(sample_size)



#Location of the center and radius of the circle.
xc,yc = 0.5, 0.5
r = 0.5



#Calculate the distance squared of each randomly generated point from the center of the circle.
d_squared = (x_axis - xc)**2 + (y_axis - yc)**2



#Find the indices of the randomly generated points that fall within or on the circle.
points_in_circle = np.where(d_squared <= r**2)



#Convert the indices tuple to a 1D array of data.
points_in_circle =np.array(points_in_circle)



#Calculate the number of points that fall in or on the circle contained within a square.
number_circle_points = (points_in_circle.size)



#State the number of points contained in the entire bounding square.
number_square_points = sample_size



#Calculate an estimate of pi by using the ratio of circle points to square points.  This is equivalent to
#taking an estimate of the ratio of the circle area to the square area.  The result should
#be fairly close to pi/4.  So the ratio is multiplied by 4 to get this estimate.
pi_estimate = (number_circle_points/number_square_points)*4



#Set up a figure to display the Monte Carlo simulation
fig = plt.figure()



#The figure will include a circle, so set up a subplot to overlay the circle on the screen.
ax = fig.add_subplot(1, 1, 1)



#Plot the random events landing in the square as plus signs showning there location.
#Label the axes as x and y.
plt.plot(x_axis,y_axis, '+')
plt.xlabel('x'), plt.ylabel('y')



#Set the axis limits to between 0 and 1.
plt.axis([0,1,0,1])



#Set the axes to be equal length and shown in box format using 'Get Current Axes' (gca).
plt.gca().set_aspect('equal', adjustable='box')



#Draw the new axes on the plot.
plt.draw()



#Create a circle centered at x,y = (0.5,0.5), with a radius of 0.5.  Make the circle edge
#black and make sure the circle is unfilled.
circ = plt.Circle((xc,yc), r, color='k', fill=False)



#Add the circle to the plot
ax.add_patch(circ)



#Show the plot.
plt.show()



#Print the estimate of pi determined from this simulation.
print(pi_estimate)




