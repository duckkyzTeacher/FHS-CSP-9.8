def printExampleHeader(exampleNum):
    print(f"~Example {exampleNum}:\n\n")
#DEMO:


printExampleHeader(1)
#Adding clarity in names an comments
def calc_area(w, h):
    return w * h

# Refactored version with clearer variable names and documentation
def calculate_rectangle_area(width, height):
    """
    Calculates the area of a rectangle.
    """
    return width * height


printExampleHeader(2)
#Adding modularity to functions for resuablity 
def print_square():
    for i in range(5):
        print('*' * 5)

# Refactored version
def print_square(size):
    """
    Prints a square of a given size.
    """
    for i in range(size):
        print('*' * size)

print_square(3)



printExampleHeader(3)
#Reducing complexity and adding readability 
def calculate_total(cart):
    total = 0
    for item in cart:
        total += item['price']
    tax = total * 0.07
    return total + tax

# Refactored version
def calculate_subtotal(cart):
    total = 0
    for item in cart:
        total += item['price']
    return total

def calculate_tax(subtotal):
    return subtotal * 0.07

def calculate_total(cart):
    subtotal = calculate_subtotal(cart)
    return subtotal + calculate_tax(subtotal)






















printExampleHeader(4)
def printTriangle():
    for row in range(5):
        # Print leading spaces
        for spaces in range(5 - row):
            print(" ", end="")
        
        # Print asterisks for the current row
        for stars in range(1, 2*row):
            print("*", end="")
        print()

# Refactored version
def printAnyTriangle(size):
    """
    Prints a triangle of a given size.
    """
    for row in range(1, size + 1):
        # Print leading spaces
        for spaces in range(size - row):
            print(" ", end="")
        
        # Print asterisks for the current row
        for stars in range(1, 2*row):
            print("*", end="")
        print()


printTriangle()
print()
printAnyTriangle(3)
print()
printAnyTriangle(5)
print()
printAnyTriangle(10)
