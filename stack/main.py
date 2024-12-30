class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if (i == '(') or (i == '[') or (i == '{'):
                stack.append(i)
            else:
                # if the stack is empty and its a closing brace then return false
                if len(stack) == 0:
                    return False
                elif (i == ')' and stack[-1] == '(') or (i == ']' and stack[-1]  == '[') or (i == '}' and stack[-1]  == '{'):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0