def main():
    # Prompt the user to enter a fraction in the format X/Y
    fraction = get_fraction("Enter the fraction (e.g., X/Y):")

    # Calculate the percentage of fuel based on the fraction and display the result
    percentage = calculate_percentage(fraction)

    # Check if the tank is essentially empty (1% or less) or essentially full (99% or more),
    # and output 'E' or 'F' accordingly. Otherwise, print the calculated percentage.
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")

def get_fraction(prompt):
    while True:
        # Get the user input for the fraction
        x = input(prompt)
        try:
            # Split the input into numerator and denominator parts
            num, denom = x.split('/')
            num = int(num)
            denom = int(denom)

            # Validate the fraction: denominator cannot be zero, and numerator should be less than or equal to the denominator
            if denom == 0:
                print("Invalid input. Denominator cannot be zero.")
            elif num > denom:
                print("Invalid input. Numerator cannot be greater than the denominator.")
            else:
                return num, denom  # Return the valid fraction as integers
        except ValueError:
            print("Invalid input. Please enter a valid fraction (e.g., 'X/Y')")

def calculate_percentage(fraction):
    # Calculate the percentage of fuel by dividing the numerator by the denominator and multiplying by 100
    num, denom = fraction
    percentage = (num / denom) * 100

    # Round the percentage to the nearest integer and return the result
    return round(percentage)

if __name__ == "__main__":
    main()
