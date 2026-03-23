# Practice Python Debugging:

# Continue (F5): Resume execution until the next breakpoint
# Step Over (F10): Execute the current line and move to the next
# Step Into (F11): Enter into function calls
# Step Out (Shift+F11): Exit the current function

# Example code with a bug:
# Debugging Practice Program

def calculate_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    average = total / len(numbers)
    return average

def find_max(numbers):
    max_num = numbers[0]
    for n in numbers:
        if n > max_num:
            max_num = n
    return max_num

def main():
    nums = [10, 20, 30, 40, 50]
    
    avg = calculate_average(nums)
    print("Average is: " + str(avg))
    
    maximum = find_max(nums)
    print("Maximum number is:", maximum)

main()