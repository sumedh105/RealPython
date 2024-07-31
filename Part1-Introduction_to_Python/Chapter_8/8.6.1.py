while (1):
    try:
        user_input = int(input("Enter an integer:"))
        print(user_input)
        break
    except ValueError:
        print("The entered input is not an integer.")
