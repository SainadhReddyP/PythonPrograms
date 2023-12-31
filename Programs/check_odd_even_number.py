while True:
    user_input = input("Enter a number (or 'end' to exit): ")

    if user_input.lower() == 'end':
        print("Exiting the program. Thank you!")
        break

    try:
        num = int(user_input)

        if num % 2 == 0:
            print(f"{num} is an even number.")
        else:
            print(f"{num} is an odd number.")
    except ValueError:
        print("Invalid input. Please enter a valid number or 'end' to exit.")
