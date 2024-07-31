try:
    string = input("Enter a string:")
    n = int(input("Enter an integer n:"))
    character = string[n]
    print(character)
except ValueError:
    print("The entered input n is not an integer")
except IndexError:
    print("Index is out of bounds")
