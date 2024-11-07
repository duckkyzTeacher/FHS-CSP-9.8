# For each of the functions below, I recommend writing test for the original function and then 
# refactoring the function in a new function. Then write tests for your new function and verify
# the outputs are identical



# 1. Refactor the following function for better readability by renaming variables and adding comments:
#    Test the function with various inputs to ensure it still works correctly after refactoring.
#   def fn(a, b, c):
#       return a + b * c
def fn(a, b, c):
    return a + b * c

def yourFunctionNameHere():





# 2. Refactor the following function to make it reusable:
#    def print_rectangle():
#        for i in range(3):
#            print('*' * 5)
#    Modify the function so that it can print a rectangle of any size.
def new_print_rectangle(length, width):




# 3. Refactor the 'checkout' function so that the discount is applied in a function called 
#    'calcTotal' that takes in a subtotal and tax rate and returns the properly adjusted total.
#    Feel free to refactor the function further if needed.
def checkout(cart, tax_rate=0.08):
    # Calculate subtotal
    subtotal = 0
    for item in cart:
        subtotal += item['price'] * item['quantity']
    
    # Apply discount based on subtotal
    if subtotal > 100:
        discount = 0.1  # 10% discount for orders over $100
        subtotal -= subtotal * discount
    elif subtotal > 50:
        discount = 0.05  # 5% discount for orders over $50
        subtotal -= subtotal * discount
    
    # Add tax
    total = subtotal + (subtotal * tax_rate)
    
    return total

def calcTotal(subtotal, taxRate):
    #WRITE YOUR CODE HERE
    
    return subtotal



#DONT MODIFY BELOW
def newCheckout(cart, tax_rate=0.08):
    # Calculate subtotal
    subtotal = 0
    for item in cart:
        subtotal += item['price'] * item['quantity']
    
    # Apply discount based on subtotal and add tax
    total = calcTotal(subtotal, tax_rate)
        
    return total
























def test_checkout():
    # Test 1: Basic functionality without discount
    cart = [{'price': 10, 'quantity': 1}, {'price': 3, 'quantity': 10}]  # Total = 40, no discount
    result = checkout(cart)
    expected = 40 + (40 * 0.08)  # Adding 8% tax to 40
    assert abs(result - expected) < 0.01, f"Test 1 failed: expected {expected}, got {result}"

    # Test 2: Applying 5% discount (subtotal > 50)
    cart = [{'price': 20, 'quantity': 3}]  # Total = 60, 5% discount
    result = checkout(cart)
    subtotal_with_discount = 60 * 0.95  # 5% discount applied
    expected = subtotal_with_discount + (subtotal_with_discount * 0.08)  # Adding 8% tax
    assert abs(result - expected) < 0.01, f"Test 2 failed: expected {expected}, got {result}"

    # Test 3: Applying 10% discount (subtotal > 100)
    cart = [{'price': 30, 'quantity': 4}]  # Total = 120, 10% discount
    result = checkout(cart)
    subtotal_with_discount = 120 * 0.9  # 10% discount applied
    expected = subtotal_with_discount + (subtotal_with_discount * 0.08)  # Adding 8% tax
    assert abs(result - expected) < 0.01, f"Test 3 failed: expected {expected}, got {result}"

    # Test 4: No discount, different tax rate
    cart = [{'price': 10, 'quantity': 5}]  # Total = 50, no discount
    result = checkout(cart, tax_rate=0.1)  # 10% tax rate
    expected = 50 + (50 * 0.1)  # Adding 10% tax to 50
    assert abs(result - expected) < 0.01, f"Test 4 failed: expected {expected}, got {result}"

    # Test 5: Empty cart
    cart = []  # Total = 0
    result = checkout(cart)
    expected = 0  # No items, total should be 0
    assert result == expected, f"Test 5 failed: expected {expected}, got {result}"

    print("All checkout tests passed!")

def test_newCheckout():
    # Test 1: Basic functionality without discount
    cart = [{'price': 10, 'quantity': 1}, {'price': 3, 'quantity': 10}]  # Total = 40, no discount
    result = newCheckout(cart)
    expected = 40 + (40 * 0.08)  # Adding 8% tax to 40
    assert abs(result - expected) < 0.01, f"Test 1 failed: expected {expected}, got {result}"

    # Test 2: Applying 5% discount (subtotal > 50)
    cart = [{'price': 20, 'quantity': 3}]  # Total = 60, 5% discount
    result = newCheckout(cart)
    subtotal_with_discount = 60 * 0.95  # 5% discount applied
    expected = subtotal_with_discount + (subtotal_with_discount * 0.08)  # Adding 8% tax
    assert abs(result - expected) < 0.01, f"Test 2 failed: expected {expected}, got {result}"

    # Test 3: Applying 10% discount (subtotal > 100)
    cart = [{'price': 30, 'quantity': 4}]  # Total = 120, 10% discount
    result = newCheckout(cart)
    subtotal_with_discount = 120 * 0.9  # 10% discount applied
    expected = subtotal_with_discount + (subtotal_with_discount * 0.08)  # Adding 8% tax
    assert abs(result - expected) < 0.01, f"Test 3 failed: expected {expected}, got {result}"

    # Test 4: No discount, different tax rate
    cart = [{'price': 10, 'quantity': 5}]  # Total = 50, no discount
    result = newCheckout(cart, tax_rate=0.1)  # 10% tax rate
    expected = 50 + (50 * 0.1)  # Adding 10% tax to 50
    assert abs(result - expected) < 0.01, f"Test 4 failed: expected {expected}, got {result}"

    # Test 5: Empty cart
    cart = []  # Total = 0
    result = newCheckout(cart)
    expected = 0  # No items, total should be 0
    assert result == expected, f"Test 5 failed: expected {expected}, got {result}"

    print("All newCheckout tests passed!")

# Run the tests
test_checkout()
try:
    test_newCheckout()
except AssertionError as e:
    print(e)
    
#DONT MODIFY ABOVE