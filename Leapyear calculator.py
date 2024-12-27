# Leap Year Calculator
def is_leap_year(year):
    """Check if a year is a leap year."""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def main():
    print("Welcome to the Leap Year Calculator!")
    while True:
        try:
            year = int(input("Enter a year (or type 0 to exit): "))
            if year == 0:
                print("Exiting the program. Goodbye!")
                break

            if is_leap_year(year):
                print(f"{year} is a leap year.")
            else:
                print(f"{year} is not a leap year.")
        except ValueError:
            print("Invalid input. Please enter a valid year.")

if __name__ == "__main__":
    main()