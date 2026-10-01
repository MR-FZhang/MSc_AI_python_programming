# creating a working robot

name = input("Enter the name of your robot: ")
row_coord = int(input("Enter the row coordinate of your robot: "))
col_coord = int(input("Enter the column coordinate of your robot: "))
direction = input("What is its initial direction [N|S|E|W]: ")
id = 1000

def correct_bounds(row, col):
    if row < 0 :
        row = 0
    elif row > 9:    
        row = 9
    
    if col < 0:
        col = 0
    elif col > 9:
        col = 9
    
    return row, col
    
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
    else:
        if col != 9:
            col += 1
    return row, col

def display_direction(direction):
    if direction == "W":
        d_direction = "West"
    elif direction == "N":
        d_direction = "North"
    elif direction == "S":
        d_direction = "South"
    elif direction == "E":
         d_direction = "East"
    return d_direction

row_coord, col_coord = correct_bounds(row_coord, col_coord)
print(row_coord, col_coord)
d_direction = display_direction(direction)

print(f"Hello. My name is {name}. My ID is {id}")
print(f"I am located is ({row_coord}, {col_coord}). I am in the {quadrant(row_coord, col_coord)} quadrant")

row_coord, col_coord = move_robot(row_coord, col_coord, direction)

print(f"I am facing {d_direction}")
print(f"My current lacation is ({row_coord}, {col_coord}). I am in the {quadrant(row_coord, col_coord)} quadrant")