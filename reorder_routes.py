def minReorder(n, connections):
        count=0
        stack=[]
        visited=[False]*n
        def reorder(connections,i):
            count=0
            for path in connections:
                visited[i]=True
                if path[0]==i and not visited[path[1]]:
                    temp=path[1]
                    path[1]=i
                    path[0]=temp
                    count+=1
                    print(f"count ={count} node= {i}")
                    if not visited[path[0]]:
                        stack.append(path[0]) 
                elif path[1]==i:
                    stack.append(path[0]) 
            return count
        count+=reorder(connections,0)
        while(stack):
            print(stack)
            node=stack.pop()
            if visited[node]:
                continue
            # print(node)
            count+=reorder(connections,node)
        return count
print(minReorder(5,[[1,0],[1,2],[3,2],[3,4]]))