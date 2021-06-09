# accept 5 number
# print 
# a+b
# a+b+c
# a+b+c+d
# a+b+c+d+e

# inputs:
# 10 20 30 40 50

# output:
# 30
# 60
# 100
# 150

def add(*arguments):
    totalValue=sum([value for value in arguments])   #using listcomprehension we get the values nd sum it in a sum(build-in)
    return totalValue    #returning the value


a,b,c,d,e=map(int,input().strip())
print(add(a,b))
print(add(a,b,c))
print(add(a,b,c,d))
print(add(a,b,c,d,e))
