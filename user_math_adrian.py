"""
Adrian Vega 09/01/2023 Project 2 

Import the math module.
Steal the logging setup code from any of the examples.
Define at least one function that you might use in your domain - a simple reusable math function. 
Implement the function to calculate the correct area. 

"""
#Importing math from libraries#

import math

import statistics as stats


#Borrowing logger code from defensive_math.py#

from util_logger import setup_logger
logger, logname = setup_logger(__file__)


#Function to find area of office# 

def area_of_office(height,width):
    """return area of office given height and width"""
    try: 
        area = height * width
        logger.info(f"The office area is {area} sqft")
        return area  #will return area to function#
    except Exception as ex:
        logger.error(f"Error: {ex}")
        return None
    
#Function to find parameter of office useful when trying to set up an instrumentation line#
    
def get_parameter(sides):
    """supply any amount of lengths in floats/ints to get parameter"""
    try:
        parameter = math.fsum(sides)
        logger.info(f"The office parameter is {parameter} ft")
        return parameter
    except Exception as ex:
        logger.error(f"Error: {ex}")
        return None
    
#Function to find the average glucose in a year#

def get_avg_glucose(glucose):
    """calculate average from monthly glucose for a year(not an a1c)"""
    try:
        average = math.fsum(glucose)/len(glucose)
        logger.info(f"The average glucose for one year is {average:.1f} mg/dl")
        return average
    except Exception as ex:
        logger.error(f"Error: {ex}")
        return None
    
#get range of temperatures in lab from list

def temp_range(temp):
    try:
        min_temp = min(temp)
        max_temp = max(temp)
        logger.info(f"The range of temperature in the lab is {min_temp} to {max_temp} degrees celcius")
        return min_temp and max_temp
    except Exception as ex:
        logger.effor(f"Error: {ex}")
        return None
        

if __name__ == "__main__":

#Just trying some permutations and combinations#

    logger.info("Explore some functions in the math module")
    logger.info(f"math.comb(5,1) = {math.comb(5,1)}")
    logger.info(f"math.perm(5,1) = {math.perm(5,1)}")
    logger.info(f"math.comb(5,3) = {math.comb(5,3)}")
    logger.info(f"math.perm(5,3) = {math.perm(5,3)}")
    logger.info(f"math.pi = {math.pi}")
    logger.info(f"math.degrees(2 * math.pi) = {math.degrees(2 * math.pi)}")
    logger.info(f"math.radians(180)         = {math.radians(180)}")
    logger.info("")

#Calling area function

    logger.info("TRY: Call area_of_office() function with different values.") 

    """Call new function three times with different values"""

    area_of_office(15, 10)
    area_of_office(15, 15)
    area_of_office(12, 12)
    logger.info("")

#Calling parameter function

    """Call parameter function with list of different values"""

    logger.info("TRY: Call get_parameter() function with a list of office side measurements")
    sides_list = [15, 15.4, 10.5, 10.1]
    get_parameter(sides_list)
    sides_list = [10,10,10,10]
    get_parameter(sides_list)
    logger.info("")
    
#Calling get_avg_glucose

    """Call glucose function with 12 different values for average"""
    
    logger.info("TRY: Call get_avg_glucose() function with list of 12 monthly data points in mg/dl")
    glucose_lvls = [80,90,95.1,99.5,110,85.5,86,87.4,93,94.5,96.7,100]
    get_avg_glucose(glucose_lvls)
    logger.info("")

#Calling temp_range function

    """Call temp range function with a list of temperatures to get a range"""

    logger.info("TRY: Call temp_range() function with list of temperatures in celcius ")
    temp_lvls = [27,37,37,36,40,30,35,34]
    temp_range(temp_lvls)
    logger.info("")