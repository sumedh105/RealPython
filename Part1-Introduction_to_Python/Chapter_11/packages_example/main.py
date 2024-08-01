# main.py

import mypackage.module1
import mypackage.module2
import mypackage.mysubpackage.module3

mypackage.module1.greet("Pythonista")
mypackage.module2.depart("Pythonista")

for person in mypackage.mysubpackage.module3.people:
    mypackage.module1.greet(person)
