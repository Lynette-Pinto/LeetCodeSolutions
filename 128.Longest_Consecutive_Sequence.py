

nums=[3,3]
longest=1
count=1

sortd_ = list(set(nums))
sortd=sorted(sortd_)
print(f"sorted:{sortd}")
for i in range(len(sortd)-1):
    print(f"i:{i}, sortd[i]:{sortd[i]}, sortd[i+1]:{sortd[i+1]}")
    print(f"count:{count}")
    print(f"longest:{longest}")
    print("=============")
    if (sortd[i]+1==sortd[i+1]):
        count=count+1
        if (count>longest):
            longest=count
            print(f"new count:{count}")
            print(f"new longest:{longest}")
        
    else:
        count=1

        
print("=============")


print(f"longest:{longest}")
    
        