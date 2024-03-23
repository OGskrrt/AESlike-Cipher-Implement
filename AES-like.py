# Define a fixed matrix
fixed_matrix = [4, 1, 1,
                0, 1, 1,
                1, 2, 1]

# Initialize shift amounts
right_shift_amount = 0
left_shift_amount = 0

# Get user input for shifting amounts
input_value = input("Enter input: ")
right_shift_amount = int(input("Enter right shift amount:"))
left_shift_amount = int(input("Enter left shift amount:"))

# S-box substitution table
s_box = {"input": [0, 1, 2, 3, 4, 5, 6, 7],
         "output": [0, 1, 6, 7, 2, 3, 4, 5]}

# Perform S-box substitution
output_value = ''.join([str(s_box["output"][s_box["input"].index(int(char))]) for char in input_value])

print("Output:", output_value)

# Divide the output into three parts
first_3 = output_value[0:3]
middle = output_value[3:6]
last_3 = output_value[6:9]

print("First:", first_3)
print("Middle:", middle)
print("Last:", last_3)

# Convert each part into binary format
binary_string = ''
for part in [first_3, middle, last_3]:
    for char in part:
        int_number = int(char)
        binary_format = format(int_number, '03b')
        print(f"{int_number}: {binary_format}")
        binary_string += str(binary_format)

print("Binary string:", binary_string)

# Function to shift left
def left_shift(binary_number, shift):
    shift %= len(binary_number)
    return binary_number[shift:] + binary_number[:shift]

# Function to shift right
def right_shift(binary_number, shift):
    shift %= len(binary_number)
    return binary_number[-shift:] + binary_number[:-shift]

# Determine which shifting operation to perform
if right_shift_amount > left_shift_amount:
    shift_amount = right_shift_amount - left_shift_amount
    shifted_binary = right_shift(binary_string, shift_amount)
elif right_shift_amount < left_shift_amount:
    shift_amount = left_shift_amount - right_shift_amount
    shifted_binary = left_shift(binary_string, shift_amount)
else:
    shift_amount = left_shift_amount
    shifted_binary = left_shift(binary_string, shift_amount)

print("Shifted binary:", shifted_binary)

# Divide the shifted binary into three parts
shifted_first_3 = shifted_binary[0:9]
shifted_middle = shifted_binary[9:18]
shifted_last_3 = shifted_binary[18:27]

# Function to group binary into groups of 3 and convert to decimal
def group_binary(binary_number):
    decimal_numbers = [int(binary_number[i:i+3], 2) for i in range(0, len(binary_number), 3)]
    return ''.join(map(str, decimal_numbers))

decimal_value = group_binary(shifted_binary)
print("Decimal value:", decimal_value)

# Convert decimal value to list
matrix_list = []
for i in decimal_value:
    matrix_list.append(i)

print("Matrix list:", matrix_list)

# Extract specific elements from the list
p0 = matrix_list[0]
p1 = matrix_list[3]
p2 = matrix_list[6]

print("p0:", p0)
print("p1:", p1)
print("p2:", p2)
