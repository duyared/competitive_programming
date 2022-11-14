class Solution:
    def isValid(self, s: str) -> bool:
        pair = {')':'(','}':'{',']':'['}
        isValid = False
        s = list(s)
        stack = []
        
        for i in range(len(s)):
            if s[i] in pair.values():
                stack.append(s[i])
                
                
            else:
                if len(stack) == 0:
                    return False
                
                if stack[-1] == pair[s[i]]:
                    stack.pop()
                else:
                    return False
                
        if len(stack) == 0:
            isValid = True
            
        return isValid
    
                
        
