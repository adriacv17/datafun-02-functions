
# ----------------- INSTRUCTOR GENERATED CODE -----------------

# Use this handy logger to document your work automatically

# import setup_logger function from instructor-generated module
from util_logger import setup_logger

# setup the logger using the current file name (a built-in variable)
logger, logname = setup_logger(__file__)

# ----------------- END INSTRUCTOR GENERATED CODE -----------------


# Import from Python Standard Library

import statistics
import sys

######################################################################
# X data below
######################################################################

#use data from day_x for follwing example
"""day_x list is 1, 3, 6, 9, 12, 15, 18, 21, 24, 27"""

day_x = [1,3,6,9,12,15,18,21,24,27]

logger.info("day_x = " + str(day_x))

# Descriptive: Averages and measures of central tendency

mean = statistics.mean(day_x)
median = statistics.median(day_x)
mode = statistics.mode(day_x)

# log use variable colon formatting to avoid unnecessary digits (e.g. .2f)

logger.info(f"mean of day_x  = {mean:.2f}")
logger.info(f"median of day_x= {median:.2f}")
logger.info(f"mode of day_x = {mode:.2f}")

# Descriptive: Measures of spread

var = statistics.variance(day_x)
stdev = statistics.stdev(day_x)
lowest = min(day_x)
highest = max(day_x)

# TODO: change to f-strings and display 2 decimal places (like we did above)
logger.info(f"var of day_x   =  {var:.2f}")
logger.info(f"stdev of day_x =  {stdev:.2f}")
logger.info(f"lowestof day_x =  {lowest:.2f}")
logger.info(f"highest of day_x=  {highest:.2f}")
logger.info(f"range of day_x is {lowest:.2f} to {highest:.2f}")

logger.info("day_x = " + str(day_x))

######################################################################
# Y axis below
######################################################################

#use data from day_x for follwing example
"""use temp_y data for following exaples"""

temp_y =[37,36,35,34,33,36,37,38,38,38]

# Descriptive: Averages and measures of central tendency

mean = statistics.mean(temp_y)
median = statistics.median(temp_y)
mode = statistics.mode(temp_y)

# log use variable colon formatting to avoid unnecessary digits (e.g. .2f)

logger.info(f"mean of temp_y  = {mean:.2f}")
logger.info(f"median of temp_y= {median:.2f}")
logger.info(f"mode of temp_y = {mode:.2f}")

# Descriptive: Measures of spread

var = statistics.variance(temp_y)
stdev = statistics.stdev(temp_y)
lowest = min(temp_y)
highest = max(temp_y)

# TODO: change to f-strings and display 2 decimal places (like we did above)
logger.info(f"var of temp_y   =  {var:.2f}")
logger.info(f"stdev of temp_y =  {stdev:.2f}")
logger.info(f"lowestof temp_y =  {lowest:.2f}")
logger.info(f"highest of temp_y=  {highest:.2f}")
logger.info(f"range of temp_y is {lowest:.2f} to {highest:.2f}")