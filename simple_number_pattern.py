def number_pyramid(rows):
    # Step 1: Iterate through the number of rows
    for i in range(1, rows + 1):
        # Step 2: Print leading spaces to make it a pyramid
        print(' ' * (rows - i), end='')  # Adjust the space before the numbers
        
        # Step 3: Print numbers in increasing order
        for j in range(1, i + 1):
            print(j, end=' ')
        
        # Move to the next line after each row is printed
        print()

# Step 4: Test the program with user input
rows = int(input("Enter the number of rows for the pyramid: "))
number_pyramid(rows)
