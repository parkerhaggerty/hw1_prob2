# Author: Parker Haggerty
# Date: 1/27/17
# Assignment 1, Problem 2

from math import pi
G = 6.67*(10**-11)              #Gravitational constant
M = 5.97*(10**24)               #Mass of earth
R = 6371*1000                   #Radius of earth (meters)


T = float(input("Enter a time (in seconds):"))      #Time
h = ((G*M*(T**2))/(4*(pi**2)))**(1.0/3)-R           #Altitude (meters)

print("The altitude is", h)



#For T=86400 (aka: one day); h= 35855910.17617497 meters
#For T=5400 (aka: 90 min); h= 279321.62537285965 meters
#For T=2700 (aka: 45 min); h= -2181559.8978108233 meters
#For T=86148 (aka: 1 siddereal day); h= 35773762.329895645 meters
#The altitude difference between a 24hr day and a siddereal day is about 82,147 meters