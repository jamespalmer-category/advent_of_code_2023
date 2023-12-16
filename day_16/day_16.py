import re
import ast
import numpy as np
import math
#from functools import cache
from itertools import product

def read_file_to_string(file_path):
    with open(file_path,'r') as f:
        return f.read()
    
def parse_string(string):

    return np.array([np.array(list(row)) for row in string.split('\n')])

cache = {}

def beam_of_light(grid, start, direction='right'):

    position = start
    visited = [start]
    

    while 0 <= start[0] < grid.shape[0] and 0 < start[1] < grid.shape[1]:
        print(position)

        if direction == 'right':
            position = (position[0], position[1]+1)
            visited.append(position)

            if grid[position] in '.-':
                continue
            elif grid[position] =='|':
                if (position, 'up') not in cache.keys() and (position, 'down') not in cache.keys():
                    cache[(position, 'up')] = True
                    cache[(position, 'down')] = True
                    visited = visited + beam_of_light(grid, position, direction='up') + beam_of_light(grid, position, direction='down')
                    
                break

            elif grid[position] == '/':
                if (position, 'up') not in cache.keys():
                    cache[(position, 'up')] = True
                    visited = visited + beam_of_light(grid, position, direction='up')
                    
                break

            elif grid[position] == '\\':
                if (position, 'down') not in cache.keys():
                    cache[(position, 'down')] = True
                    visited = visited + beam_of_light(grid, position, direction='down')
                    
                break

        elif direction == 'left':
            position = (position[0], position[1]-1)
            visited.append(position)

            if grid[position] in '.-':
                continue

            elif grid[position] =='|':
                if (position, 'up') not in cache.keys() and (position, 'down') not in cache.keys():
                    cache[(position, 'up')] = True
                    cache[(position, 'down')] = True
                    visited = visited + beam_of_light(grid, position, direction='up') + beam_of_light(grid, position, direction='down')
                    
                break

            elif grid[position] == '/':
                if (position, 'down') not in cache.keys():
                    cache[(position, 'down')] = True
                    visited = visited + beam_of_light(grid, position, direction='down')
                    
                break

            elif grid[position] == '\\':
                if (position, 'up') not in cache.keys():
                    cache[(position, 'up')] = True
                    visited = visited + beam_of_light(grid, position, direction='up')
                    
                break

        elif direction == 'up':
            position = (position[0]-1, position[1])
            visited.append(position)

            if grid[position] in '.|':
                continue
            
            elif grid[position] =='-':
                if (position, 'left') not in cache.keys() and (position, 'right') not in cache.keys():
                    cache[(position, 'left')] = True
                    cache[(position, 'right')] = True
                    visited = visited + beam_of_light(grid, position, direction='left') + beam_of_light(grid, position, direction='right')
                    
                break

            elif grid[position] == '/':
                if (position, 'right') not in cache.keys():
                    cache[(position, 'right')] = True
                    visited = visited + beam_of_light(grid, position, direction='right')
                    
                break

            elif grid[position] == '\\':
                if (position, 'left') not in cache.keys():
                    cache[(position, 'left')] = True
                    visited = visited + beam_of_light(grid, position, direction='left')
                    
                break

        elif direction == 'down':
            position = (position[0]+1, position[1])
            visited.append(position)

            if grid[position] in '.|':
                continue
            
            elif grid[position] =='-':
                if (position, 'left') not in cache.keys() and (position, 'right') not in cache.keys():
                    cache[(position, 'left')] = True
                    cache[(position, 'right')] = True
                    visited = visited + beam_of_light(grid, position, direction='left') + beam_of_light(grid, position, direction='right')
                    
                break

            elif grid[position] == '/':
                if (position, 'left') not in cache.keys():
                    cache[(position, 'left')] = True
                    visited = visited + beam_of_light(grid, position, direction='left')
                    
                break

            elif grid[position] == '\\':
                if (position, 'right') not in cache.keys():
                    cache[(position, 'right')] = True
                    visited = visited + beam_of_light(grid, position, direction='right')
                    
                break

    return list(set(visited))

if __name__ == '__main__':

    day_16_test = read_file_to_string('day_16_test.txt')
    day_16_test_grid = parse_string(day_16_test)
    beam_of_light(day_16_test_grid, (0,0), direction='right')