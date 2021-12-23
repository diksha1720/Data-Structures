# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty arra

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 1:
            return [0]
        
        prereq = []  # pre require course
        postreq = []  #post require course
        
        for i in range(0, numCourses):
            prereq.append(set())
            postreq.append(set())
            
        for prereqc in prerequisites:
            prereq[prereqc[0]].add(prereqc[1])
            postreq[prereqc[1]].add(prereqc[0])
            
        leafs = [] 
        newleafs = []
        res = []
        
        for i in range(0, numCourses):
			# if no pre required courses, it is read to take the course i
            if len(prereq[i]) == 0:
                leafs.append(i)
        
        while numCourses > 0:
            numCourses -= len(leafs)
			# if no leaf course but still have remained courses, it has cycle
            if len(leafs)  == 0:
                return []
			
			
            while leafs:
                l = leafs[-1]
                leafs[:] = leafs[:-1]
                res.append(l)
                # take leaf course and remove it from pre required courses
                for t in postreq[l]:
                    prereq[t].remove(l)
                    if len(prereq[t]) == 0:
                        newleafs.append(t)
            leafs[:] = newleafs
            newleafs[:] = []
        
        
        return res