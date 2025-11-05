import math
str1 = "LEET"
str2 = "CODE"

if (str1+str2)!=(str2+str1):
    final=""
    print (final)
else:
    gcd_len=math.gcd(len(str1), len(str2))
    for i in range(0,len(str1), gcd_len):
        if str1[i:i+gcd_len] != str2[0:gcd_len]:
            final = ""
            break
        else :
            final = str1[:gcd_len]
print(final)