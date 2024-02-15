from dao.OrderProcessorRepositoryImpl import OrderProcessorRepositoryImpl
from exception.CustomerNotFoundException import CustomerNotFoundException
from exception.ProductNotFoundException import ProductNotFoundException
from exception.OrderNotFoundException import OrderNotFoundException

def main():
    order_processor = OrderProcessorRepositoryImpl()

    while True:
        print("\n1. Register Customer")
        print("2. Create Product")
        print("3. Delete Product")
        print("4. Add to Cart")
        print("5. View Cart")
        print("6. Place Order")
        print("7. View Customer Order")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            register_customer(order_processor)
        elif choice == "2":
            create_product(order_processor)
        elif choice == "3":
            delete_product(order_processor)
        elif choice == "4":
            add_to_cart(order_processor)
        elif choice == "5":
            view_cart(order_processor)
        elif choice == "6":
            place_order(order_processor)
        elif choice == "7":
            view_customer_order(order_processor)
        elif choice == "8":
            print("Exiting the application...")
            break
        else:
            print("Invalid choice! Please try again.")

def register_customer(order_processor):
    # Implement customer registration logic
    pass

def create_product(order_processor):
    # Implement product creation logic
    pass

def delete_product(order_processor):
    # Implement product deletion logic
    pass

def add_to_cart(order_processor):
    # Implement add to cart logic
    pass

def view_cart(order_processor):
    # Implement view cart logic
    pass

def place_order(order_processor):
    # Implement place order logic
    pass

def view_customer_order(order_processor):
    # Implement view customer order logic
    pass

if __name__ == "__main__":
    main()





