# problem: Implement and algorithm ot determin if a string has all unique characters.
#          What if you cannot use additional data structures.

# I/O: Input is a string. Output is a boolean value


# initial idea
# loop through the string creating a hashmap.
# if the char is not in the hashmap add it, 
# if the char is in the hashmap return false.
def is_unique(item):
    '''
    Time: O(n)
    Space: O(1) only Alphabet (26 chars)
    '''
    hs = set()
    for i in item:
        if i not in hs:
            hs.add(i)
        else:
            return False
    return True


# Second idea
# create a list with a size equal to the number of possible chars (ACSII = 128)
# if the string length is longer than 128, its false as a char would have to be repeated
def is_unique1(item):
    '''
    TIME: O(n)
    SPACE: O(1)
    '''
    ht = [None]*255
    for i in item:
        val = ord(i)
        if val == None:
            continue
        if ht[val]:
            return False
        ht[val] = True
    return True

# no aditional data structures
def is_unique2(item):
    '''
    TIME: O(N^2)
    SPACE: O(1)
    '''
    for i, char in enumerate(item):
        for j in range(i+1, len(item)):
            if item[i] == item[j]:
                return False
    return True


import unittest
class TestIsUnique(unittest.TestCase):
    def test_is_unique1(self):
        answer = is_unique("abc")
        self.assertEqual(answer, True)
        answer = is_unique1("abc")
        self.assertEqual(answer, True)


    def test_is_unique2(self):
        answer = is_unique("abca")
        self.assertEqual(answer, False)
        answer = is_unique1("abca")
        self.assertEqual(answer, False)

    def test_is_unique3(self):
        answer = is_unique("aabbcc")
        self.assertEqual(answer, False)
        answer = is_unique1("aabbcc")
        self.assertEqual(answer, False)

if __name__ == '__main__':
    unittest.main()