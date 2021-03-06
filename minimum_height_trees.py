# A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

# Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

# Return a list of all MHTs' root labels. You can return the answer in any order.

# The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

 




from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
                
        total_node_count = n    
        
        if total_node_count == 1:  
            
            return [0]       
        
        adj_matrix = defaultdict( set )
        
        for src_node, dst_node in edges:
            adj_matrix[src_node].add( dst_node )
            adj_matrix[dst_node].add( src_node )
          
        leave_nodes = [ node for node in adj_matrix if len(adj_matrix[node]) == 1 ]     
        while total_node_count > 2:
            
            total_node_count -= len(leave_nodes)
            
            leave_nodes_next_round = []
        
            for leaf in leave_nodes:
                
                neighbor = adj_matrix[leaf].pop()
                adj_matrix[neighbor].remove( leaf )
                
                if len(adj_matrix[neighbor]) == 1:
                    leave_nodes_next_round.append( neighbor )
                    
            leave_nodes = leave_nodes_next_round
        
        return leave_nodes          