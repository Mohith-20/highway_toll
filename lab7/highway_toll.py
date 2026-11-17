
import re


# Function 1: Parse vehicle registration number
def parse_plate(plate):

    if not isinstance(plate, str):
        return None

    pattern = r"^([A-Za-z]{2})-(\d{1,2})-([A-Za-z]{1,3})-(\d{1,4})$"

    match = re.fullmatch(pattern, plate.strip())

    if not match:
        return None

    state = match.group(1).upper()
    district = int(match.group(2))
    number = int(match.group(4))

    return state, district, number


# Function 2: Calculate trip cost
def trip_cost(text):

    if not isinstance(text, str):
        return None

    pattern = r"^\s*(\d+)\s*[xX]\s*(\d+)\s*$"

    match = re.fullmatch(pattern, text)

    if not match:
        return None

    count = int(match.group(1))
    rate = int(match.group(2))

    return count * rate


# Function 3: Classify vehicle based on axle count
def axle_class(axles):

    if isinstance(axles, bool):
        return None

    try:
        n = int(axles)

        if isinstance(axles, float) and not axles.is_integer():
            return None

        if isinstance(axles, str) and not re.fullmatch(r"\s*\+?\d+\s*", axles):
            return None

    except (ValueError, TypeError, OverflowError):
        return None

    if n <= 0:
        return None

    if n == 2:
        return "car"

    if n <= 4:
        return "truck"

    return "heavy"


# Main application
def main():

    print("==== Running parse_plate ====")
    user_input = input("Enter a plate (e.g. KA-05-AB-1234): ")
    result = parse_plate(user_input)
    print("State, District and Number:", result)

    print("\n==== Running trip_cost ====")
    user_input = input("Enter trips x rate (e.g. 3x150): ")
    result = trip_cost(user_input)
    print("Trip Cost:", result)

    print("\n==== Running axle_class ====")
    user_input = input("Enter an axle count (e.g. 3): ")
    result = axle_class(user_input)
    print("Vehicle Class:", result)


if __name__ == "__main__":
    main()
