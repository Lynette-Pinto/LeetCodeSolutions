prices=[2,4,1]
mn=prices[0]
best=0
mx=0
for i in prices:
    if (i < mn):
        mn=i
        mx=0
    if (i > mx):
        mx=i
        best=max(best,mx-mn)
print(best)        
