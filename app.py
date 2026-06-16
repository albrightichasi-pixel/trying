def main():
    try:
        weight = float(input("Weight: "))
    except ValueError:
        print("Please enter a valid number for weight.")
        return

    unit = input("L(lbs) or K(kgs): ").strip()

    if unit.upper() == "L":
        print(f"{weight / 2.2:.2f} kg")
    elif unit.upper() == "K":
        print(f"{weight * 2.2:.2f} lbs")
    else:
        print("Unknown unit. Please enter 'L' or 'K'.")


if __name__ == '__main__':
    main()
