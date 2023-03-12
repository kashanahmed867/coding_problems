def find_max_sum(numbers):
    # Initialize the two largest elements
    largest1 = 0
    largest2 = 0
    
    # Scan through the list to find the two largest elements
    for num in numbers:
        if num > largest1:
            largest2 = largest1
            largest1 = num
        elif num > largest2:
            largest2 = num
    
    # Calculate the sum of the two largest elements
    max_sum = largest1 + largest2
    
    return max_sum

print(find_max_sum([5, 9, 7,11]))
