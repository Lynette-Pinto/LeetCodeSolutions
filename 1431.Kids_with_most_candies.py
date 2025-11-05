candies=[2,3,5,1,3]
extraCandies = 3
max_candies=max(candies)
result = [None] * len(candies)
for i in range(len(candies)):
    if candies[i]+3 >= max_candies:
        result[i]=True
    else:
        result[i]=False

print(result)