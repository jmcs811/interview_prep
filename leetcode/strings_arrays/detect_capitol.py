'''
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
 

Example 1:

Input: "USA"
Output: True
 

Example 2:

Input: "FlaG"
Output: False
'''

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        '''
        TIME: O()
        SPACE: O()
        '''
        # check capital
        temp = word.upper()
        if temp == word:
            return True
        # check not capitals
        temp = word.lower()
        if word.lower() == word:
            return True
        # check first letter
        if word[0].upper() == word[0] and word[1:].lower() == word[1:]:
            return True

        # no cases hold true, return false
        return False