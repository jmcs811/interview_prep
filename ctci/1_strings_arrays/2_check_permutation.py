# problem: Given two strings write a a method to determine if one is a permutation of the other

# I/O: Input is two strings, Output: boolean value

# inital idea
# check if str lengths match
# sort both strings
# loop through the chars
# compare the chars
def is_permutation(str1, str2):
    '''
    TIME: O(n lg n)
    SPACE: O(n)
    '''
    if len(str1) != len(str2):
        return False
    # sort the strings
    sorted_s1 = sorted(str1)
    sorted_s2 = sorted(str2)

    # loop through the chars
    # for i, char in enumerate(sorted_s1):
    #     if char != sorted_s2[i]:
    #         return False
    
    # return True

    # or just compare the sorted strings
    return sorted_s1 == sorted_s2

# book idea
# create an array with a size equal to possible chars (128 or 255)
# loop through 1 string incrementing the count
# loop through the second string decrementing the cound
# make sure all values are 0
def is_permutation1(str1, str2):
    '''
    TIME: O(n)
    SPACE: O(1)
    '''
    ht = [0]*255
    for i in str1:
        val = ord(i)
        if val == None:
            continue
        
        ht[val] = ht[val] + 1
    
    for i in str2:
        val = ord(i)
        if val == None:
            continue

        ht[val] = ht[val] - 1

    for i in ht:
        if i != 0:
            return False
    return True

import unittest
class TestIsUnique(unittest.TestCase):
    def test_is_permuation(self):
        answer = is_permutation("aabbcc", "ccbbaa")
        self.assertEqual(answer, True)
        answer = is_permutation1("aabbcc", "ccbbaa")
        self.assertEqual(answer, True)

    def test_is_permuation1(self):
        answer = is_permutation("whats up", "not much")
        self.assertEqual(answer, False)
        answer = is_permutation1("whats up", "not much")
        self.assertEqual(answer, False)

if __name__ == '__main__':
    unittest.main()