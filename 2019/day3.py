import numpy as np

def get_coordinates(path: list, origin = [0,0]):
    coordinates = [origin]
    for instr in path:
        direction = instr[:1]
        length = int(instr[1:])
        if direction == 'R':
            vec = [length,0]
        elif direction == 'L':
            vec = [-length,0]
        elif direction == 'U':
            vec = [0,length]
        elif direction == 'D':
            vec = [0,-length]
        else:
            raise Exception('Direction is not valid')
        new_coord = list(map(sum, zip(coordinates[-1],vec)))    #vectpr addition
        coordinates.append(new_coord)
    
    return coordinates

# def get_all_points(coordinates: list):
#     for i in len(coordinates):
#         delta

        

if __name__ == "__main__":
    
    path1 = ['R8','U5','L5','D3']
    path2 = ['U7','R6','D4','L4']
    
    print(get_coordinates(path = path1))
