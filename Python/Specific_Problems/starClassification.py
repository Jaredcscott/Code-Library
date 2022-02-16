'''
    @Author Jared Scott ☯
    This function will classify a start using the stars properties. 
    Properties needed to classify:
        Temperature: In degrees Kelvin
        Radius     : In Solar Radii (Multiples of the Sun's radius) 
        Luminosity : In multiples of the Sun's luminosity 
        Solar Mass : In multiples of the Sun's solar Mass  

      Will classify a star following categories based on the given properties
      O, B, A, F, G, K and M
'''

def star( temperature="null", radius="null", luminosity="null", solar_mass="null"):
    #These values are pulled from https://en.wikipedia.org/wiki/Stellar_classification 
    #They use the Harvard system of classification
    
    #This temerature is in Kelvin
    if temperature != "null":
        if temperature >= 30000:
            return "A star with surface temperature " + str(temperature) + " is of type O"
        elif 10000 <= temperature and temperature < 30000:
            return "A star with surface temperature " + str(temperature) + " is of type B"
        elif 7500 <= temperature and temperature < 10000:
            return "A star with surface temperature " + str(temperature) + " is of type A"
        elif 6000 <= temperature and temperature < 7500:
            return "A star with surface temperature " + str(temperature) + " is of type F"
        elif 5000 <= temperature and temperature < 6000:
            return "A star with surface temperature " + str(temperature) + " is of type G"
        elif 3700 <= temperature and temperature < 5000:
            return "A star with surface temperature " + str(temperature) + " is of type K"
        elif 0 <= temperature and temperature < 3700:
            return "A star with surface temperature " + str(temperature) + " is of type M"
        else:
            return "A star cannot have negative temerature, invalid input"
    
    #This radius is in solar radii
    if radius != "null":
        if radius >= 6.6:
            return "A star with radius " + str(radius) + " is of type O"
        elif 1.8 <= radius and radius < 6.6:
            return "A star with radius " + str(radius) + " is of type B"
        elif 1.4 <= radius and radius < 1.8:
            return "A star with radius " + str(radius) + " is of type A"
        elif 1.15 <= radius and radius < 1.4:
            return "A star with radius " + str(radius) + " is of type F"
        elif .96 <= radius and radius < 1.15:
            return "A star with radius " + str(radius) + " is of type G"
        elif .7 <= radius and radius < .96:
            return "A star with radius " + str(radius) + " is of type K"
        elif 0 <= radius and radius < .7:
            return "A star with radius " + str(radius) + " is of type M"
        else:
            return "A star cannot have negative radius, invalid input"
        
    #The luminosity of our sun is 1
    if luminosity != "null":
        if luminosity >= 30000:
            return "A star luminosity " + str(luminosity) + " is of type O"
        elif 25 <= luminosity and luminosity < 30000:
            return "A star with luminosity " + str(luminosity) + " is of type B"
        elif 5 <= luminosity and luminosity < 25:
            return "A star with luminosity " + str(luminosity) + " is of type A"
        elif 1.5 <= luminosity and luminosity < 5:
            return "A star with luminosity " + str(luminosity) + " is of type F"
        elif .6 <= luminosity and luminosity < 1.5:
            return "A star with luminosity " + str(luminosity) + " is of type G"
        elif .08 <= luminosity and luminosity < .6:
            return "A star with luminosity " + str(luminosity) + " is of type K"
        elif 0 <= luminosity and luminosity < .08:
            return "A star with luminosity " + str(luminosity) + " is of type M"
        else:
            return "A star cannot have negative luminosity, invalid input"
        
    #This mass is in solar masses
    if solar_mass != "null":
        if solar_mass >= 16:
            return "A star with solar mass " + str(solar_mass) + " is of type O"
        elif 2.1 <= solar_mass and solar_mass < 16:
            return "A star with solar mass " + str(solar_mass) + " is of type B"
        elif 1.4 <= solar_mass and solar_mass < 2.1:
            return "A star with solar mass " + str(solar_mass) + " is of type A"
        elif 1.04 <= solar_mass and solar_mass < 1.4:
            return "A star with solar mass " + str(solar_mass) + " is of type F"
        elif .8 <= solar_mass and solar_mass < 1.04:
            return "A star with solar mass " + str(solar_mass) + " is of type G"
        elif .45 <= solar_mass and solar_mass < .8:
            return "A star with solar mass " + str(solar_mass) + " is of type K"
        elif 0 <= solar_mass and solar_mass < .45:
            return "A star with solar mass " + str(solar_mass) + " is of type M"
        else:
            return "A star cannot have negative solar mass, invalid input"
