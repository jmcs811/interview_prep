# TIME: O(n)
# SPACE: O(n)
def valid_palindrom_naive(item):
    return ''.join(reversed(item)) == item

# TIME: O(n/2) = O(n)
# SPACE: O(1)
def valid_palindrom_clean_input(item):
    s = ''.join(filter(str.isalnum, item)).lower()

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left = left + 1
        right = right - 1
    return True

print(valid_palindrom_clean_input("A man, a plan, a canal: Panama"))