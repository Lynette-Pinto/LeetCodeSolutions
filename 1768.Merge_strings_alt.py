word1="ab"
word2="pqrs"
max_len=max(len(word1),len(word2))
merged=[]
for i in range(max_len):
    if i < len(word1):
        merged.append(word1[i])
    if i < len(word2):
        merged.append(word2[i])
result = "".join(merged)
print(merged)
print(result)