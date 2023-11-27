# Specify the file path
file_path = r'f1.txt'

# Generate numbers from 1 to 84 and join them with commas
numbers = ','.join(map(str, range(1, 85)))

# Write the numbers to the file
with open(file_path, 'w') as file:
    file.write(numbers)

print(f"Numbers 1 to 84 have been written to {file_path}.")
