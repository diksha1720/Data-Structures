# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
 
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        queue=[root]
        final=[]
        while(queue):
            length=len(queue)
            level_sum=0.0
            for _ in range(length):
                curr=queue.pop(0)
                if curr:
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                    level_sum += curr.val      
            final.append(level_sum/length)
        return final
 
