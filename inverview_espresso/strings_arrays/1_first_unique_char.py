
# TIME: O(n)
# SPACE: O(1)
def first_char(arr):
    char_dict = {}
    for char in arr:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    
    for i, char in enumerate(arr):
        if char_dict[char] == 1:
            return i
    return -1

# TIME: O(n^2)
# SPACE: O(1)
def first_char_alt(arr):
    for i, char in enumerate(arr):
        if arr.index(char) == arr.rindex(char):
            return i
    return -1

print(first_char('aabb'))