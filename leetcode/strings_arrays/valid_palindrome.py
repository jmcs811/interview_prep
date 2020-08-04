'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        TIME: O(n)
        SPACE: O(n)
        '''
        # filter out odd chars (: , !) and make ever char lowercase
        temp = ''.join(filter(str.isalnum, s)).lower()

        # iterate through the string and check both end of the string
        # r a c e c a r
        # ^           ^
        #   ^       ^
        #     ^   ^
        #       ^
        left = 0
        right = len(temp) - 1
        while left < right:
            if temp[left] != temp[right]:
                return False
            left += 1
            right -= 1
            
        return True