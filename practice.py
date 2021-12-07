
def findsum(N,M,C,edges):
	res=[1000000]*(N)
	for i in range(1,N+1):
		for j in range(1,N+1):
			if i!=j and C[i-1]!=C[j-1]:
				for edge in edges:
					if edge[0]==i and edge[1]==j or edge[0]==j and edge[1]==i:
						res[i-1]=min(res[i-1],edge[2])
	ans=sum(res)
	print(ans)


N=5
M=6
C=[1,0,1,1,0]
edges=[[1,2,2],[2,3,1],[4,5,3],[2,4,2],[1,4,2],[1,5,3]]
findsum(N,M,C,edges)