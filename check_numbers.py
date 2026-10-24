def check_positive_number():
    try:
        user_input=float(input("Enter the number: "))
        if user_input >0:
            print(f"Great! You enter the {user_input} positive number")
        else:
            print("Someething went wrong.")
    except ValueError:
        print("Invalid input, Enter the valid input")
check_positive_number()

