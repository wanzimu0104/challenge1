# CHALLENGE PROBLEMS
# YOU MAY NOT USE ANY ADDITIONAL LIBRARIES OR PACKAGES TO COMPLETE THIS CHALLENGE

# Divvy is Chicago's bike share system, which consists of almost 600 stations scattered
# around the city with blue bikes available for anyone to rent. Users begin a ride by removing
# a bike from a dock, and then they can end their ride by returning the bike to a dock at any Divvy 
# station in the city. You are going to use real data from Divvy collected at 1:30pm on 4/7/2020 
# to analyze supply and demand for bikes in the system. 

# NOTE ** if you aren't able to run this, type "pip install json" into your command line
import json
import numpy
# do not delete; this is the data you'll be working with
divvy_stations = json.loads(open('divvy_stations.txt').read())
print(divvy_stations)

# PROBLEM 1
# find average number of empty docks (num_docks_available) and
# available bikes (num_bikes_available) at all stations in the system
list_num_docks_available = []

for i in divvy_stations:
    list_num_docks_available.append(i["num_docks_available"])

avg_empty_docks = numpy.mean (list_num_docks_available)
# print(avg_empty_docks) 9.532773109243697

list_num_bikes_available = []

for i in divvy_stations:
    list_num_bikes_available.append(i["num_bikes_available"])

avg_available_bikes = numpy.mean(list_num_bikes_available)
#print(avg_available_bikes) 7.7596638655462185


# PROBLEM 2
# find ratio of bikes that are currently rented to total bikes in the system (ignore ebikes)
list_total_bikes = []

for i in divvy_stations:
    list_total_bikes.append(
        float(i["num_bikes_disabled"]) +
        float(i["num_docks_available"]) +
        float(i["num_bikes_available"]))
# total bikes = disabled bikes + empty docks (unavailable bikes) + available bikes

total_bikes = sum(list_total_bikes)
#print(total_bikes) #10308

list_num_bikes_rented = []

for i in divvy_stations:
    list_num_bikes_rented.append(i["num_docks_available"]) # rented bikes= empty docks

num_bikes_rented = sum(list_num_bikes_rented)
#print(num_bikes_rented) #5672

ratio_rented = num_bikes_rented / total_bikes
#print(ratio_rented) #0.5502522312766783

# PROBLEM 3 
# Add a new variable for each divvy station's entry, "percent_bikes_remaining", that shows 
# the percentage of bikes available at each individual station (again ignore ebikes). 
# This variable should be formatted as a percentage rounded to 2 decimal places, e.g. 66.67%

