# Initialize variables
previous_num = 0

# Iterate through the first 10 numbers
for current_num in range(10):
    # Calculate sum
    sum_value = previous_num + current_num

    # Print results
    print(f"Current Number: {current_num} | "
          f"Previous Number: {previous_num} | "
          f"Sum: {sum_value}")

    # Update previous_num for next iteration
    previous_num = current_num
