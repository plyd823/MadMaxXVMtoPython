import random

# Assuming "vector" is a list or numpy array where the color values are set.
# For simplicity, we will use a list with three elements (RGB).

class Vector:
    def __init__(self):
        self.values = [0.0, 0.0, 0.0]
    
    def set(self, r, g, b):
        """Sets the RGB values of the vector."""
        self.values = [r, g, b]

# Color functions for each XVM section
def weakspot_grey(vector):
    vector.set(0.2, 0.2, 0.2)

def grey(vector):
    vector.set(0.3, 0.3, 0.3)

def blue(vector):
    vector.set(0.0, 0.0, 1.0)

def white(vector):
    vector.set(1.0, 1.0, 1.0)

def black(vector):
    vector.set(0.0, 0.0, 0.0)

def magenta(vector):
    vector.set(1.0, 0.0, 1.0)

def green(vector):
    vector.set(0.0, 1.0, 0.0)

def orange(vector):
    vector.set(229 / 255.0, 61 / 255.0, 0.0)

def dirty_orange(vector):
    vector.set(100 / 255.0, 40 / 255.0, 0.0)

def light_blue(vector):
    vector.set(0.0, 153 / 255.0, 255 / 255.0)

def yellow(vector):
    vector.set(1.0, 1.0, 0.0)

def random_color(vector):
    r = random.random() * 255
    g = random.random() * 255
    b = random.random() * 255
    vector.set(r, g, b)

def cyan(vector):
    vector.set(0.0, 1.0, 1.0)

def purple(vector):
    vector.set(0.5, 0.1, 0.6)

def dark_green(vector):
    vector.set(118 / 255.0, 191 / 255.0, 44 / 255.0)

def red(vector):
    vector.set(1.0, 0.0, 0.0)

# Main driver function to simulate applying the color
def main():
    vector = Vector()  # Create a vector object to store RGB values
    
    # Simulate setting different colors
    print("Setting color to 'Weakspot Grey':")
    weakspot_grey(vector)
    print("RGB values:", vector.values)
    
    print("\nSetting color to 'Grey':")
    grey(vector)
    print("RGB values:", vector.values)
    
    print("\nSetting color to 'Blue':")
    blue(vector)
    print("RGB values:", vector.values)
    
    print("\nSetting color to 'Random':")
    random_color(vector)
    print("RGB values:", vector.values)

    print("\nSetting color to 'Red':")
    red(vector)
    print("RGB values:", vector.values)

if __name__ == "__main__":
    main()
