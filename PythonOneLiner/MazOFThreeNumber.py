# Fill in the blanks with code so that the program must accept three integers X, Y and Z as the input. The program must print the maximum integer among the three integers as the output.

# Boundary Condition(s):
# 1 <= X, Y, Z <= 1000

# Input Format:
# The first line contains X, Y and Z separated by a space.

# Output Format:
# The first line contains the maximum integer among the three integers.

# Example Input/Output 1:
# Input:
# 5 8 9

# Output:
# 9

# Example Input/Output 2:
# Input:
# 15 78 36

# Output:
# 78


x,y,x=[int(var) for var in input().split()]
print(X if X>Y and X>Z else Y if Y>Z else Z)