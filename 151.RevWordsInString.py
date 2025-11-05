s = "the sky is blue"
rev=[]
final=[]
for word in s.split(' '):
    final.append(word)
result = " ".join(final[::-1])
print(result)