class Solution:

    def encode(self, strs: List[str]) -> str:
        res_s = ''
        for s in strs:
            res_s += f'{len(s)}#{s}'
        return res_s

    def decode(self, s: str) -> List[str]:
        if s == '':
            return []

        i = 0
        j = 0
        res_l = []

        while j < len(s):
            raw_j = ''
            for n in s[i:]:
                if n == '#':
                    break
                raw_j += n
            offset = len(raw_j) + 1
            j += int(raw_j) + offset
            res_l.append(s[i + offset : j])
            i = j 
        return res_l
            
        
