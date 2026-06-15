weight = int(input("Weight: "))
unit = input("L(lbs) or K(kgs): ")
if unit.upper == "L":
    print(weight/2.2)
elif unit.lower == "k":
    print(weight*2.2)
