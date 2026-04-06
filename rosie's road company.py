import math

def number_of_stoplights(miles, lanes):
    stoplights_per_intersection = lanes + 2
    number_of_intersections = int(miles)
    total_stoplights = number_of_intersections * stoplights_per_intersection
    return total_stoplights
    
def truckloads_of_asphalt(miles, lanes, depth_inches):
    road_length = miles * 5280
    road_width = lanes * 12
    road_depth = depth_inches / 12
    asphalt_cubic_feet = road_length * road_width * road_depth
    asphalt_pounds = asphalt_cubic_feet * 145
    approximate_truck_loads = asphalt_pounds / 10000
    total_truckloads = math.ceil(approximate_truck_loads)
    return total_truckloads
    
def number_of_power_pipes(miles):
    feet = miles * 5280
    approximate_power_pipes = feet / 20
    total_power_pipes = math.ceil(approximate_power_pipes)
    return total_power_pipes

def number_of_water_pipes(miles):
    feet = miles * 5280
    approximate_water_pipes = feet / 10
    total_water_pipes = math.ceil(approximate_water_pipes)
    return total_water_pipes

def number_of_crew_members(miles, lanes, number_of_days):
    miles_of_road = miles
    number_of_lanes = lanes
    days_to_complete = number_of_days
    crew_members = (50 * miles_of_road * number_of_lanes) / days_to_complete
    return math.ceil(crew_members)
    
#inputs    
miles = float(input('Enter Road Project Length in Miles : '))
lanes = int(input('Enter Number of Lanes              : '))
depth_inches = int(input('Enter Depth of Asphalt in Inches   : '))
number_of_days = int(input('Enter Days to Complete Project     : '))

#call function
asphalt_truckloads = truckloads_of_asphalt(miles, lanes, depth_inches)
stoplights = number_of_stoplights(miles, lanes)
water_pipes = number_of_water_pipes(miles)
power_pipes = number_of_power_pipes(miles)
number_of_crew_members = number_of_crew_members(miles, lanes, number_of_days)

#calculations
cost_of_asphalt = 750 * asphalt_truckloads
cost_of_stoplights = 25000 * stoplights
cost_of_water_pipes = 200 * water_pipes
cost_of_power_pipes = 400 * power_pipes
cost_of_labor = (160 * number_of_days) * number_of_crew_members
total_cost = cost_of_asphalt + cost_of_stoplights + cost_of_water_pipes + cost_of_power_pipes + cost_of_labor

#results
print("=== Amount of materials needed ===")
print("Truckloads of Asphalt :", asphalt_truckloads)
print("Stoplights            :", stoplights)
print("Water pipes           :", water_pipes)
print("Power pipes           :", power_pipes)
print("Crew members needed   :", number_of_crew_members)
print("=== Cost of Materials ============")
print("Cost of Asphalt       :", cost_of_asphalt)
print("Cost of Stoplights    :", cost_of_stoplights)
print("Cost of Water pipes   :", cost_of_water_pipes)
print("Cost of Power pipes   :", cost_of_power_pipes)
print("Cost of Labor         :", cost_of_labor)
print("=== Total Cost of Project ========")
print("Total cost of project :", total_cost)
