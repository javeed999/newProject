def sum_of_evens(start, end):
    total_sum = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            total_sum += num
    return total_sum

# Input from user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Calculate and print result
result = sum_of_evens(start, end)
print(f"The sum of even numbers from {start} to {end} is: {result}")
