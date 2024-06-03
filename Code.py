class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t1 = []
        i,j = 0,0
        for x in range(max(len(s),len(t))):
            if i>len(s)-1 or j>len(t)-1:
                break
            if s[i] == t[j]:
                t1.append(s[i])
                i += 1
                j += 1

            else:
                i += 1
        return len(t)-len(t1)
            
                
