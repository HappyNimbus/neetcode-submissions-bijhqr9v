class Solution:
    def isValid(self, s: str) -> bool:

        valid = { "}":"{", "]":"[", ")":"("}

        stack = []


        for c in s:

            if c in valid and stack:
                
                if stack[-1] == valid[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return not stack



    