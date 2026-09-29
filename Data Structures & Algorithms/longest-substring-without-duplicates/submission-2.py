class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        z x y z x y z
                
        
        """
        left = 0
        seen = set()
        longest_length = 0
        for right in range(len(s)):
            cur_char = s[right]
            while cur_char in seen:
                seen.remove(s[left])
                left += 1
                    
            seen.add(cur_char)
            cur_length = right - left + 1
            longest_length = max(longest_length, cur_length)


        return longest_length
            


            
