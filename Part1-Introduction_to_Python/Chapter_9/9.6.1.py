captains = {}
print(f"captains = {captains}")

captains["Enterprise"] = "Picard"
captains["Voyager"] = "Janeway"
captains["Defiant"] = "Sisko"

print(f"captains = {captains}")

if not "Enterprise" in captains:
    print("Unknown Enterprise")
elif not "Discovery" in captains:
    print("Unknown Discovery")

for ship, captain_names in captains.items():
    print(f"The {ship} is captained by {captain_names}")

del captains["Voyager"]
print(f"captains = {captains}")

captains_new = dict(
        [
            ("Enterprise","Picard"),
            ("Voyager","Janeway"),
            ("Defiant","Sisko")
        ]
    )

print(f"captains_new = {captains_new}")
