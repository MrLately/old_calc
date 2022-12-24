# Initialize sum to 0
sum = 0

# Open the file 'income.txt' in read mode
with open('income.txt', 'r') as f:
    # Initialize a flag to determine whether the current line contains a number
    a = False
    # Iterate over each line in the file
    for line in f:
        # If the flag is True, then process the line to extract the number
        if a:
            # Initialize an empty string to store the number
            num = ''
            # Iterate over the characters in the line in reverse order
            for i in line[::-1]:
                # If the character is a dollar sign, then stop processing the line
                if(i == '$'):
                    break
                # Otherwise, add the character to the number string
                num = num+i
            # Reverse the number string so that it is in the correct order
            num = num[::-1]
            # Convert the number string to a float and add it to the sum
            sum += float(num[:-1])
        # Negate the flag so that it is True on the next iteration if the current line contained a number
        a = not(a)
# Print the total sum with a message
print(f' The total is {sum}')
