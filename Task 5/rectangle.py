# Define a Rectangle class
class Rectangle:
    # Constructor: initializes width and height of the rectangle
    def __init__(self, height, width):
        self.width = width
        self.height = height

    # Method to draw the rectangle using '*' characters
    def draw(self):
        for i in range(self.height):  # Loop over each row
            print("* " * self.width)  # Print a row of '*' repeated width times

# Main function to get user input and draw the rectangle
def main():
    width = int(input("Enter the rectangle width: "))   # Ask user for width
    height = int(input("Enter the rectangle height: ")) # Ask user for height
    rectangle = Rectangle(height, width)                # Create Rectangle object
    rectangle.draw()                                    # Call draw method

# Entry point function
def init():
    main()  # Call main function

# Start the program
init()
