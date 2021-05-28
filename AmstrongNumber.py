# For this challenge, you need to take an integer input and store it in a variable of your choice and checks whether this number is an Armstrong number or not. If yes print 'True' else print 'False'.

# Input Format
# A single integer value to be taken as input from stdin and stored it in a variable. 

# Constraints
# 1 < = n < = 18

# Output Format
# print 'True' if your number is Armstrong otherwise print 'False' to the stdout. 

# Sample TestCase 1
# Input
# 370
# Output
# True
# Explanation
# It is a armstrong Number as 3^3 + 7^3 + 0^3 = 370.

def main():
    a=int(input())  #getting input
    temp=a
    c=0
    while(temp>0):
        c=c+(temp%10)**3  #AmstrongNumber Formula
        temp//=10
    if a==c:
        print("True")
    else:
        print("False")

main()
