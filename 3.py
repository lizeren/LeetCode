class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}
        final = {}
        count = 0
        
        for i in s:
            if i not in dict:
                dict[i] = count
                count += 1
                if len(dict) > len(final):
                    final = dict.copy()
                print (dict)
            else:
                delete = []
                if i in dict:
                    for key,value in dict.items():
                        if (value < count):
                            delete.append(key)
                            if i == key:
                                break
                for key in delete: del dict[key]
                dict[i] = count
                if len(dict) > len(final):
                    final = dict.copy()
                print ("old dict: ",final)
                print ("new dict: ",dict)
                count += 1
                print (delete)
        return len(final)


"""
My implementation failed the last case. The weakness is that the code cannot have the head pointer skip all the chars that are between the head char and the repetitive char.
The solution does not find the string itself but focus on finding the length of that string
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""