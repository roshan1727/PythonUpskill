# Program to accept a list of integers and print the integer from the third integer as the output
# Input:
# 1 2 3 4 5 6 
# output:
# 3 4 5 6

def main():
    numList=[int(val) for val in input().split()]
    for num in numList[2:]:
        print(num,end=" ")
main()