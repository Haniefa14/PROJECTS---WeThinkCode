# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    while True:
        shape = input('Pick a shape from the list: pyramid, triangle, square, parallelogram, rectangle: ').lower()
        if shape == 'pyramid' or shape == 'triangle' or shape == 'square' or shape == 'parallelogram' or shape == 'rectangle':
            break
    return shape    


# TODO: Step 1 - get height (it must be int!)
def get_height():
    while True:
        height = input('Choose a height (80 max): ')
        if height.isdigit() and int(height) <= 80 and int(height) > 0:
            break
    return int(height)

# TODO: Step 2
def draw_pyramid(height, outline):
    if outline == False:
        for row in range(1,height+1):
            for col in range(height-row):
                print(end=" ")
            for col in range(2*row-1):
                print("*",end="")
            print()
    if outline == True:
        for row in range(1, height+1):
            for col in range(1, 2*height):
                if row==height or row + col == height+1 or col-row== height-1:
                    print('*',end="")
                else:
                    if col >= height + row:
                        break
                    print(end=" ")
            print()

# TODO: Step 3
def draw_square(height, outline):
    if outline == False:
        for col in range(height):
            for row in range(height):
                print("*",end="")
            print()
    
    if outline == True:
        for row in range(height):
            for col in range(height):
                if row == 0 or row == height-1 or col == 0 or col ==height-1:
                    print("*",end="")
                else:
                    print(" ",end="")    
            print()


# TODO: Step 4
def draw_triangle(height, outline):
    if outline == False:
        for clmn in range(height):
            for raw in range(clmn + 1):
                print("*", end="")
            print()

    if outline == True:
        for row in range(height):
            for col in range(row+1):
                if col==0 or row==(height-1) or row==col:
                    print("*", end="")
                else:
                    print(end=" ")
            print()


#Extra Shapes
def draw_rectangle(height, outline):
    if outline == False:
        for row in range(height):
            for col in range(height*2):
                print("*",end="")
            print()
    
    if outline == True:
        for row in range(height):
            for col in range(height*2):
                if row == 0 or row == height-1 or col == 0 or col == (2* height - 1):
                    print("*",end="")
                else:
                    print(end=" ")
            print()
def draw_parallelogram(height, outline):
    if outline == False:
        for row in range(1, height + 1): 
	        for col in range(1, row): 
		        print(end = " ") 
	        for col in range(1, height + 1): 

		        if (row == 1 or row == height or col == 1 or col == height): 
			        print("*", end = "") 
		        else: 
			        print(end = "*") 
	        print()

    if outline == True:
        for row in range(1, height + 1): 
	        for col in range(1, row): 
		        print(end = " ") 
	        for col in range(1, height + 1): 

		        if (row == 1 or row == height or col == 1 or col == height): 
			        print("*", end = "") 
		        else: 
			        print(end = " ") 
	        print()


# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape == "pyramid":
        draw_pyramid(height, outline)
    elif shape == "square":
        draw_square(height, outline)
    elif shape == "triangle":
        draw_triangle(height, outline)
    elif shape == "rectangle":
        draw_rectangle(height, outline)
    elif shape == "parallelogram":
        draw_parralelogram(height, outline)

# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    outline = input("Outline only? (y/N): ").lower()
    if outline == 'y':
        return True
    elif outline == 'n':
        return False
    else:
        get_outline()


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)