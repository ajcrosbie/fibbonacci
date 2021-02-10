nums = [0, 1]
i = True
g = 0
while i:
    g = g+1
    nums.append(nums[0]+nums[1])
    nums.pop(0)
    # print(nums[1])
    if g % 10000 == 0:
        print(nums[1])
        j = input("1 to leave")
        if j == "1":
            i = False
    if len(str(nums[1])) == 1000:
        print("found it")
        i = False
        print(nums[1])
