# Swaping of vowel 

# input:
# aeiouisnotvowel

# output:
# eaoiiusnotvowel

string=list(input().strip())
pair=[]
for i in range(len(string)):
    if(s[i].lower() in "aeiou"):
        if(pair):
            string[i],string[pair[1]]=pair[0],string[i]
            pair=[]
        else:
            pair=[s[i],i]
print(*string,sep="")

