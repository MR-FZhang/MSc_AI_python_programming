# creating a working robot
import random
facing = ['N', 'S', 'E', 'W']
name = input("Enter the name of your robot: ")
row_coord = random.randint(0, 9) #int(input("Enter the row coordinate of your robot: "))
col_coord = random.randint(0, 9) #int(input("Enter the column coordinate of your robot: "))
direction = random.choice(facing) #input("What is its initial direction [N|S|E|W]: ")
id = 1000
goal_coord = [9,9]

# def correct_bounds(row, col): 
#     if row < 0 :
#         row = 0
#     elif row > 9:    
#         row = 9
#     if col < 0:
#         col = 0
#     elif col > 9:
#         col = 9
    
#     return row, col
    
def quadrant(row, col):
    if row < 5 and col < 5:
        return 'top left'
    elif row < 5 and col >= 5:
        return 'top right'
    elif row >= 5 and col < 5:
        return 'bottom left'
    elif row >= 5 and col >= 5:
        return 'bottom right' 

def move_robot(row, col, direction):
    if direction == "N" and row != 0:
        row -= 1
    elif direction == "S" and row != 9:
        row += 1
    elif direction == "W" and col != 0:
        col -= 1
    elif direction == "E" and col != 9:
        col += 1

    return row, col

def display_direction(direction):
    if direction == "W":
        d_direction = "West"
        d_change  = "N"
    elif direction == "N":
        d_direction = "North"
        d_change  = "E"
    elif direction == "S":
        d_direction = "South"
        d_change  = "W"
    elif direction == "E":
         d_direction = "East"
         d_change  = "S"
    return d_direction, d_change

# row_coord, col_coord = correct_bounds(row_coord, col_coord)
def goal(name, goal_coord, row_coord, col_coord, direction):
    
    print(f"Hello. My name is {name}. My ID is {id}")
    
    while (row_coord != goal_coord[0]) or (col_coord != goal_coord[1]):
        d_direction, d_change  = display_direction(direction)
        if (
            (direction == "N" and row_coord == 0)
            or (direction == "S" and row_coord == 9)
            or (direction == "W" and col_coord == 0)
            or (direction == "E" and col_coord == 9)
        ):

            direction = d_change
        
        print(f"My current lacation is at ({row_coord}, {col_coord}), facing {d_direction}. I am in the {quadrant(row_coord, col_coord)} quadrant")
        row_coord, col_coord = move_robot(row_coord, col_coord, direction)
    
    print(f"My current lacation is at ({row_coord}, {col_coord}), facing {d_direction}. I am in the {quadrant(row_coord, col_coord)} quadrant")

goal(name, goal_coord, row_coord, col_coord, direction)
