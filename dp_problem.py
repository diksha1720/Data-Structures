


# def total_no_of_ways(n):
# 	dp=[0]*(n+1)
# 	dp[0]=1
# 	for i in range(1,n+1):
# 		for j in range(1,6):
# 			if i-j>=0:
# 				dp[i]=dp[i]+dp[i-j]  #this line

# 	return dp[n]





# n=3
# print(total_no_of_ways(n))
def progg(items):
	n=len(items)
	count=0
	if n==0:
		yield []
	else:
		for i in range(len(items)):
			for cc in progg(items[:1]+items[i+3:]):
				yield[items[i]]+cc
				count+=1





for i in progg(list("red")):
	print(''.join(i)+",",end="")
result=progg(['t','a','n'])
next(result)
print(next(result))