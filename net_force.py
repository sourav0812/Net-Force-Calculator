from math import sin, cos, tan, asin, acos, atan2, radians, degrees, sqrt

def find_net_force(forces):
    horizontal = 0
    vertical = 0
    for value in forces:
        horizontal += value[0] * cos(radians(value[1]))
        vertical += value[0] * sin(radians(value[1]))
    
    total_magnitude = sqrt((horizontal**2) + (vertical**2))
    angle = degrees(atan2(vertical, horizontal))

    return round(total_magnitude, 1), round(angle, 1)
    
#If your function works correctly, this will originally
#print: (87.0, 54.4)
forces = [(10, 90), (10, -90), (100, 45), (20, 180)]
print(find_net_force(forces))
