#Monte Carlo simulation of 20 keV and 200 keV X-ray
#photon transport in an infinite slab of Lucite
#(ignore reflectance at lucite boundaries).


import numpy as np
import math
from matplotlib import pyplot as plt
import mpl_toolkits

#Attenuation, scattering and absorption coefficients
#given in units of cm^-1 for 20 keV photons in Lucite.
ut = 0.632
u_ab = 0.35
u_sc = 0.282


#Attenuation, scattering and absorption coefficients
#given in units of cm^-1 for 200 keV photons in Lucite.
ut = 0.157
u_ab = 0.0339
u_sc = 0.1231

#Anistropy estimate of 200 keV (just a guess).
#Scattering should be more forward directed than
#for 20 keV.
g = 0.4

#Number of photons
N = 30

photons = []

for k in range(N):
    #Lists of positions and direction cosines for a photon.
    positions = []
    dir_cosines = []


    #Part 1: Launch photon packet.
    #Position and direction cosines initialized
    x = 0
    y = 0
    z = 0

    ux = 0 
    uy = 0
    uz = 1

    pos = [x, y, z]
    dir_cos = [ux, uy, uz]

    positions.append(pos)
    dir_cosines.append(dir_cos)

    #Initial photon packet weight and threshold weight for cutoff.
    W = 1
    m = 10
    Wt = 0.00001

    weights = []
    weights.append(W)

    while W != 0:
        while W >= Wt:
            #Part 2:  Move photon by step size.
            epsilon = np.random.uniform(0, 1)
            step_size = -(np.log(epsilon))/ut

            x = x + ux*step_size
            y = y + uy*step_size
            z = z + uz*step_size

            pos = [x, y, z]

            #Part 3: Absorption

            #Photon packet weight loss absorbed.
            delta_w = (u_ab/ut)*W
            W = W - delta_w

            #Part 4: Scattering, assume isotropic for 20 keV
            epsilon = np.random.uniform(0, 1)
            scatter_angle = math.acos(1 - 2*epsilon) 
           
            #Scatter angle for anisotropic 200 keV photons 
            epsilon = np.random.uniform(0, 1)
            aniso = (1/(2*g))*(1 + g*g - ((1 - g*g)/(1 - g + 2*g*epsilon))**2)
            scatter_angle = math.acos(aniso)
 
            epsilon = np.random.uniform(0, 1)
            polar_angle = 2*math.pi*epsilon

            if uz == 1:
                ux_p = (math.sin(scatter_angle))*(math.cos(polar_angle))
                uy_p = (math.sin(scatter_angle))*(math.sin(polar_angle))
                uz_p = math.cos(scatter_angle)
            elif uz == -1:
                ux_p = (math.sin(scatter_angle))*(math.cos(polar_angle))
                uy_p = -(math.sin(scatter_angle))*(math.sin(polar_angle))
                uz_p = -math.cos(scatter_angle)
            else:
                denom = math.sqrt(1 - uz*uz)
                ux_p = (math.sin(scatter_angle)*(ux*uz*math.cos(polar_angle) - uy*math.sin(polar_angle)))/denom + ux*math.cos(scatter_angle)
                uy_p = (math.sin(scatter_angle)*(uy*uz*math.cos(polar_angle) + ux*math.sin(polar_angle)))/denom + uy*math.cos(scatter_angle)
                uz_p = -denom*math.sin(scatter_angle)*math.cos(polar_angle) + uz*math.cos(scatter_angle)

            ux = ux_p
            uy = uy_p
            uz = uz_p

            dir_cos = [ux, uy, uz]

            positions.append(pos)
            dir_cosines.append(dir_cos)
            weights.append(W)

        epsilon_roulette = np.random.uniform(0,1)
        if epsilon_roulette <= 1/m:
            W = m*W
            weights.append(W)
        else:
            W = 0
            weights.append(W)

    x_plot = []
    y_plot = []
    z_plot = []

    for pos in positions:
        x_plot.append(pos[0])
        y_plot.append(pos[1])
        z_plot.append(pos[2])

    keys = ["photon_num", "positions", "x_plot", "y_plot", "z_plot" ]
    photon_object = dict.fromkeys(keys)
    photon_object["photon_num"] = k
    photon_object["positions"] = positions
    photon_object["x_plot"] = x_plot  
    photon_object["y_plot"] = y_plot  
    photon_object["z_plot"] = z_plot  
    photons.append(photon_object)

#2D plot in X-Y plane
plt.xlabel("X Position (cm)")
plt.title("200 keV X-ray Photon Transport in Lucite")
plt.ylabel("Y Position (cm)")
for j in range(len(photons)): 
    plt.plot(photons[j]["x_plot"], photons[j]["y_plot"], '.r-')
plt.show()


#3D plot of photon transport
fig = plt.figure()
ax = plt.axes(projection ="3d")
plt.title("200 keV X-ray Photon Transport in Lucite")
ax.set_xlabel('X Position (cm)', fontweight ='bold')
ax.set_ylabel('Y Position (cm)', fontweight ='bold')
ax.set_zlabel('Z Position (cm)', fontweight ='bold')


for j in range(len(photons)):
    ax.scatter3D(photons[j]['x_plot'], photons[j]['y_plot'], photons[j]['z_plot'], c = 'red', s = 5)
    ax.plot(photons[j]['x_plot'], photons[j]['y_plot'], photons[j]['z_plot'], color = 'red')

plt.show()
