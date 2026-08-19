class Solution(object):
    def isValid(self, s):
        stack = []
        for i in s:
            if i == '(':
                stack.append(')')
            elif i == '[':
                stack.append(']')
            elif i == '{':
                stack.append('}')
            else:
                if len(stack)==0:
                    return False
                if stack[-1] != i:
                    return False
                stack.pop()
        return len(stack) == 0    
