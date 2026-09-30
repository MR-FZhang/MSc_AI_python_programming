# creating a working robot

name = input("Enter the name of your robot: ")
row_coord = int(input("Enter the row coordinate of your robot: "))
col_coord = int(input("Enter the column coordinate of your robot: "))
id = 1000

def correct_bounds(row, col):
    if row < 0 :
        row = 0
    if col < 0:
        col = 0
        row = 9
    if col > 9:
        col = 9
    return row, col
    
def quadrant(row, col):
    if row < 5 and col < 5:
        return 'top left'
    elif row < 5 and col > 5:
        return 'top right'
    elif row > 5 and col < 5:
        return 'bottom left'
    elif row > 5 and col > 5:
        return 'bottom right' 

row_coord, col_coord = correct_bounds(row_coord, col_coord)

print(f"Hello. My name is {name}. My ID is {id}")
print(f"I am located is ({row_coord}, {col_coord}). I am in the {quadrant(row_coord, col_coord)} quadrant")