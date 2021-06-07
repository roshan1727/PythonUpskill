# An integer value N is passed as the input. The program must print YES if N is prime number. Else the program must print NO.

# Input Format:
# The first line denotes the value of N.

# Output Format:
# YES or NO based on if N is a prime number or not. (The OUTPUT is CASE SENSITIVE).

# Boundary Conditions:
# 2 <= N <= 9999999

# Example Input/Output 1:
# Input:
# 19

# Output:
# YES

# Example Input/Output 2:
# Input:
# 189210

# Output:
# NO


a=int(inpput())
c=0
for i in range(1,a+1):
    if(a%i==0):
        c+=1
print("YES" if c==2 else "NO")