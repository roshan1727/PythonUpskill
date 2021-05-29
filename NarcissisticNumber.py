# Is Your Number Narcissistic? (110 Marks)
# For this challenge, you will take an integer input and store it in a variable and checks whether the input number is a Narcissistic number or not. If it is, then print 'True' else print 'False'.

# Input Format
# A single integer value to be taken as input from stdin and stored it in a variable of your choice. 

# Constraints
# 1 < = n < = 18

# Output Format
# print 'True' if your number is Narcissistic otherwise print 'False' to the stdout. 

# Sample TestCase 1
# Input
# 1634
# Output
# True

# Explanation
# First of all, what is a Narcissistic Number?
# An n-digit number that is the sum of the nth powers of its digits is called an n-narcissistic number.

# For example, take the number 1634

# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# So, this is a Narcissistic Number.

def main():
    a=int(input())  #getting input
    b=len(str(a))
    temp=a
    c=0
    while(temp>0):
        c=c+(temp%10)**b  #formula for Narcissistic Number
        temp//=10
    if a==c:
        print("True",end="")
    else:
        print("False",end="")

main()

