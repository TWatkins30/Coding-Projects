import numpy as np
from math import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd

hold = []
time = 24

for single_date in pd.date_range('2019-07-29', '2019-07-31'):

	day = int(single_date.strftime("%d"))
	month = int(single_date.strftime("%m"))
	year = int(single_date.strftime("%Y"))
	day_number = 367 * int(year) - 7 * (int(year) + (int(month) + 9) / 12) / 4 + 275 * int(month) / 9 + int(day) - 730530
	day_number = day_number + int(time) /24
	#print(f"{day_number}\n")
	hold.append(day_number)
		
def mean_anomaly_adjustment(number):
	if number < 0:
		while number < 0:
			number = number + 360
	return number
def radian_conversion(number):
	number = number * (np.pi/180)
	return number
def degree_conversion(number):
	number = number * (180 / np.pi)
	return number	
def days_to_years(number):
	number = number / 364
	return number
def polar_coordinates_distance(one, two):
	return np.sqrt(one ** 2 + two ** 2)

def ecliptic_obliquity(time_scale):
	obliquity = 23.4393 - 3.63 * np.exp(-7) * int(time_scale)
	return obliquity

class Mercury(): #parent class
	def __init__(self, ecliptic_longitude = 300, ecliptic_latitude = 130):
		self.ecliptic_longitude = ecliptic_longitude
		self.ecliptic_latitude = ecliptic_latitude
		self.perihelion = None
		self.distance = None
		self.eccentricity = None
		self.mean_anomaly = None
		self.r_g = None
		self.geocentric_longitude = None
		self.x = None
		self.y = None
		
	def orbital_elements(self, initial_position, complete_orbit, perihelion, eccentricity, semi_major_axis):
		days = hold
		x = []
		y = []
		for i in days:
			#Heliocentric Orbital Elements
			angular_speed = 360 / complete_orbit 
			mean_traversed_angle = angular_speed * i #Final Position
			
			#Heliocentric Elliptical Elements
			mean_longitude = mean_anomaly_adjustment(mean_traversed_angle + initial_position)
			mean_anomaly = radian_conversion(mean_longitude - perihelion)
		
			precision = degree_conversion(2 * eccentricity * np.sin(mean_anomaly))
			precision += degree_conversion((5/4) *eccentricity ** 2 * np.sin(2 * mean_anomaly))
		
			vernal_equinox = int(round(int(days_to_years(i)) * (360/25800)))
			anomaly = mean_anomaly + precision
			corrected_longitude = mean_longitude + precision + vernal_equinox
			
			#Geocentric Perspective
			distance_from_sun = ((semi_major_axis * (1 - eccentricity ** 2)) 
			/ (1 + eccentricity * np.sin(anomaly)))
			
			r = distance_from_sun #(radii)
			
			#Heliocentric rectangular coordinates of the planet
			X_h = r * np.cos(radian_conversion(corrected_longitude)) #
			Y_h = r * np.sin(radian_conversion(corrected_longitude)) #
			
			#Heliocentric rectangular coordinates of Earth
			X_0 = -0.174 # AU
			Y_0 = 0.968 #AU
		
			#rectangular coordinates of the planet from Earth
			X_g = X_h - X_0
			Y_g = Y_h - Y_0
			#converting the X_g and Y_g into polar coordinates
			self.r_g = polar_coordinates_distance(X_g, Y_g)
			self.geocentric_longitude = mean_anomaly_adjustment(mean_anomaly_adjustment(degrees(atan(Y_g/X_g))))
			#adding the polar coordinates to the list to plot them
			x.append(self.r_g)
			y.append(self.geocentric_longitude)
			
		self.x = x
		self.y = y
		for plot in self.x:
			print(f"{plot} AU")
			
		for yplot in self.y:
			print(f"{yplot} degrees")
			
		return f"{x[0]} AU, {y[0]} degrees"		
	def plotting_coordinates(self):
		return (self.x, self.y)
		
#Child classes		
class Venus(Mercury):
	def __init__(self, ecliptic_longitude = 179, ecliptic_latitude = 46):
		super().__init__(ecliptic_longitude, ecliptic_latitude)

class Earth(Mercury):
	def __init__(self, ecliptic_longitude = 179, ecliptic_latitude = 46):
		super().__init__(ecliptic_longitude, ecliptic_latitude)
		
class Mars(Mercury):
	def __init__(self, ecliptic_longitude = 179, ecliptic_latitude = 46):
		super().__init__(ecliptic_longitude, ecliptic_latitude)
		
