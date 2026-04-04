class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        s1_dict={chr(ord('a')+i):0 for i in range(26)}
        s2_dict={chr(ord('a')+i):0 for i in range(26)}

        for i in range(len(s1)):
            s1_dict[s1[i]]+=1
            s2_dict[s2[i]]+=1
        
        match_count=0
        for i in range(26):
            char=chr(ord('a')+i)
            if s1_dict[char]==s2_dict[char]:
                match_count+=1
        l=0
        for r in range(len(s1),len(s2)): # since already handled for the first window thus start from second window i.e. len(s1)
            if match_count==26:
                return True

            char=s2[r]
            s2_dict[char]+=1
            if s1_dict[char] == s2_dict[char]:
                match_count+=1
            elif s1_dict[char]+1 == s2_dict[char]:
                match_count-=1
            
            char=s2[l]
            s2_dict[char]-=1
            if s1_dict[char] ==  s2_dict[char]:
                match_count+=1
            elif s1_dict[char]-1 == s2_dict[char]:
                match_count-=1
            
            l+=1
        return match_count==26

        