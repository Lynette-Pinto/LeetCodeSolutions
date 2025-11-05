s = "IcaCreAm"
s_rev=[]
vowels = "aeiouAEIOU"
reversed_vowels = []
for char in s:
    if char in vowels:
        reversed_vowels.append(char)

for char in s:
    if char in vowels:
        s_rev.append(reversed_vowels.pop())  
    else:
        s_rev.append(char)
result = "".join(s_rev)
print(result)