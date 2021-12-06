# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


def longestCommonPrefix(strs):
        prefix=""
        curr=""
        n=len(strs[0])
        i=0
        while(i<=n-1):
            curr+=(strs[0][i])
            print(curr)
            for string in strs:
                if not string.startswith(curr):
                    return prefix
            prefix=curr
            i+=1 
        return prefix   

print(longestCommonPrefix(["flower","flower","flower","flower"]))