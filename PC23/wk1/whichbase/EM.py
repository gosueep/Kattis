p = int(input())
# print(p)

actual_output = []

for i in range(p):
    k, data = input().split(" ")
    
    # Default values
    octal_value = decimal_value = hex_value = 0  # Default to 0
    
    # Octal
    if data[0] == "0" or all(d in '01234567' for d in data):
        try:
            octal_value = int(data, 8)
        except ValueError:  
            octal_value = 0  # Set to 0 if invalid octal
    
    # Decimal
    decimal_value = int(data)
    
    # Hexadecimal
    hex_value = int(data, 16)
    
    result = f"{k} {octal_value} {decimal_value} {hex_value}"
    actual_output.append(result)
    print(result)