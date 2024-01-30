# Read electric_current and electric_voltage from input as floats
electric_current = float(input())
electric_voltage = float(input())

# Compute metal_resistance using the formula
metal_resistance = electric_voltage / electric_current

# Compute metal_conductance using the reciprocal of resistance
metal_conductance = 1 / metal_resistance

# Output the result with the specified formatting
print(f'Metal conductance is {metal_conductance:.4f}')

#This code correctly calculates the metal conductance using the reciprocal of the metal 
#resistance. With the input values 2.0 and 12.0, the output will be Metal conductance
#is 0.1667.
