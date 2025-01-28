# Function to display the menu options
def display_menu():
    print("\nShopping Cart Menu:")
    print("1. Add item to cart")
    print("2. View cart items")
    print("3. Calculate total price")
    print("4. Exit")

# Function to add an item to the cart
def add_item(cart):
    # Ask user for item name and price
    item_name = input("Enter the item name: ")
    item_price = float(input("Enter the item price: "))
    # Add the item as a tuple (name, price) to the cart
    cart.append((item_name, item_price))
    print(f"{item_name} added to the cart.")

# Function to view items in the cart
def view_cart(cart):
    if not cart:  # Check if the cart is empty
        print("Your cart is empty.")
    else:
        print("\nItems in your cart:")
        # Loop through and display each item and its price
        for i, (name, price) in enumerate(cart, start=1):
            print(f"{i}. {name} - ${price:.2f}")

# Function to calculate the total price of items in the cart
def calculate_total(cart):
    # Sum the prices of all items in the cart
    total = sum(price for _, price in cart)
    print(f"Total price: ${total:.2f}")

# Main program
def shopping_cart():
    cart = []  # Initialize an empty list to store cart items
    while True:  # Start an infinite loop for the menu
        display_menu()  # Show the menu options
        choice = input("Enter your choice (1-4): ")  # Get user input for menu choice
        if choice == "1":  # Add an item to the cart
            add_item(cart)
        elif choice == "2":  # View items in the cart
            view_cart(cart)
        elif choice == "3":  # Calculate and display the total price
            calculate_total(cart)
        elif choice == "4":  # Exit the program
            print("Exiting the shopping cart. Goodbye!")
            break
        else:  # Handle invalid menu choices
            print("Invalid choice. Please try again.")

# Run the shopping cart program
shopping_cart()
