# strings

'''

message1 = """Mbali's World,
is Amazing!"""

print(message1) 

'''

# advanced concepts - strings

message2 = " Hello, World! "

'''
print(message2[0])
print(message2[1])
print(message2[-1])

print(len(message2))

'''

print(message2.strip()) # remove leading and trailing whitespace
print(message2.lower()) # converts all characters to lowercase
print(message2.split(',')) # split the string into a list based on the comma
print(message2.upper()) # converts characters to uppercase
print(message2.replace("Hello", "Mbali")) # replace a specific old string with a new string