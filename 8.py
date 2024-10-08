print("Welcome To Bike Shop")

bikes = ["MTB", "Geared", "Non-Geared", "With Training Wheels", "For Trial Riding"]
net = 0  # Initialize net revenue

while True:
    print("\nChoose any of the following Services:")
    print("1: View Bikes on Sale")
    print("2: View Prices")
    print("3: Place Orders")
    print("4: Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print("\nThe Bikes Available are:")
        for bike in bikes:
            print(bike)
    
    elif choice == 2:
        print("\nThe prices at our store are:")
        print("1. Hourly ---- $100")
        print("2. Daily ---- $500")
        print("3. Weekly ---- $2500")
        print("Family pack gets 30% discount on 3-5 bikes")
    
    elif choice == 3:
        print("\nChoose your rental type:")
        print("1. Hourly")
        print("2. Daily")
        print("3. Weekly")
        
        rental_type = int(input("Enter your option: "))
        number_of_bikes = int(input("Enter the number of bikes (3-5 to avail family pack option): "))
        
        if rental_type == 1:
            bill = 100 * number_of_bikes
        elif rental_type == 2:
            bill = 500 * number_of_bikes
        elif rental_type == 3:
            bill = 2500 * number_of_bikes
        else:
            print("Invalid rental type option.")
            continue
        
        if 3 <= number_of_bikes <= 5:
            print("Do you want to avail the family pack discount?")
            discount_choice = input("y for YES, n for NO: ")
            if discount_choice.lower() == "y":
                bill *= 0.7
        
        net += bill  # Add the current bill to net revenue
        print(f"Thanks for renting. Your bill is ${bill:.2f}. Please pay at checkout.")
    
    elif choice == 4:
        print(f"Exiting. Thank you for visiting the Bike Shop!")
        print(f"Total revenue from all transactions: ${net:.2f}")
        break
    
    else:
        print("Invalid choice. Please select a valid option.")