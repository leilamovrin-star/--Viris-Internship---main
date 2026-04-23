# Class to draw a snowman of a given size
class Snowman:
    def __init__(self, size):
        self.size = size
        self.body = size + 2
        self.base = size + 4

    # Draw a square of given size
    # 'eyes' draws eyes only for the head
    def draw_section(self, size, eyes=False):
        for i in range(size):
            for j in range(size):
                if i == 0 or i == size-1 or j == 0 or j == size-1:
                    print("*", end=" ")
                elif eyes and i == 1 and (j == 1 or j == size-2):
                    print("o", end=" ")
                else:
                    print(" ", end=" ")
            print()
    
    # Draw the full snowman
    def draw_snowman(self):
        print("_===_".center(self.size * 2))
        self.draw_section(self.size, eyes=True)  # head
        self.draw_section(self.body)             # body
        self.draw_section(self.base)             # base

# Class to draw stairs
class Stairs:
    def __init__(self, width):
        self.width = width  # Store width (not used in this simple example)

    # Draw stairs of height 'y'
    def draw(self, y):
        for i in range(1, y + 1):  # Loop through each step
            print("*" * i)  # Print a row with increasing number of stars
        self.draw(self.width)


# Class to draw a rectangle
class Rectangle:
    def __init__(self, width):
        self.width = width  # Store the width of the rectangle

    # Draw a rectangle of size 'x' x 'x'
    def draw(self, x):
        for i in range(x):  # Loop over rows
            print("*" * x)  # Print a row of stars
        self.draw(self.width)