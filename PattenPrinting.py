# The first L lines, each contains the characters of the string S based on the given conditions.

# Example Input/Output 1:
# Input:
# orange

# Output:
# oe
# roeg
# aroegn
# naroegna
# gnaroegnar
# egnaroegnaro

# Explanation:
# Here the length of the string orange is 6. So the pattern contains 6 lines.
# o e (1st and 6th characters)
# ro eg (first 2 and last 2 characters in reverse order)
# aro egn (first 3 and last 3 characters in reverse order)
# naro egna (first 4 and last 4 characters in reverse order)
# gnaro egnar (first 5 and last 5 characters in reverse order)
# egnaro egnaro (first 6 and last 6 characters in reverse order)

# Example Input/Output 2:
# Input:
# SKILLRACK

# Output:
# SK
# KSKC
# IKSKCA
# LIKSKCAR
# LLIKSKCARL
# RLLIKSKCARLL
# ARLLIKSKCARLLI
# CARLLIKSKCARLLIK
# KCARLLIKSKCARLLIKS



s=input().strip()
for i in range(1,len(s)+1):
    print(s[:i][::-1]+s[-i:][::-1])