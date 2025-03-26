# Write a Python code to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

previous_num = 0

for i in range(1, 11):
    total_sum = previous_num + i
    print("Current Number:", i, " Previous Number:",
          previous_num, " Sum:", total_sum)
    # To modify Previous Number and set it to current number
    previous_num = i
