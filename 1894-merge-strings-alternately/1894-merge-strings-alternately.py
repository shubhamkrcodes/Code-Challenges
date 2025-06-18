class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged=[]
        min_length= min(len(word1) , len(word2))
        # print(min_length)
        for i in range(min_length):
            merged.append(word1[i])
            merged.append(word2[i])
        # print(merged)
        merged.append(word1[min_length:])
        merged.append(word2[min_length:])

        return''.join(merged)
            

    

