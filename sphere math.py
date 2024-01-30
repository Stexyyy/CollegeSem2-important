import math

sphere_radius = float(input())

# Compute the surface area of the sphere
sphere_area = 4 * math.pi * (sphere_radius ** 2)


print(f'{sphere_area:.2f}')

#This program first reads the sphere radius as a float from the user, then calculates the
#surface area using the formula, and finally prints the result rounded to two decimal 
#places. If the input is 3.10, the output should be 120.76.
