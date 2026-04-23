from classes import Snowman
from classes import Rectangle
from classes import Stairs

# Main function choice

class DrawManager:
    def __init__(self):
        self.shapes = {
            "snowman": Snowman,
            "stairs": Stairs,
            "rectangle": Rectangle
        }

    def start(self):
        choice = input("Izberi program (stairs, rectangle, snowman): ")

        if choice == "stairs":
            size = int(input("Height of stairs: "))
            program = Stairs(size)
            program.draw(size)

        elif choice == "rectangle":
            size = int(input("Size of the rectangle: "))
            program = Rectangle(size)
            program.draw(size)

        elif choice == "snowman":
            size1 = int(input("Enter head size: "))
            snowman = Snowman(size1)
            snowman.draw_snowman()
        else:
            print("Not a choice.")
            return


# Entry point of the program
def init():
    manager = DrawManager()
    manager.start()

# Start the program
init()