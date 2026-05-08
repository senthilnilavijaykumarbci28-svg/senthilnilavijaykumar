import sys

# Get input and remove extra spaces
input_data = input().strip()

try:
    # Try to convert the input to an integer
    n = int(input_data)

    # Perform the conditional logic
    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        # This covers even numbers > 20
        print("Not Weird")

except ValueError:
    # If the input is 'senthilnila', this part runs
    print(f"Error: '{input_data}' is not a valid number. Please enter an integer.")
