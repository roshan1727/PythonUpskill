# For this challenge, you need to take a string as an input from the stdin, count the number of uppercase and lowercase letters and print them to the stdout.

# Input Format
# A single line of string to be taken as an input and store it in a variable of your choice. 

# Constraints
# 1 < = |s| < = 100000 

# Output Format
# print the number of uppercase letters on one line and number of lowercase letters on another side. 

# Sample TestCase 1
# Input
# I Am Awesome
# Output
# 3
# 7
# Explanation
# For the above string which is taken as input, it has 3 uppercase letters which is displayed on one line and 7 lowercase letters which is displayed on another line.

def main():
    a=input()
    b,c=0,0
    for char in a:
        if char.isupper():
            b+=1
        elif char.islower():
            c+=1
        else:
            pass
    print(b)
    print(c,end="")