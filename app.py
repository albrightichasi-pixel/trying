POUNDS_PER_KILOGRAM = 2.20462


def convert_weight(weight, unit):
    unit = unit.strip().upper()

    if unit == "L":
        return weight / POUNDS_PER_KILOGRAM, "kg"

    if unit == "K":
        return weight * POUNDS_PER_KILOGRAM, "lbs"

    raise ValueError("Unknown unit. Please enter 'L' for pounds or 'K' for kilograms.")


def main():
    try:
        weight = float(input("Weight: "))
        unit = input("L for pounds or K for kilograms: ")
        converted_weight, converted_unit = convert_weight(weight, unit)
    except ValueError as error:
        print(error)
        return

    print(f"{converted_weight:.2f} {converted_unit}")


if __name__ == "__main__":
    main()
