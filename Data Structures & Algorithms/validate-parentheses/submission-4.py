class Solution:
    def isValid(self, s: str) -> bool:
        s_l = len(s)
        if s_l % 2 == 1:
            return False
        
        bracket_map = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for bracket in s:
            expected = bracket_map.get(bracket)
            if expected:
                stack.append(expected)
            elif not stack or stack.pop() != bracket:
                return False
        return not stack