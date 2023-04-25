# Open the text file "numbers.txt" in read mode
with open("numbers.txt", "r") as num_file:
    content = num_file.read()

#split content into list of integers
numbers = [int(i) for i in content.split()]

# Create two empty lists to store: odd and even integers
odd_int = []
even_int = []

# Check and sort each integer into the two empty lists
for num in numbers:
    if num % 2 == 0:
        even_int.append(str(num))
    else:
        odd_int.append(str(num))

# Create a text file "odd.txt" to write even integers
with open("even.txt", "w") as f:
    num_file.write("EVEN INTEGERS\n")
    for num in even_int:
        num_file.write(str(num) + "\n")

# Create a text file "even.txt" to write odd integers
with open("odd.txt", "w") as f:
    num_file.write("ODD INTEGERS\n")
    for num in odd_int:
        num_file.write(str(num) + "\n")