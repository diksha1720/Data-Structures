

def delta(N,K):
	ans=[]
	ans.append(K)
	for i in range(1,N+1):
		if i==K:
			ans.append(K*10)
			ans.append((i)*10+(i)+K)
		else:
			if i>K:
				ans.append(i*10+(i-K))
			if (i)*10+(i)+K<(i+1)*10:
				ans.append((i)*10+(i)+K)

	return ans[N]


N=10
K=3
print(delta(N,K))