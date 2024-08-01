import random

capitals_dict = {
        'Alabama' : 'Montgomery',
        'Alaska' : 'Juneau',
        'Arizona' : 'Phoenix',
        'Arkansas' : 'Little Rock',
        'California' : 'Sacramento',
        'Colorado' : 'Denver',
        'Connecticut' : 'Hartford',
        'Delaware' : 'Dover',
        'Florida' : 'Tallahassee',
        'Georgia' : 'Atlanta',
    }

state, capital = random.choice(list(capitals_dict.items()))

print(f"state = {state}")

while True:
    cap = input("Enter the name of the capital:")
    if cap == capital:
        print("Correct")
        break
    elif cap == 'q':
        print("The correct answer is '{capital}', Goodbye")
        break
        
