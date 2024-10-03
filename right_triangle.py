# Input the height of the triangle
n = int(input("Enter the height of the triangle: "))

# Loop to create the inverted right triangle
for i in range(n, 0, -1):  # Start from n and decrement to 1
    print('*' * i)  # Print '*' i times for each row
