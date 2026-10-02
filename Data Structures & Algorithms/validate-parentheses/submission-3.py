class Solution:
    def isValid(self, s: str) -> bool:
        s_l = len(s)
        if s_l % 2 == 1:
            return False
        
        bracket_map = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for bracket in s:
            reverse_bracket = bracket_map.get(bracket)
            if reverse_bracket is None:
                if not stack or stack.pop() != bracket:
                    return False
                continue
            stack.append(reverse_bracket)
        
        if stack:
            return False

        return True