class Jupiter(Mercury):
	def __init__(self, ecliptic_longitude = 179, ecliptic_latitude = 46):
		super().__init__(ecliptic_longitude, ecliptic_latitude)
		
class Saturn(Mercury):
	def __init__(self, ecliptic_longitude = 179, ecliptic_latitude = 46):
		super().__init__(ecliptic_longitude, ecliptic_latitude)
		
class Neptune(Mercury):
	def __init__(self, ecliptic_longitude = 179, ecliptic_latitude = 46):
		super().__init__(ecliptic_longitude, ecliptic_latitude)
		
class Uranus(Mercury):
	def __init__(self, ecliptic_longitude = 179, ecliptic_latitude = 46):
		super().__init__(ecliptic_longitude, ecliptic_latitude)
		
class Pluto(Mercury):
	def __init__(self, ecliptic_longitude = 179, ecliptic_latitude = 46):
		super().__init__(ecliptic_longitude, ecliptic_latitude)
		
#Objects		
jupiter = Jupiter()
jupiter_orbitals = jupiter.orbital_elements(30.1, 4332.59, 14.3, 0.0485, 5.20)
jcoordinates = jupiter.plotting_coordinates()
print(f"Jupiter coordinates: {jupiter_orbitals}")		

neptune = Neptune()
neptune_orbitals = neptune.orbital_elements(304.88, 60225, 44.971, 0.008585, 30.1)
ncoordinates = neptune.plotting_coordinates()
print(f"Neptune coordinates: {neptune_orbitals}")
		
mercury = Mercury()
mercury_orbitals = mercury.orbital_elements(250.2, 87.969, 77.5, 0.205635, 0.387)
mcoordinates = mercury.plotting_coordinates()
print(f"Mercury's coordinates: {mercury_orbitals}")

venus = Venus()
venus_orbitals = venus.orbital_elements(181.2, 224.701, 131.6, 0.0068, 0.7233)
vcoordinates = venus.plotting_coordinates()
print(f"Venus' coordinates: {venus_orbitals}")

earth = Earth()
earth_orbitals = earth.orbital_elements(100.2, 365.256, 102.9, 0.0167,1)
ecoordinates = earth.plotting_coordinates()
print(f"Earth's coordinates: {earth_orbitals}")

mars = Mars()
mars_orbitals = mars.orbital_elements(344.6, 686.980, 336.1, 0.0934, 1.52)
marscoordinates = mars.plotting_coordinates()
print(f"Mars coordinates: {mars_orbitals}")

saturn = Saturn()
saturn_orbitals = saturn.orbital_elements(54.6, 10759.2, 93.1, 0.0555, 9.55)
scoordinates = saturn.plotting_coordinates()
print(f"Saturn coordinates: {saturn_orbitals}")

uranus = Uranus()
uranus_orbitals = uranus.orbital_elements(313.23218, 30660, 170.96424, 0.0473, 19.201)
ucoordinates = uranus.plotting_coordinates()
print(f"Uranus coordinates: {uranus_orbitals}")

#Plotting the planets according
earthx = (0,0)
plt.figure()
plt.plot(jcoordinates, ecoordinates, '--o', color = 'purple', label = 'Jupiter')	
plt.plot(ecoordinates, earthx, '--o', color = 'yellow', label = 'Sun')	
plt.plot(ncoordinates, ecoordinates, '--o', color = 'orange', label = 'Neptune')	
plt.plot(marscoordinates, ecoordinates, '--o', color = 'firebrick', label = 'Mars')
plt.plot(scoordinates, ecoordinates, 'o--', color = 'lightyellow', label = 'Saturn')
plt.plot(vcoordinates, ecoordinates, 'o--', color = 'lightblue', label = 'Venus')
plt.plot(mcoordinates, ecoordinates, 'o--', color = 'darkgray', label = 'Mercury')
plt.plot(ucoordinates, ecoordinates, '--o', color = 'turquoise', label = 'Uranus')

plt.yscale('linear')
plt.grid(b=True, which='major', color='b', linestyle='-')
plt.grid(b=True, which='minor', color='r', linestyle='--')
plt.plot(0,0, 'o',color = 'green', )
plt.title("Planetary Positions from man", fontsize = 27)
plt.ylabel("Height (Degrees)", fontsize = 14)
plt.xlabel("<------- Eastward   Distance (AU)   Westward-------> ", fontsize = 14)
plt.legend()
plt.show()



