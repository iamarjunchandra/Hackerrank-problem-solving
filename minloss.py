"""Lauren has a chart of distinct projected prices for a house over the next several years. 
She must buy the house in one year and sell it in another, and she must do so at a loss. 
She wants to minimize her financial loss."""

n =  int(input().strip())
numbers = list(map(int,input().strip().split()))

nums = list(numbers)
nums.sort()
minCost = 10**10
for i in range(1,n):
    if (nums[i]-nums[i-1] < minCost)  and (numbers.index(nums[i]) < numbers.index(nums[i-1])):
        minCost = nums[i]-nums[i-1]
print(minCost)