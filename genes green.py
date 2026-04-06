# make any necessary imports here
import math

# include your function definitions
def area_of_rectangle(width, height):
    area = width * height
    return area

def area_of_circle (diameter):
    area = math.pi * (diameter / 2) ** 2 
    return area
    
def perimeter_of_rectangle(width, height):
    perimeter = width * 2 + (height * 2)
    return perimeter
    
def perimeter_of_circle(diameter):
    perimeter = 2 * math.pi * (diameter / 2)
    return perimeter
    
def area_of_tee(width):
    diameter = width / 4
    total_tee_area = area_of_circle(diameter)
    return total_tee_area 
    
def area_of_putting_green(width):
    diameter = width / 2
    total_putting_green_area = area_of_circle(diameter)
    return total_putting_green_area
    
def area_of_sand_trap(width):
    diameter = width / 3
    total_sand_trap_area = area_of_circle(diameter)
    return total_sand_trap_area

def number_of_bushes(width, length):
    height = length - 1
    total_bushes = int(perimeter_of_rectangle(width, height))
    return total_bushes
    
def number_of_bricks(width):
    diameter = width * 3
    total_bricks = math.ceil(perimeter_of_circle(diameter)/2)
    return total_bricks
    
def tons_of_sand(width):
    width_feet = width * 3
    total_tons_of_sand = math.ceil(area_of_sand_trap(width_feet) * 0.05)
    return total_tons_of_sand
    
# collect the inputs
length = float(input('Enter Course Length : '))
width = float(input('Enter Course Width  : '))

# compute the required outputs
total_area_smooth_sod = math.ceil(area_of_tee(width) + area_of_putting_green(width))
total_area_rough_sod = math.ceil(area_of_rectangle(width, length) - total_area_smooth_sod - area_of_sand_trap(width))
total_tons_of_sand = (tons_of_sand(width))
number_of_walls = int(number_of_bricks(width))
total_bushes = number_of_bushes(width, length)

# results
print('Total square yards of rough sod  :', total_area_rough_sod)
print('Total square yards of smooth sod :', total_area_smooth_sod)
print('Tons of sand                     :', total_tons_of_sand)
print('Number of retaining wall bricks  :', number_of_walls)
print('Number of bushes     
