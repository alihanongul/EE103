my_str = input("Input string: ")
output_str = ""

for n in range(0, len(my_str), 2):
    output_str = output_str + my_str[n]

print(output_str)
    
    