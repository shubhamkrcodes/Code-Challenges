class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        if not word:
            return 0
        
        total = 0
        current_char = word[0]
        count = 1
        
        for char in word[1:]:
            if char == current_char:
                count += 1
            else:
                if count >= 2:
                    total += (count - 1)
                current_char = char
                count = 1
        if count >= 2:
            total += (count - 1)
        
        return total + 1